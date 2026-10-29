# -*- coding: utf-8 -*-
"""Export PDF au style de l'app (disign/DISIGN_RULES.md §9) :
police embarquée, tokens de couleurs, titres h1, accent pour les mises
en avant, marges généreuses."""

import os
from datetime import datetime

from dotenv import load_dotenv
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (HRFlowable, KeepTogether, Paragraph,
                                SimpleDocTemplate, Spacer)

from core.theme_manager import ThemeManager

load_dotenv()

DEFAULT_SIGNATURE = "Armando Lando - bandy mlay"


class PDFExporter:

    FONT_FILES = {
        "SpaceGrotesk-Regular": os.path.join("resources", "fonts",
                                             "SpaceGrotesk-Regular.ttf"),
        "SpaceGrotesk-SemiBold": os.path.join("resources", "fonts",
                                              "SpaceGrotesk-SemiBold.ttf"),
        "SpaceGrotesk-Bold": os.path.join("resources", "fonts",
                                          "SpaceGrotesk-Bold.ttf"),
    }

    def __init__(self):
        self.tokens = ThemeManager.TOKENS["light"]
        self.signature = (os.environ.get("PDF_SIGNATURE") or
                          DEFAULT_SIGNATURE).strip()
        self._fonts_registered = False
        self._register_fonts()
        self._build_styles()

    def _register_fonts(self):
        try:
            for name, path in self.FONT_FILES.items():
                if os.path.exists(path):
                    pdfmetrics.registerFont(TTFont(name, path))
                    self._fonts_registered = True
        except Exception:
            self._fonts_registered = False

    def _font(self, weight="Regular"):
        if self._fonts_registered:
            return f"SpaceGrotesk-{weight}"
        if weight in ("SemiBold", "Bold"):
            return "Helvetica-Bold"
        return "Helvetica"

    def _build_styles(self):
        accent_hex = self.tokens["accent"]
        text_hex = self.tokens["text.primary"]
        secondary_hex = self.tokens["text.secondary"]
        muted_hex = self.tokens["text.muted"]
        self.accent = colors.HexColor(accent_hex)
        self.text_color = colors.HexColor(text_hex)
        self.secondary_color = colors.HexColor(secondary_hex)
        self.muted_color = colors.HexColor(muted_hex)

        base = getSampleStyleSheet()

        self.title_style = ParagraphStyle(
            "PdfTitle", parent=base["Heading1"],
            fontName=self._font("Bold"), fontSize=26, leading=30,
            textColor=self.text_color, alignment=0, spaceAfter=10)

        self.date_style = ParagraphStyle(
            "PdfDate", parent=base["Normal"],
            fontName=self._font("Regular"), fontSize=10, leading=14,
            textColor=self.muted_color)

        self.article_title_style = ParagraphStyle(
            "ArticleTitle", parent=base["Heading2"],
            fontName=self._font("SemiBold"), fontSize=14, leading=18,
            textColor=self.text_color, spaceAfter=6)

        self.index_style = ParagraphStyle(
            "IndexStyle", parent=base["Heading2"],
            fontName=self._font("Bold"), fontSize=16, leading=18,
            textColor=self.accent, spaceAfter=6)

        self.meta_style = ParagraphStyle(
            "MetaStyle", parent=base["Normal"],
            fontName=self._font("Regular"), fontSize=10, leading=14,
            textColor=self.secondary_color, spaceAfter=8)

        self.description_style = ParagraphStyle(
            "Description", parent=base["BodyText"],
            fontName=self._font("Regular"), fontSize=11, leading=16,
            textColor=self.secondary_color, spaceAfter=8)

        self.url_style = ParagraphStyle(
            "UrlStyle", parent=base["Normal"],
            fontName=self._font("Regular"), fontSize=10, leading=14,
            textColor=self.accent)

        self.signature_style = ParagraphStyle(
            "SignatureStyle", parent=base["Normal"],
            fontName=self._font("SemiBold"), fontSize=10, leading=15,
            textColor=self.secondary_color, alignment=TA_CENTER,
            splitLongWords=0, spaceBefore=10)

    def export_to_pdf(self, articles,
                      filename=f"news_export_"
                               f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                               f".pdf"):
        try:
            doc = SimpleDocTemplate(
                filename, pagesize=A4,
                rightMargin=2.4 * cm, leftMargin=2.4 * cm,
                topMargin=2.6 * cm, bottomMargin=2.6 * cm,
                title="Actus — Export d'articles",
                author="Actus",
            )
            story = []

            story.append(Paragraph("Rapport d'actualités", self.title_style))
            date_str = datetime.now().strftime("%d/%m/%Y à %H:%M")
            story.append(Paragraph(f"Exporté le {date_str}", self.date_style))
            story.append(Spacer(1, 14))
            story.append(self._separator())

            for index, article in enumerate(articles, 1):
                story.append(self._article_section(article, index))
                story.append(Spacer(1, 20))

            story.append(self._signature_block())
            doc.build(story)
            return True, f"PDF exporté avec succès : {filename}"
        except Exception as exc:
            return False, f"Erreur lors de l'export PDF : {exc}"

    def _separator(self):
        return HRFlowable(width="100%", thickness=1, lineCap="round",
                          color=colors.HexColor(self.tokens["chart.track"]),
                          spaceAfter=8, spaceBefore=8)

    def _article_section(self, article, index):
        elements = []

        header = Paragraph(f"{index:02d}", self.index_style)
        title = Paragraph(f"{article.get('title', 'Sans titre')}",
                          self.article_title_style)

        meta = Paragraph(
            f"<b>Source :</b> {article.get('source', 'Inconnue')} &nbsp;·&nbsp; "
            f"<b>Date :</b> {article.get('published_at', 'Date inconnue')} "
            "&nbsp;·&nbsp; "
            f"<b>Auteur :</b> {article.get('author', 'Inconnu')}",
            self.meta_style)

        description = article.get("description", "")
        if description and description != "Aucune description disponible":
            elements.append(Paragraph(description, self.description_style))

        url = article.get("url", "")
        lines = [header, title, meta]
        if description:
            lines.append(Paragraph(description, self.description_style))
        if url:
            lines.append(Paragraph(
                f"<link href='{url}'>{url}</link>", self.url_style))
        lines.append(self._separator())
        return KeepTogether(lines)

    def _signature_block(self):
        """Signature centrée (wrap auto, donc jamais de débordement)."""
        text = (self.signature.replace("&", "&amp;")
                .replace("<", "&lt;").replace(">", "&gt;"))
        return KeepTogether([
            Spacer(1, 16),
            Paragraph(
                f'<font color="{self.tokens["accent"]}">—</font>&nbsp;&nbsp;'
                f'{text}&nbsp;&nbsp;'
                f'<font color="{self.tokens["accent"]}">—</font>',
                self.signature_style),
        ])

    def export_summary_pdf(self, articles, filename="news_summary.pdf"):
        """Exporte un résumé statistique (tableau sobre)."""
        try:
            from collections import Counter

            doc = SimpleDocTemplate(filename, pagesize=A4,
                                    topMargin=2.6 * cm, bottomMargin=2.6 * cm,
                                    leftMargin=2.4 * cm,
                                    rightMargin=2.4 * cm)
            story = []
            story.append(Paragraph("Résumé statistique", self.title_style))
            story.append(self._separator())

            counter = Counter(a.get("source", "") for a in articles)
            rows = [["Statistique", "Valeur"],
                    ["Nombre total d'articles", str(len(articles))],
                    ["Sources uniques", str(len(counter))],
                    ["Sources principales",
                     ", ".join(f"{s} ({n})" for s, n in counter.most_common(
                         5)) or "—"]]

            from reportlab.platypus import Table, TableStyle

            table = Table(rows, colWidths=[6.6 * cm, 9.6 * cm])
            table.setStyle(TableStyle([
                ("FONTNAME", (0, 0), (-1, 0), self._font("Bold")),
                ("FONTNAME", (0, 1), (-1, -1), self._font("Regular")),
                ("TEXTCOLOR", (0, 0), (-1, 0), self.text_color),
                ("TEXTCOLOR", (0, 1), (-1, -1), self.secondary_color),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("LINEBELOW", (0, 0), (-1, 0), 1, self.accent),
                ("GRID", (0, 1), (-1, -1), 0.5,
                 colors.HexColor(self.tokens["chart.track"])),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            story.append(table)
            story.append(Spacer(1, 20))

            story.append(self._signature_block())

            doc.build(story)
            return True, f"Résumé PDF exporté : {filename}"
        except Exception as exc:
            return False, f"Erreur résumé PDF : {exc}"

    def generate_statistics(self, articles):
        counter = Counter(a.get("source", "") for a in articles)
        return {
            "Nombre total d'articles": len(articles),
            "Sources uniques": len(counter),
            "Source la plus fréquente":
                counter.most_common(1)[0][0] if counter else "Aucune",
        }
