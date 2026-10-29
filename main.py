# -*- coding: utf-8 -*-
"""Actus — Lecteur d'actualités (fenêtre principale).

Design system : disign/DISIGN_RULES.md (soft-neumorphism / glass).
Structure : Sidebar 220px + panneau principal radius 32 (QStackedWidget).
"""

import os
import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
                             QMessageBox, QStackedWidget, QVBoxLayout,
                             QWidget)

from api import NewsAPIClient
from analysis import DataAnalyzer
from core.favorites_manager import FavoritesManager
from core.theme_manager import ThemeManager
from pdf_exporter import PDFExporter
from ui import components as c
from ui import pages as p
from ui.article_detail import ArticleDetailDialog


# ------------------------------------------------------------------ workers (§6 / §8.7)

class FetchArticlesThread(QThread):
    articles_fetched = pyqtSignal(object)
    error_occurred = pyqtSignal(str)

    def __init__(self, api_client, category=None, query=None):
        super().__init__()
        self.api_client = api_client
        self.category = category
        self.query = query

    def run(self):
        try:
            articles = self.api_client.get_articles(
                self.category, self.query)
            self.articles_fetched.emit(articles)
        except Exception as exc:
            self.error_occurred.emit(str(exc))


class ExportThread(QThread):
    export_done = pyqtSignal(bool, str)

    def __init__(self, pdf_exporter, articles, filename):
        super().__init__()
        self.pdf_exporter = pdf_exporter
        self.articles = articles
        self.filename = filename

    def run(self):
        try:
            result = self.pdf_exporter.export_to_pdf(
                self.articles, self.filename)
            self.export_done.emit(*result)
        except Exception as exc:
            self.export_done.emit(False, f"Erreur d'export : {exc}")


# ------------------------------------------------------------------ window

class MainWindow(QMainWindow):
    PAGE_SIZE = 20

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actus — Lecteur d'actualités")
        self.setMinimumSize(1100, 700)
        self.resize(1240, 820)

        self.theme_manager = ThemeManager()
        self.api_client = NewsAPIClient()
        self.analyzer = DataAnalyzer()
        self.favorites = FavoritesManager()
        self.pdf_exporter = PDFExporter()

        self._themable = []
        self._article_cards = []
        self._threads = []

        self.all_articles = []
        self.current_page = "home"
        self.analysis_period = "day"

        self._build_ui()

    # ------------------------------------------------------------ construction

    def _build_ui(self):
        backdrop = QFrame()
        backdrop.setObjectName("AppBackground")
        self.setCentralWidget(backdrop)

        shell = QHBoxLayout(backdrop)
        shell.setContentsMargins(24, 24, 24, 24)
        shell.setSpacing(20)

        self.sidebar = c.SidebarWidget(self.theme_manager)
        self.sidebar.nav_changed.connect(self._navigate)
        self.sidebar.refresh_requested.connect(self.fetch_articles)
        self.theme_manager.apply_shadow(self.sidebar, 3)
        self._themable.append(self.sidebar)
        shell.addWidget(self.sidebar)

        self.main_panel = QFrame()
        self.main_panel.setObjectName("MainPanel")
        self.theme_manager.apply_shadow(self.main_panel, 3)
        shell.addWidget(self.main_panel, 1)

        panel_layout = QVBoxLayout(self.main_panel)
        panel_layout.setContentsMargins(0, 0, 0, 0)
        self.stacked = QStackedWidget()
        panel_layout.addWidget(self.stacked)

        self._register_themable(self._build_pages())

    def _build_pages(self):
        self.home_page = p.build_home(self)
        self.articles_page = p.build_articles(self)
        self.favorites_page = p.build_favorites(self)
        self.analysis_page = p.build_analysis(self)

        self.stacked.addWidget(self.home_page)
        self.stacked.addWidget(self.articles_page)
        self.stacked.addWidget(self.favorites_page)
        self.stacked.addWidget(self.analysis_page)
        return (self.home_page, self.articles_page, self.favorites_page,
                self.analysis_page)

    def _register_themable(self, pages):
        """Recense tout widget custom nécessitant refresh_theme (§8.2)."""
        registered = set()

        def walk(widget):
            if id(widget) in registered:
                return
            registered.add(id(widget))
            if hasattr(widget, "refresh_theme") and widget not in self._themable:
                self._themable.append(widget)
            for child in widget.findChildren(QWidget):
                walk(child)

        for page in pages:
            walk(page)

    # ------------------------------------------------------------ navigation

    def _navigate(self, key):
        mapping = {"home": self.home_page, "articles": self.articles_page,
                   "favorites": self.favorites_page,
                   "analysis": self.analysis_page}
        page = mapping.get(key, self.home_page)
        self.stacked.setCurrentWidget(page)
        self.current_page = key
        if key == "analysis":
            self.refresh_analysis()

    def handle_quick_action(self, key):
        if key == "search":
            self._navigate("articles")
            self.search_bar.input.setFocus()
        elif key == "favorites":
            self._navigate("favorites")
        elif key == "export":
            self.export_to_pdf()
        elif key == "analysis":
            self._navigate("analysis")
        elif key == "theme":
            self.toggle_theme()

    def toggle_theme(self):
        theme = self.theme_manager.toggle_theme(QApplication.instance())
        for widget in self._themable:
            widget.refresh_theme()
        self._update_theme_icon("moon" if theme == "dark" else "sun")

    def _update_theme_icon(self, icon_name):
        for action in self.quickbar.actions:
            if action.action_key == "theme":
                action.icon_name = icon_name
                action._update_icon()

    # ------------------------------------------------------------ données

    def fetch_articles(self):
        category = None
        self.start_fetch(category=None, query=None)
        self.set_busy(message="Chargement de l'actualité…")

    def start_fetch(self, category=None, query=None):
        thread = FetchArticlesThread(self.api_client, category, query)
        thread.articles_fetched.connect(self.set_articles)
        thread.error_occurred.connect(self.handle_fetch_error)
        self._threads.append(thread)
        thread.start()
        self.set_busy(True)

    def set_busy(self, busy=True, message=None):
        self.articles_refresh.setText("Chargement…" if busy else "Actualiser")
        self.articles_refresh.setEnabled(not busy)
        if not busy and message:
            self.statusBar().showMessage(message, 4000)

    def set_articles(self, articles):
        self.set_busy(False)
        self.all_articles = list(articles or [])
        self.render_articles()
        self.render_favorites()
        self.update_home_stats()
        if self.current_page == "analysis":
            self.refresh_analysis()
        self.statusBar().showMessage(
            f"{len(self.all_articles)} articles chargés.", 4000)

    def handle_fetch_error(self, error_msg):
        self.set_busy(False)
        QMessageBox.critical(self, "Erreur",
                             f"Impossible de charger les articles :\n"
                             f"{error_msg}")

    def perform_search(self, query):
        self.start_fetch(query=query)
        self.set_busy(True)

    # ------------------------------------------------------------ rendu listes

    def render_articles(self):
        while self.cards_layout.count():
            item = self.cards_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self._article_cards = []

        favorites_urls = {fav.get("url") for fav in self.favorites.favorites}
        theme = self.theme_manager
        for article in self.all_articles:
            is_fav = article.get("url") in favorites_urls
            card = c.ArticleCard(article, theme, is_favorite=is_fav)
            card.article_opened.connect(self.open_article)
            card.favorite_toggled.connect(self.toggle_favorite)
            self.cards_layout.addWidget(card)
            self._article_cards.append(card)

        if not self.all_articles:
            empty = QWidget()
            empty_layout = QVBoxLayout(empty)
            empty_layout.setContentsMargins(0, 80, 0, 0)
            note = c.make_label("Aucun article pour le moment.\n"
                                "Utilisez « Actualiser » ou la recherche.",
                                "body", c.LABEL_SECONDARY)
            note.setAlignment(Qt.AlignCenter)
            empty_layout.addWidget(note)
            self.cards_layout.addWidget(empty)

        count = len(self.all_articles)
        self.articles_card_count.setText(f"{count} article(s)")

    def render_favorites(self):
        while self.favorites_layout.count():
            item = self.favorites_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        theme = self.theme_manager
        favorites = list(self.favorites.favorites)
        for article in favorites:
            card = c.ArticleCard(article, theme, is_favorite=True)
            card.article_opened.connect(self.open_article)
            card.favorite_toggled.connect(self.toggle_favorite)
            self.favorites_layout.addWidget(card)
        if not favorites:
            empty = QWidget()
            empty_layout = QVBoxLayout(empty)
            empty_layout.setContentsMargins(0, 80, 0, 0)
            note = c.make_label(
                "Aucun favori. Ajoutez-en avec l'étoile " "★ d'une carte.",
                "body", c.LABEL_SECONDARY)
            note.setAlignment(Qt.AlignCenter)
            empty_layout.addWidget(note)
            self.favorites_layout.addWidget(empty)
        self.favorites_count.setText(f"{len(favorites)} favori(s)")

    def toggle_favorite(self, article, wanted):
        url = article.get("url", "")
        if not url:
            return
        if wanted:
            self.favorites.add_favorite(article)
        else:
            self.favorites.remove_favorite(url)
        favorites_urls = {fav.get("url") for fav in self.favorites.favorites}
        for card in self._article_cards:
            match = card.article.get("url") == url
            if match and card.star.isChecked() != (url in favorites_urls):
                card.star.setChecked(url in favorites_urls)
        self.render_favorites()

    def open_article(self, article):
        dialog = ArticleDetailDialog(article, self.theme_manager, self)
        dialog.exec_()

    # ------------------------------------------------------------ accueil stats

    def update_home_stats(self):
        stats = self.analyzer.stats(self.all_articles) \
            if self.all_articles else None
        total = len(self.all_articles)
        loaded = min(total, self.PAGE_SIZE)
        self.home_progress.setMaximum(max(1, self.PAGE_SIZE))
        self.home_progress.animate_to(loaded)
        self.home_progress_value.setText(str(loaded))
        if stats:
            self.home_goal_subtitle.setText(
                "Voici le flux du moment.")
            self.home_dark_stat.setText(stats["dominant"])
            self.home_dark_note.setText(
                f"{total} articles de {stats['sources']} sources.")
            self.stat_total.stat_value.setText(str(total))
            self.stat_sources.stat_value.setText(str(stats["sources"]))
            last = stats["last"].strftime("%d/%m") if stats["last"] else "—"
            self.stat_last.stat_value.setText(str(last))

    # ------------------------------------------------------------ analyse

    def refresh_analysis(self):
        self.analysis_period = self.analysis_segment.current_key()
        if not self.all_articles:
            self.analysis_empty.setVisible(True)
            self.analysis_bars_period.set_data([])
            self.analysis_bars_sources.set_data([])
            self.analysis_ring.set_value(0.0, animate=False)
            self.analysis_ring_value.setText("0%")
            self.analysis_ring_source.setText("—")
            self.analysis_dark_stat.setText("0")
            self.period_value.setText("")
            return
        self.analysis_empty.setVisible(False)

        stats = self.analyzer.stats(self.all_articles)
        window = self.analyzer.by_day(self.all_articles, self.analysis_period)
        sources = self.analyzer.by_source(self.all_articles, top=10)
        period_total = sum(count for _label, count in window)

        period_labels = {"day": "Journalier", "week": "Hebdomadaire",
                         "month": "Mensuel"}
        self.period_label.setText(
            f"Articles — {period_labels.get(self.analysis_period, '/')}")
        self.period_value.setText(str(period_total))
        self.analysis_dark_stat.setText(str(period_total))
        self.analysis_dark_note.setText(
            f"Total du flux : {stats['total']} articles.")
        self.analysis_bars_period.set_data(window)

        source_labeled = [(label[:12], count) for label, count in sources]
        self.analysis_bars_sources.set_data(source_labeled)

        if stats["total"]:
            share = stats["dominant_count"] / stats["total"]
            self.analysis_ring.set_value(share)
            self.analysis_ring_value.setText(f"{int(round(share * 100))}%")
            self.analysis_ring_source.setText(stats["dominant"])

    # ------------------------------------------------------------ export

    def export_to_pdf(self):
        if not self.all_articles:
            QMessageBox.warning(
                self, "Export PDF",
                "Aucun article à exporter.\n"
                "Chargez d'abord le flux depuis l'accueil ou la recherche.")
            return
        filename = (f"articles_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                    f".pdf")
        thread = ExportThread(self.pdf_exporter, self.all_articles, filename)
        thread.export_done.connect(self._on_export_done)
        self._threads.append(thread)
        thread.start()
        self.set_busy(True)

    def _on_export_done(self, ok, message):
        self.set_busy(False)
        if ok:
            QMessageBox.information(self, "Export PDF", message)
        else:
            QMessageBox.warning(self, "Export PDF", message)


def main():
    # High-DPI : à faire AVANT QApplication (§8.6)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    tm = ThemeManager()
    c.init_fonts(tm)
    tm.apply_theme(app)

    palette = QPalette()
    palette.setColor(QPalette.Highlight, tm.qcolor("accent"))
    palette.setColor(QPalette.HighlightedText, QColor("#FFFFFF"))
    app.setPalette(palette)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
