# -*- coding: utf-8 -*-
"""Détail d'article : grande carte blanche (§9), actions en pills (§4.4)."""

import webbrowser

from PyQt5.QtCore import Qt, QUrl, pyqtSignal
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import (QDialog, QFrame, QHBoxLayout, QLabel,
                             QScrollArea, QTextBrowser, QVBoxLayout,
                             QWidget)

from ui import components as c


class ArticleDetailDialog(QDialog):

    export_requested = pyqtSignal(dict)

    def __init__(self, article, theme_manager, parent=None):
        super().__init__(parent)
        self.article = dict(article)
        self.theme_manager = theme_manager
        self.setWindowTitle("Détails de l'article")
        self.setMinimumSize(860, 640)
        self.resize(900, 720)
        self._build_ui()
        self._load_article_data()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        self.card = QFrame()
        self.card.setObjectName("DetailCard")
        self.theme_manager.apply_shadow(self.card, 2)
        self._themable = []
        layout.addWidget(self.card, 1)

        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(32, 32, 32, 24)
        card_layout.setSpacing(16)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(16)

        self.title_label = QLabel()
        self.title_label.setFont(c.role_font("h1"))
        self.title_label.setObjectName(c.LABEL_PRIMARY)
        self.title_label.setWordWrap(True)
        content_layout.addWidget(self.title_label)

        row = QHBoxLayout()
        row.setSpacing(16)

        self.image = c.ImageLabel()
        self.image.set_image(self.article.get("image_url", ""), 200, 24)
        self.image.setFixedSize(260, 148)
        row.addWidget(self.image, alignment=Qt.AlignTop)

        meta_col = QVBoxLayout()
        meta_col.setSpacing(6)
        self.source_label = c.make_label("", "label", c.LABEL_SECONDARY)
        self.date_label = c.make_label("", "caption", c.LABEL_MUTED)
        self.author_label = c.make_label("", "caption", c.LABEL_MUTED)
        meta_col.addWidget(self.source_label)
        meta_col.addWidget(self.date_label)
        meta_col.addWidget(self.author_label)
        meta_col.addStretch()
        row.addLayout(meta_col, 1)
        content_layout.addLayout(row)

        self.description_box = QFrame()
        self.description_box.setObjectName("CardInset")
        desc_box_layout = QVBoxLayout(self.description_box)
        desc_box_layout.setContentsMargins(20, 16, 20, 16)
        self.description_label = QLabel()
        self.description_label.setFont(c.role_font("body"))
        self.description_label.setObjectName(c.LABEL_PRIMARY)
        self.description_label.setWordWrap(True)
        desc_box_layout.addWidget(self.description_label)
        self.description_box.setMaximumWidth(720)
        content_layout.addWidget(self.description_box)

        self.content_browser = QTextBrowser()
        self.content_browser.setFont(c.role_font("body"))
        self.content_browser.setOpenExternalLinks(True)
        self.content_browser.setMinimumHeight(140)
        self.content_browser.setMaximumWidth(720)
        content_layout.addWidget(self.content_browser, 1)
        content_layout.addStretch()

        scroll.setWidget(content)
        card_layout.addWidget(scroll, 1)

        footer = QHBoxLayout()
        close_button = c.pill_button("Fermer", "Ghost")
        close_button.clicked.connect(self.accept)
        export_button = c.pill_button("Exporter en PDF", "Secondary")
        export_button.setAccessibleName("Exporter l'article en PDF")
        export_button.clicked.connect(self._request_export)
        visit_button = c.pill_button("Visiter le site", "Primary")
        visit_button.clicked.connect(self.visit_website)
        footer.addWidget(close_button)
        footer.addWidget(export_button)
        footer.addStretch()
        footer.addWidget(visit_button)
        card_layout.addLayout(footer)

    def _request_export(self):
        """Signal export_requested : l'export est centralisé côté MainWindow."""
        self.export_requested.emit(self.article)

    def _load_article_data(self):
        self.title_label.setText(self.article.get("title", "Sans titre"))
        self.source_label.setText(
            f"Source : {self.article.get('source', 'Inconnue')}")
        self.date_label.setText(
            f"Publié le : {self.article.get('published_at', 'Date inconnue')}")
        self.author_label.setText(
            f"Auteur : {self.article.get('author', 'Inconnu')}")

        description = self.article.get("description",
                                       "Aucune description disponible")
        self.description_label.setText(description)

        content = self.article.get("content", "Contenu non disponible")
        if content and "[+" in content:
            content = content.split("[+")[0]
        self.content_browser.setHtml(
            "<html><body style=\"font-family: sans-serif; font-size: 14px;"
            " line-height: 1.5;\">%s</body></html>" % (content or ""))

    def visit_website(self):
        url = self.article.get("url", "")
        if url:
            if hasattr(QDesktopServices, "openUrl"):
                QDesktopServices.openUrl(QUrl(url))
            else:  # pragma: no cover
                webbrowser.open(url)
