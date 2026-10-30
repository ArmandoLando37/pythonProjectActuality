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
from core.about_info import load_about_info
from core.favorites_manager import FavoritesManager
from core.selection import ArticleSelection, article_key as key_of
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
        self.about_info = load_about_info()

        self._themable = []
        self._article_cards = []
        self._favorite_cards = []
        self._threads = []

        self.all_articles = []
        self.current_page = "home"
        self.analysis_period = "day"

        # État de chargement du flux (section 1) : un seul chargement à la
        # fois ; _fetch_seq rejette les réponses périmées (recherche pendant
        # un chargement) ; _last_fetch_failed mémorise l'échec pour ne pas
        # masquer la carte d'erreur après une navigation.
        self._is_loading = False
        self._fetch_seq = 0
        self._last_fetch_failed = False

        # Sélection multiple + export PDF (section 3) : un seul export à
        # la fois, le modèle de sélection est partagé par les deux pages.
        self.selection_model = ArticleSelection()
        self.selection_model.changed.connect(self._on_selection_changed)
        self._export_running = False

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
        self.about_page = p.build_about(self)

        self.stacked.addWidget(self.home_page)
        self.stacked.addWidget(self.articles_page)
        self.stacked.addWidget(self.favorites_page)
        self.stacked.addWidget(self.analysis_page)
        self.stacked.addWidget(self.about_page)
        return (self.home_page, self.articles_page, self.favorites_page,
                self.analysis_page, self.about_page)

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
                   "analysis": self.analysis_page,
                   "about": self.about_page}
        page = mapping.get(key, self.home_page)
        self.stacked.setCurrentWidget(page)
        self.current_page = key
        if key == "articles":
            self.ensure_articles_loaded()
        if key == "analysis":
            self.refresh_analysis()
        self._update_selection_bars()

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
        _apply_selection_palette(self.theme_manager, QApplication.instance())
        for widget in self._themable:
            widget.refresh_theme()
        self._update_theme_icon("moon" if theme == "dark" else "sun")
        theme_label = getattr(self, "about_theme_value", None)
        if theme_label is not None:
            theme_label.setText(p.self_theme_text(self.theme_manager))

    def _update_theme_icon(self, icon_name):
        for action in self.quickbar.actions:
            if action.action_key == "theme":
                action.icon_name = icon_name
                action._update_icon()

    # ------------------------------------------------------------ données

    def fetch_articles(self) -> None:
        """Recharge explicitement le flux (« Actualiser » / « Réessayer »)."""
        self.start_fetch()

    def ensure_articles_loaded(self) -> None:
        """Charge automatiquement le flux à l'ouverture de la page
        Articles si aucune donnée n'a jamais été récupérée.

        Ne relance pas un chargement :
        - si des articles sont déjà disponibles (lesdits restent affichés) ;
        - si un chargement est déjà en cours (_is_loading, section 1).
        """
        if self.all_articles or self._is_loading:
            return
        self.fetch_articles()

    def start_fetch(self, category: str | None = None,
                    query: str | None = None) -> None:
        """Lance le FetchArticlesThread (une requête à la fois).

        Les réponses d'une séquence périmée (recherche relancée pendant un
        chargement) sont ignorées via les fermetures seq / current_seq.
        """
        if self._is_loading and query is None:
            return
        self._fetch_seq += 1
        self._is_loading = True
        self._last_fetch_failed = False
        seq = self._fetch_seq

        thread = FetchArticlesThread(self.api_client, category, query)
        thread.articles_fetched.connect(
            lambda articles, at_seq=seq: self._on_articles_ready(
                articles, at_seq))
        thread.error_occurred.connect(
            lambda error, at_seq=seq: self._on_fetch_failed(error, at_seq))
        self._threads.append(thread)
        thread.start()

        self._show_fetch_state(loading=True)

    def _on_articles_ready(self, articles, at_seq: int) -> None:
        """Réception d'une réponse du thread : ignore les périmées."""
        if at_seq != self._fetch_seq:
            return
        self.set_articles(articles)

    def _on_fetch_failed(self, error_msg: str, at_seq: int) -> None:
        """Réception d'une erreur : ignore les périmées."""
        if at_seq != self._fetch_seq:
            return
        self.handle_fetch_error(error_msg)

    def _show_fetch_state(self, loading: bool, error_message: str = "") -> None:
        """Affiche l'état de la page Articles (chargement / erreur / neutre)."""
        button = self.articles_refresh
        button.setText("Chargement…" if loading else "Actualiser")
        button.setEnabled(not loading)
        self.articles_loading.setVisible(loading)
        if error_message:
            self.articles_error.error_text.setText(error_message)
        self.articles_error.setVisible(bool(error_message) and not loading)
        if loading:
            self.articles_card_count.setText("Chargement…")

    def set_busy(self, busy=True, message=None):
        self.articles_refresh.setText("Chargement…" if busy else "Actualiser")
        self.articles_refresh.setEnabled(not busy)
        if message is not None and not busy:
            self.statusBar().showMessage(message, 4000)

    def set_articles(self, articles):
        self._is_loading = False
        self._last_fetch_failed = False
        self.all_articles = list(articles or [])
        self.selection_model.prune_to(self.all_articles,
                                      self.favorites.favorites)
        self._show_fetch_state(loading=False)
        self.render_articles()
        self.render_favorites()
        self.update_home_stats()
        if self.current_page == "analysis":
            self.refresh_analysis()
        self.statusBar().showMessage(
            f"{len(self.all_articles)} articles chargés.", 4000)

    def handle_fetch_error(self, error_msg: str) -> None:
        """Traduit l'erreur api.py en état visible.

        Les articles déjà chargés ne sont jamais effacés (section 1) :
        avec données présentes, seul le statusBar rappelle le motif ;
        sans données, la carte d'erreur de la page propose « Réessayer ».
        """
        self._is_loading = False
        self._last_fetch_failed = True
        if self.all_articles:
            self._show_fetch_state(loading=False)
        else:
            self._show_fetch_state(loading=False, error_message=error_msg)
        self.statusBar().showMessage(error_msg, 6000)

    def perform_search(self, query: str) -> None:
        """Recherche par mot-clé : passe outre le drapeau passif (section 1)."""
        self.start_fetch(query=query)

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
            card = c.ArticleCard(article, theme, is_favorite=is_fav,
                                 selectable=True)
            card.article_opened.connect(self.open_article)
            card.favorite_toggled.connect(self.toggle_favorite)
            card.selection_changed.connect(self.toggle_article_selection)
            card.set_selected(self.selection_model.is_selected(
                key_of(article)))
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
        self._update_selection_bars()

    def render_favorites(self):
        while self.favorites_layout.count():
            item = self.favorites_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        theme = self.theme_manager
        favorites = list(self.favorites.favorites)
        self._favorite_cards = []
        for article in favorites:
            card = c.ArticleCard(article, theme, is_favorite=True,
                                 selectable=True)
            card.article_opened.connect(self.open_article)
            card.favorite_toggled.connect(self.toggle_favorite)
            card.selection_changed.connect(self.toggle_article_selection)
            card.set_selected(self.selection_model.is_selected(
                key_of(article)))
            self.favorites_layout.addWidget(card)
            self._favorite_cards.append(card)
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
        self._update_selection_bars()

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
        self.selection_model.prune_to(self.all_articles,
                                      self.favorites.favorites)
        self.render_favorites()

    def open_article(self, article):
        dialog = ArticleDetailDialog(article, self.theme_manager, self)
        dialog.export_requested.connect(self.export_single_article)
        dialog.exec_()

    # ------------------------------------------------------------ sélection (étape 3)

    def toggle_article_selection(self, article, checked):
        """Coche / décoche une carte dans le modèle partagé."""
        self.selection_model.toggle(article, checked)

    def _on_selection_changed(self):
        """Modèle modifié : resynchronise cartes, barres et compteurs."""
        for card in (self._article_cards + self._favorite_cards):
            card.set_selected(self.selection_model.is_selected(
                key_of(card.article)))
        self._update_selection_bars()

    def _current_listing(self):
        """Articles « visibles » de la page de sélection active."""
        if self.current_page == "favorites":
            return list(self.favorites.favorites)
        return list(self.all_articles)

    def _page_bar(self):
        """Barre de la page active (l'autre reste masquée)."""
        if self.current_page == "favorites":
            return self.favorites_selection_bar
        return self.articles_selection_bar

    def _update_selection_bars(self):
        """Compteur + visibilité : seule la barre de la page active s'affiche
        (dès qu'au moins une carte est cochée)."""
        count = self.selection_model.count()
        total = len(self._current_listing())
        bar = self._page_bar()
        bar.update_state(count, total)
        bar.setVisible(count > 0)
        other = (self.articles_selection_bar
                 if bar is self.favorites_selection_bar
                 else self.favorites_selection_bar)
        other.setVisible(False)

    def toggle_all_selection(self):
        """« Tout sélectionner » / « Tout désélectionner » (page active)."""
        listing = self._current_listing()
        if not listing:
            return
        model_keys = set(self.selection_model.keys())
        already_all = all(key_of(article) in model_keys
                          for article in listing)
        if already_all:
            self.selection_model.remove_all(listing)
        else:
            self.selection_model.select_all(listing)

    def clear_selection(self):
        """Bouton « Annuler » : vide la sélection (les cartes restent)."""
        self.selection_model.clear()

    def export_selection(self):
        """Exporte les articles cochés (sélection conservée)."""
        self.export_articles_to_pdf(self.selection_model.articles(),
                                    "selection")

    def export_single_article(self, article):
        """Bouton PDF du dialogue de détail (l'article affiché)."""
        name = _safe_filename(article.get("title") or "article")
        self.export_articles_to_pdf([dict(article)], name)


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
        """Action rapide « Export PDF » : tout le flux courant."""
        self.export_articles_to_pdf(self.all_articles, "articles")

    def export_articles_to_pdf(self, articles, suggested_name=None):
        """Export PDF centralisé (étape 3 + dossier du jour) : le PDF
        rejoint automatiquement pdf/<jj-mm-aaaa>/<nom>_<horodatage>.pdf
        (regroupement par date seule, heure ignorée). Tout passage
        (flux, sélection, article de détail) converge ici ; la
        sélection est conservée après l'export."""
        if not articles:
            QMessageBox.warning(
                self, "Export PDF",
                "Aucun article à exporter.\n"
                "Chargez d'abord le flux ou cochez des articles.")
            return
        if self._export_running:
            self.statusBar().showMessage("Un export PDF est déjà en cours.",
                                         4000)
            return
        day_dir = _daily_pdf_dir(datetime.now())
        os.makedirs(day_dir, exist_ok=True)
        base = _safe_filename(suggested_name or "articles")
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(day_dir, f"{base}_{stamp}.pdf")
        self._export_running = True
        thread = ExportThread(self.pdf_exporter, list(articles), path)
        thread.export_done.connect(self._on_export_done)
        self._threads.append(thread)
        thread.start()
        self.set_busy(True)

    def _on_export_done(self, ok, message):
        self._export_running = False
        self.set_busy(False)
        if ok:
            QMessageBox.information(self, "Export PDF", message)
        else:
            QMessageBox.warning(self, "Export PDF", message)


def _safe_filename(name):
    """Nom de fichier sûr Windows : ~60 premiers caractères utiles,
    caractères interdits retirés, espaces bornés."""
    cleaned = "".join(ch if ch not in '\\/:*?"<>|' else " " for ch in name)
    cleaned = " ".join(cleaned.split())[:60].strip()
    return cleaned or "export"


def _daily_pdf_dir(moment):
    """Dossier de sortie du jour : pdf/<jj-mm-aaaa>.

    Le regroupement porte sur la DATE SEULE (l'heure du nom de fichier
    est ignorée) ; `moment` est injecté pour rester testable.
    """
    return os.path.join("pdf", moment.strftime("%d-%m-%Y"))


def _apply_selection_palette(tm, app):
    """Palette de sélection (textes sélectionnés) synchronisée sur tokens."""
    palette = QPalette()
    palette.setColor(QPalette.Highlight, tm.qcolor("accent"))
    palette.setColor(QPalette.HighlightedText, tm.qcolor("text.on-accent"))
    app.setPalette(palette)


def main():
    # High-DPI : à faire AVANT QApplication (§8.6)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    tm = ThemeManager()
    c.init_fonts(tm)
    tm.apply_theme(app)
    _apply_selection_palette(tm, app)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
