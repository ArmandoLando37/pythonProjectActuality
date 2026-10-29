# -*- coding: utf-8 -*-
"""Analyse des articles — données pures pour les widgets du design system
(disign/DISIGN_RULES.md §9 : SegmentedControl + RingProgress + BarChart +
CardDark). Les graphiques sont rendus nativement (QPainter), pas matplotlib.
"""

from collections import Counter
from datetime import date, datetime, timedelta


DATE_FORMATS = ("%d/%m/%Y à %H:%M", "%Y-%m-%dT%H:%M:%SZ")


class DataAnalyzer:

    def __init__(self):
        pass

    # ------------------------------------------------------------------ helpers

    @staticmethod
    def _parse_date(value):
        if not value:
            return None
        for fmt in DATE_FORMATS:
            try:
                return datetime.strptime(value, fmt).date()
            except (ValueError, TypeError):
                continue
        return None

    @staticmethod
    def _clean_articles(articles):
        prepared = []
        for article in articles:
            d = DataAnalyzer._parse_date(article.get("published_at", ""))
            prepared.append({
                "source": article.get("source", "Source inconnue"),
                "date": d,
            })
        return prepared

    # ------------------------------------------------------------------ agrégats

    def by_day(self, articles, period="day", today=None):
        """Comptage par jour / semaine / mois pour la fenêtre du contrôle
        segmenté (§9). Retourne [(label, count)]."""
        today = today or date.today()
        prepared = self._clean_articles(articles)

        if period == "week":
            prepared = self._clean_articles(articles)
            buckets = []
            monday = today - timedelta(days=today.weekday())
            for i in range(3, -1, -1):
                week_start = monday - timedelta(weeks=i)
                week_end = week_start + timedelta(days=7)
                week_number = week_start.isocalendar()[1]
                buckets.append((f"S{week_number:02d}", [
                    item for item in prepared
                    if item["date"] and week_start <= item["date"] < week_end
                ]))
            return [(label, len(group)) for label, group in buckets]

        if period == "month":
            buckets = []
            months = []
            for i in range(5, -1, -1):
                month = (today.month - i) % 12 or 12
                year = today.year - (1 if today.month - i < 1 else 0)
                months.append((year, month))
                buckets.append(0)
            month_names = ["janv", "févr", "mars", "avr", "mai",
                           "juin", "juil", "août", "sept", "oct",
                           "nov", "déc"]
            for idx, (year, month) in enumerate(months):
                for item in prepared:
                    d = item["date"]
                    if d and d.year == year and d.month == month:
                        buckets[idx] += 1
            labels = [month_names[m - 1] for (_y, m) in months]
            return list(zip(labels, buckets))

        # period == "day" : 7 derniers jours
        counts = {}
        labels = []
        day_names = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
        for i in range(6, -1, -1):
            day = today - timedelta(days=i)
            labels.append(f"{day_names[day.weekday()]} {day.day:02d}")
            counts[day] = 0
        for item in prepared:
            d = item["date"]
            if d and d in counts:
                counts[d] += 1
        return list(zip(labels, counts.values()))

    def by_source(self, articles, top=10):
        """Top N sources [(source, count)]."""
        counter = Counter(a.get("source", "Source inconnue")
                          for a in articles)
        return counter.most_common(top)

    def stats(self, articles):
        aggregate = self._clean_articles(articles)
        sources = Counter(a["source"] for a in aggregate)
        dates = [a["date"] for a in aggregate if a["date"]]
        return {
            "total": len(articles),
            "sources": len(sources),
            "dominant": sources.most_common(1)[0][0] if sources else "—",
            "dominant_count": sources.most_common(1)[0][1] if sources else 0,
            "last": max(dates) if dates else None,
        }

    # ------------------------------------------------------------------ export CSV

    def export_to_csv(self, articles, filename="news_analysis.csv"):
        """Exporte les données d'articles vers un fichier CSV."""
        import pandas as pd

        if not articles:
            return False
        rows = [{
            "title": a.get("title", ""),
            "source": a.get("source", ""),
            "published_at": a.get("published_at", ""),
            "author": a.get("author", ""),
        } for a in articles]
        pd.DataFrame(rows).to_csv(filename, index=False, encoding="utf-8")
        return True
