# -*- coding: utf-8 -*-
"""Pages de l'application, assemblées exclusivement à base des composants
du design system (disign/DISIGN_RULES.md §9).
Chaque builder prend la MainWindow et retourne le QWidget de la page.
"""

import platform
import webbrowser

from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR, Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import (QApplication, QFrame, QHBoxLayout, QScrollArea,
                             QVBoxLayout, QWidget)

from core.about_info import APP_NAME, APP_TAGLINE, APP_VERSION
from ui import components as c


# ------------------------------------------------------------------ helpers

def _v_spacer(height):
    spacer = QWidget()
    spacer.setFixedHeight(height)
    return spacer


def _open_url(url):
    """Ouvre un lien externe (e-mail -> mailto:) dans l'application liée."""
    if url.startswith("mailto:") or url.startswith("http"):
        QDesktopServices.openUrl(QUrl(url))
    else:
        webbrowser.open(url)


def _stat_card(theme_manager, title_text, value):
    card = c.Card(theme_manager)
    layout = QVBoxLayout(card)
    layout.setContentsMargins(24, 20, 24, 20)
    layout.setSpacing(4)
    layout.addWidget(c.make_label(title_text, "label", c.LABEL_SECONDARY))
    value_label = c.make_label(value, "stat", c.LABEL_PRIMARY)
    layout.addWidget(value_label)
    layout.addStretch()
    card.stat_value = value_label
    return card


def _scroll_with_cards(window):
    """Zone défilable contenant les cartes d'articles (scrollbar fine §4.12)."""
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    container = QWidget()
    window.cards_layout = QVBoxLayout(container)
    window.cards_layout.setContentsMargins(4, 4, 16, 24)
    window.cards_layout.setSpacing(16)
    window.cards_layout.setAlignment(Qt.AlignTop)
    scroll.setWidget(container)
    return scroll


def _empty_state(theme_manager, message, button_text=None, on_click=None):
    card = c.Card(theme_manager)
    layout = QVBoxLayout(card)
    layout.setContentsMargins(40, 40, 40, 40)
    layout.setSpacing(12)
    label = c.make_label(message, "body", c.LABEL_SECONDARY)
    label.setWordWrap(True)
    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label)
    if button_text and on_click:
        button = c.pill_button(button_text, "Primary")
        button.clicked.connect(on_click)
        layout.addWidget(button, alignment=Qt.AlignCenter)
    return card


def _loading_state(theme_manager):
    """Carte d'attente affichée pendant le FetchArticlesThread (§6)."""
    card = c.Card(theme_manager)
    layout = QVBoxLayout(card)
    layout.setContentsMargins(24, 20, 24, 20)
    layout.setSpacing(4)
    layout.addWidget(c.make_label("Chargement des articles…", "h3",
                                  c.LABEL_PRIMARY))
    layout.addWidget(c.make_label("Récupération du flux depuis NewsAPI.",
                                  "caption", c.LABEL_MUTED))
    return card


def _error_state(theme_manager, retry_callback):
    """Message d'échec (réseau / clé API) avec action « Réessayer ».

    Le texte d'erreur complet, produit par api.py, est écrit par
    MainWindow dans le champ error_text de la carte.
    """
    card = c.Card(theme_manager)
    layout = QVBoxLayout(card)
    layout.setContentsMargins(24, 20, 24, 20)
    layout.setSpacing(8)
    layout.addWidget(c.make_label("Impossible de charger les articles", "h3",
                                  c.LABEL_PRIMARY))
    text = c.make_label("", "body", c.LABEL_SECONDARY)
    text.setWordWrap(True)
    layout.addWidget(text)
    row = QHBoxLayout()
    row.addStretch()
    retry = c.pill_button("Réessayer", "Primary")
    retry.clicked.connect(retry_callback)
    row.addWidget(retry)
    layout.addLayout(row)
    card.error_text = text
    return card


# ------------------------------------------------------------------ accueil

def build_home(window, parent_widget=None):
    page = QWidget(parent_widget)
    root = QVBoxLayout(page)
    root.setContentsMargins(32, 32, 32, 32)
    root.setSpacing(20)

    hero = c.HeroTitle("Bonjour, prêt à lire ?")
    root.addWidget(hero)
    root.addWidget(_v_spacer(4))

    # Rangée : carte objectif + carte sombre de synthèse
    row = QHBoxLayout()
    row.setSpacing(20)

    goal_card = c.Card(window.theme_manager, white=True, radius=24)
    goal_layout = QVBoxLayout(goal_card)
    goal_layout.setContentsMargins(24, 24, 24, 24)
    goal_layout.setSpacing(8)
    goal_title = c.make_label("Objectif du flux", "h2", c.LABEL_PRIMARY)
    goal_layout.addWidget(goal_title)
    window.home_goal_subtitle = c.make_label(
        "Chargez le flux du jour.", "body", c.LABEL_SECONDARY)
    goal_layout.addWidget(window.home_goal_subtitle)
    goal_layout.addSpacing(8)
    window.home_progress = c.TokenProgressBar(20, accent=False)
    goal_layout.addWidget(window.home_progress)
    value_row = QHBoxLayout()
    window.home_progress_value = c.make_label("0", "stat", c.LABEL_PRIMARY)
    window.home_progress_total = c.make_label("/20", "label", c.LABEL_MUTED)
    value_row.addWidget(window.home_progress_value)
    value_row.addWidget(window.home_progress_total)
    value_row.addStretch()
    goal_layout.addLayout(value_row)
    row.addWidget(goal_card, 1)

    window.home_dark_card = c.Card(window.theme_manager, dark=True)
    dark_layout = QVBoxLayout(window.home_dark_card)
    dark_layout.setContentsMargins(24, 24, 24, 24)
    dark_layout.setSpacing(8)
    dark_layout.addWidget(c.make_label(
        "À la une", "label", c.LABEL_ON_DARK_MUTED))
    window.home_dark_stat = c.make_label("—", "stat", c.LABEL_ON_DARK)
    dark_layout.addWidget(window.home_dark_stat)
    window.home_dark_note = c.make_label(
        "Source la plus présente dans le flux courant.", "body",
        c.LABEL_ON_DARK_MUTED)
    window.home_dark_note.setWordWrap(True)
    dark_layout.addStretch()
    row.addWidget(window.home_dark_card, 1)

    root.addLayout(row)

    # Quick actions (§4.5 / §9)
    window.quickbar = c.QuickActionBar([
        ("search", "Rechercher", "search"),
        ("favorites", "Favoris", "star"),
        ("export", "Export PDF", "download"),
        ("analysis", "Analyse", "bar-chart-3"),
        ("theme", "Thème", "sun"),
    ], window.theme_manager)
    window.quickbar.action_clicked.connect(window.handle_quick_action)
    root.addWidget(window.quickbar)

    # Trois mini cartes de statistiques
    stats_row = QHBoxLayout()
    stats_row.setSpacing(20)
    window.stat_total = _stat_card(window.theme_manager, "Total", "0")
    window.stat_sources = _stat_card(window.theme_manager,
                                     "Sources", "0")
    window.stat_last = _stat_card(window.theme_manager,
                                  "Dernière mise à jour", "—")
    stats_row.addWidget(window.stat_total)
    stats_row.addWidget(window.stat_sources)
    stats_row.addWidget(window.stat_last)
    root.addLayout(stats_row)
    root.addStretch()

    return page


# ------------------------------------------------------------------ articles

def build_articles(window, parent_widget=None):
    page = QWidget(parent_widget)
    root = QVBoxLayout(page)
    root.setContentsMargins(32, 32, 32, 32)
    root.setSpacing(16)

    header = QHBoxLayout()
    window.articles_title = c.make_label("Articles du jour", "h1",
                                         c.LABEL_PRIMARY)
    header.addWidget(window.articles_title)
    header.addStretch()
    window.articles_refresh = c.pill_button("Actualiser", "Ghost")
    window.articles_refresh.clicked.connect(window.fetch_articles)
    header.addWidget(window.articles_refresh)
    root.addLayout(header)

    window.search_bar = c.SearchBar(window.theme_manager)
    window.search_bar.submitted.connect(window.perform_search)
    root.addWidget(window.search_bar)

    # Barre de sélection multiple (étape 3 : export PDF en lot)
    window.articles_selection_bar = c.SelectionBar(window.theme_manager)
    window.articles_selection_bar.all_clicked.connect(
        window.toggle_all_selection)
    window.articles_selection_bar.export_clicked.connect(
        window.export_selection)
    window.articles_selection_bar.cancel_clicked.connect(
        window.clear_selection)
    root.addWidget(window.articles_selection_bar)

    # États de chargement / erreur (câblés par MainWindow, §1 de la tâche)
    window.articles_loading = _loading_state(window.theme_manager)
    window.articles_loading.setVisible(False)
    root.addWidget(window.articles_loading)

    window.articles_error = _error_state(window.theme_manager,
                                         window.fetch_articles)
    window.articles_error.setVisible(False)
    root.addWidget(window.articles_error)

    window.articles_scroll = _scroll_with_cards(window)
    root.addWidget(window.articles_scroll, 1)

    window.articles_card_count = c.make_label("", "caption", c.LABEL_MUTED)
    root.addWidget(window.articles_card_count)

    return page


def build_favorites(window, parent_widget=None):
    page = QWidget(parent_widget)
    root = QVBoxLayout(page)
    root.setContentsMargins(32, 32, 32, 32)
    root.setSpacing(16)

    header = QHBoxLayout()
    window.favorites_title = c.make_label("Vos favoris", "h1",
                                          c.LABEL_PRIMARY)
    header.addWidget(window.favorites_title)
    header.addStretch()
    window.favorites_count = c.make_label("", "caption", c.LABEL_MUTED)
    header.addWidget(window.favorites_count)
    root.addLayout(header)

    # Barre de sélection multiple (étape 3) partagée avec la page Articles
    window.favorites_selection_bar = c.SelectionBar(window.theme_manager)
    window.favorites_selection_bar.all_clicked.connect(
        window.toggle_all_selection)
    window.favorites_selection_bar.export_clicked.connect(
        window.export_selection)
    window.favorites_selection_bar.cancel_clicked.connect(
        window.clear_selection)
    root.addWidget(window.favorites_selection_bar)

    window.favorites_scroll = QScrollArea()
    window.favorites_scroll.setWidgetResizable(True)
    window.favorites_scroll.setHorizontalScrollBarPolicy(
        Qt.ScrollBarAlwaysOff)
    container = QWidget()
    window.favorites_layout = QVBoxLayout(container)
    window.favorites_layout.setContentsMargins(4, 4, 16, 24)
    window.favorites_layout.setSpacing(16)
    window.favorites_layout.setAlignment(Qt.AlignTop)
    window.favorites_scroll.setWidget(container)
    root.addWidget(window.favorites_scroll, 1)

    return page


# ------------------------------------------------------------------ analyse

def build_analysis(window, parent_widget=None):
    page = QWidget(parent_widget)
    root = QVBoxLayout(page)
    root.setContentsMargins(32, 32, 32, 32)
    root.setSpacing(20)

    root.addWidget(c.make_label("Analyse des actualités", "h1",
                                c.LABEL_PRIMARY))

    window.analysis_segment = c.SegmentedControl(
        ["Jour", "Semaine", "Mois"], ["day", "week", "month"])
    window.analysis_segment.changed.connect(window.refresh_analysis)
    root.addWidget(window.analysis_segment)

    row_top = QHBoxLayout()
    row_top.setSpacing(20)

    # CardDark : chiffre clé
    window.analysis_dark = c.Card(window.theme_manager, dark=True)
    dark_layout = QVBoxLayout(window.analysis_dark)
    dark_layout.setContentsMargins(24, 24, 24, 24)
    dark_layout.setSpacing(6)
    dark_layout.addWidget(c.make_label(
        "Dernière fenêtre", "label", c.LABEL_ON_DARK_MUTED))
    window.analysis_dark_stat = c.make_label("0", "stat", c.LABEL_ON_DARK)
    dark_layout.addWidget(window.analysis_dark_stat)
    window.analysis_dark_note = c.make_label(
        "Articles publiés dans le flux sélectionné.", "caption",
        c.LABEL_ON_DARK_MUTED)
    window.analysis_dark_note.setWordWrap(True)
    dark_layout.addStretch()
    row_top.addWidget(window.analysis_dark, 1)

    # Card anneau : part de la source dominante
    window.analysis_ring_card = c.Card(window.theme_manager)
    ring_layout = QVBoxLayout(window.analysis_ring_card)
    ring_layout.setContentsMargins(24, 20, 24, 20)
    ring_layout.setSpacing(8)
    ring_layout.addWidget(c.make_label("Source dominante", "label",
                                       c.LABEL_SECONDARY))
    ring_row = QHBoxLayout()
    window.analysis_ring = c.RingProgress(window.theme_manager, 120, 10)
    ring_row.addWidget(window.analysis_ring)
    ring_col = QVBoxLayout()
    ring_col.setSpacing(4)
    window.analysis_ring_value = c.make_label("0%", "stat", c.LABEL_PRIMARY)
    window.analysis_ring_source = c.make_label(
        "—", "h3", c.LABEL_SECONDARY)
    window.analysis_ring_source.setWordWrap(True)
    ring_col.addWidget(window.analysis_ring_value)
    ring_col.addWidget(window.analysis_ring_source)
    ring_col.addStretch()
    ring_row.addLayout(ring_col, 1)
    ring_layout.addLayout(ring_row)
    ring_layout.addStretch()
    row_top.addWidget(window.analysis_ring_card, 1)

    root.addLayout(row_top)

    # Rangée du bas : deux graphes barres
    bottom = QHBoxLayout()
    bottom.setSpacing(20)
    window.analysis_period_card = c.Card(window.theme_manager)
    period_layout = QVBoxLayout(window.analysis_period_card)
    period_layout.setContentsMargins(24, 20, 24, 20)
    period_layout.setSpacing(12)
    period_header = QHBoxLayout()
    window.period_label = c.make_label("Articles", "h3", c.LABEL_PRIMARY)
    window.period_value = c.make_label("", "caption", c.LABEL_MUTED)
    period_header.addWidget(window.period_label)
    period_header.addStretch()
    period_header.addWidget(window.period_value)
    period_layout.addLayout(period_header)
    window.analysis_bars_period = c.BarChartWidget(window.theme_manager)
    period_layout.addWidget(window.analysis_bars_period, 1)
    bottom.addWidget(window.analysis_period_card, 1)

    window.analysis_sources_card = c.Card(window.theme_manager)
    sources_layout = QVBoxLayout(window.analysis_sources_card)
    sources_layout.setContentsMargins(24, 20, 24, 20)
    sources_layout.setSpacing(12)
    sources_layout.addWidget(c.make_label(
        "Top 10 sources", "h3", c.LABEL_PRIMARY))
    window.analysis_bars_sources = c.BarChartWidget(window.theme_manager)
    sources_layout.addWidget(window.analysis_bars_sources, 1)
    bottom.addWidget(window.analysis_sources_card, 1)

    root.addLayout(bottom, 1)

    empty = _empty_state(window.theme_manager,
                         "Aucune donnée à analyser. Chargez d'abord le flux "
                         "depuis l'accueil.",
                         "Charger les actualités", window.fetch_articles)
    window.analysis_empty = empty
    empty.setVisible(False)
    root.addWidget(empty)
    return page

# ------------------------------------------------------------------ à propos

def self_theme_text(theme_manager):
    """Libellé lisible du thème en cours."""
    return ("Thème sombre" if theme_manager.theme == theme_manager.DARK
            else "Thème clair")


def copy_about_infos(window):
    """Copie les infos techniques dans le presse-papiers (rapports de bug)."""
    text = "\n".join([
        f"{APP_NAME} v{APP_VERSION} — {APP_TAGLINE}",
        f"Python {platform.python_version()}",
        f"Qt {QT_VERSION_STR} / PyQt {PYQT_VERSION_STR}",
        f"Thème : {window.theme_manager.theme}",
    ])
    QApplication.clipboard().setText(text)
    window.statusBar().showMessage("Informations copiées.", 3000)


def _tech_row(title_text):
    """Rangée titre / valeur des infos techniques ; retourne (row, valeur)."""
    row = QWidget()
    layout = QHBoxLayout(row)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(12)
    label = c.make_label(title_text, "label", c.LABEL_SECONDARY)
    layout.addWidget(label)
    layout.addStretch()
    value = c.make_label("", "body", c.LABEL_PRIMARY)
    layout.addWidget(value)
    return row, value


def _build_app_card(window):
    card = c.Card(window.theme_manager)
    layout = QVBoxLayout(card)
    layout.setContentsMargins(24, 24, 24, 24)
    layout.setSpacing(16)

    header = QHBoxLayout()
    header.setSpacing(16)
    circle = c.Circle(window.theme_manager.color("bg.card.raised"), 56,
                      theme_manager=window.theme_manager,
                      token_name="bg.card.raised")
    logo = c.make_label("N", "h2", c.LABEL_PRIMARY)
    logo.setAlignment(Qt.AlignCenter)
    logo.setAttribute(Qt.WA_TransparentForMouseEvents)
    circle.set_child(logo)
    header.addWidget(circle)

    col = QVBoxLayout()
    col.setSpacing(2)
    col.addWidget(c.make_label(APP_NAME, "h2", c.LABEL_PRIMARY))
    col.addWidget(c.make_label(APP_TAGLINE, "caption", c.LABEL_MUTED))
    header.addLayout(col)
    header.addStretch()
    header.addWidget(c.Chip(f"v{APP_VERSION}", window.theme_manager))
    layout.addLayout(header)

    text = c.make_label(
        "Actus récupère le flux d'actualité mondial via NewsAPI et l'affiche "
        "dans une interface claire. Chaque article peut être ouvert en "
        "détail, marqué en favori, puis analysé par période ou par source.",
        "body", c.LABEL_SECONDARY)
    text.setWordWrap(True)
    layout.addWidget(text)
    text = c.make_label(
        "Les données peuvent être exportées en PDF (avec votre signature), "
        "en CSV ou en XLSX.",
        "body", c.LABEL_SECONDARY)
    text.setWordWrap(True)
    layout.addWidget(text)
    return card


def _build_dev_card(window, info):
    if not (info.role or info.bio or info.email or info.portfolio
            or info.github or info.linkedin):
        empty = _empty_state(
            window.theme_manager,
            "Aucune information développeur n'est renseignée "
            "(variables DEV_* du fichier .env).")
        empty.setVisible(True)
        window.about_dev_empty = empty
        return empty
    window.about_dev_empty = None

    card = c.Card(window.theme_manager, dark=True)
    layout = QVBoxLayout(card)
    layout.setContentsMargins(24, 24, 24, 24)
    layout.setSpacing(8)

    layout.addWidget(c.make_label("Le développeur", "caption",
                                  c.LABEL_ON_DARK_MUTED))
    layout.addWidget(c.make_label(info.name, "h2", c.LABEL_ON_DARK))
    if info.role:
        layout.addWidget(c.make_label(info.role, "label",
                                      c.LABEL_ON_DARK_MUTED))
    if info.bio:
        bio = c.make_label(info.bio, "body", c.LABEL_ON_DARK)
        bio.setWordWrap(True)
        layout.addWidget(bio)

    links = [("Portfolio", info.portfolio), ("GitHub", info.github),
             ("LinkedIn", info.linkedin)]
    if links or info.email:
        row = QHBoxLayout()
        row.setSpacing(12)
        for text, url in links:
            if not url:
                continue
            button = c.pill_button(text, "Secondary")
            button.clicked.connect(
                lambda _checked=False, target=url: _open_url(target))
            row.addWidget(button)
        if info.email:
            button = c.pill_button("E-mail", "Secondary")
            button.clicked.connect(
                lambda _checked=False, target=info.email:
                _open_url("mailto:" + target))
            row.addWidget(button)
        row.addStretch()
        layout.addSpacing(8)
        layout.addLayout(row)
    return card


def _build_feature_cards(window):
    cards = [
        ("newspaper", "Flux d'actualités",
         "Top headlines ou recherche par mot-clé via NewsAPI."),
        ("star", "Favoris",
         "Marquez un article : il reste sauvegardé en local."),
        ("bar-chart-3", "Analyse",
         "Statistiques par période et source dominante."),
        ("download", "Export",
         "PDF stylé avec signature, plus CSV et XLSX."),
    ]
    row = QHBoxLayout()
    row.setSpacing(16)
    for icon_name, title, text in cards:
        row.addWidget(c.FeatureCard(window.theme_manager, icon_name, title,
                                    text), 1)
    return row


def _build_chips_row(window):
    row = QHBoxLayout()
    row.setSpacing(8)
    for text in ("Python 3.12", "PyQt5", "NewsAPI", "reportlab", "openpyxl"):
        row.addWidget(c.Chip(text, window.theme_manager))
    row.addStretch()
    return row


def _build_credits_card(window):
    card = c.Card(window.theme_manager)
    layout = QVBoxLayout(card)
    layout.setContentsMargins(24, 20, 24, 20)
    layout.setSpacing(12)
    layout.addWidget(c.make_label("Crédits & licences", "h3",
                                  c.LABEL_PRIMARY))
    rows = [
        ("NewsAPI", "Source des articles d'actualité."),
        ("Space Grotesk", "Police embarquée, licence SIL OFL."),
        ("Lucide", "Icônes SVG, licence ISC."),
    ]
    for title, text in rows:
        line = QHBoxLayout()
        line.setSpacing(12)
        line.addWidget(c.make_label(title, "label", c.LABEL_SECONDARY))
        line.addStretch()
        caption = c.make_label(text, "caption", c.LABEL_MUTED)
        caption.setWordWrap(True)
        line.addWidget(caption, 2)
        layout.addLayout(line)
    return card


def _build_privacy_card(window):
    card = c.Card(window.theme_manager)
    layout = QVBoxLayout(card)
    layout.setContentsMargins(24, 20, 24, 20)
    layout.setSpacing(8)
    layout.addWidget(c.make_label("Vie privée", "h3", c.LABEL_PRIMARY))
    text = c.make_label(
        "Vos favoris restent en local (favorites.json) ; seules les requêtes "
        "vers NewsAPI quittent votre appareil.",
        "body", c.LABEL_SECONDARY)
    text.setWordWrap(True)
    layout.addWidget(text)
    return card


def _build_tech_card(window):
    card = c.Card(window.theme_manager)
    layout = QVBoxLayout(card)
    layout.setContentsMargins(24, 20, 24, 20)
    layout.setSpacing(12)
    layout.addWidget(c.make_label("Informations techniques", "h3",
                                  c.LABEL_PRIMARY))

    rows = []
    for title, value in (
            ("Application", f"{APP_NAME} v{APP_VERSION}"),
            ("Python", platform.python_version()),
            ("Qt", QT_VERSION_STR),
            ("PyQt", PYQT_VERSION_STR),
    ):
        row, value_label = _tech_row(title)
        value_label.setText(value)
        layout.addWidget(row)
        rows.append(row)

    row, window.about_theme_value = _tech_row("Thème actif")
    window.about_theme_value.setText(
        self_theme_text(window.theme_manager))
    layout.addWidget(row)

    button_row = QHBoxLayout()
    button_row.setSpacing(12)
    copier = c.pill_button("Copier", "Primary")
    copier.clicked.connect(
        lambda _checked=False: copy_about_infos(window))
    button_row.addWidget(copier)
    button_row.addStretch()
    layout.addSpacing(8)
    layout.addLayout(button_row)
    return card


def build_about(window, parent_widget=None):
    info = window.about_info
    page = QWidget(parent_widget)
    root = QVBoxLayout(page)
    root.setContentsMargins(0, 0, 0, 0)

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    reference = QWidget()
    content = QVBoxLayout(reference)
    content.setContentsMargins(32, 32, 32, 32)
    content.setSpacing(16)
    scroll.setWidget(reference)
    root.addWidget(scroll, 1)

    content.addWidget(c.HeroTitle("À propos"))
    content.addWidget(_build_app_card(window))
    content.addWidget(_build_dev_card(window, info))
    content.addLayout(_build_feature_cards(window))

    technos = c.make_label("Technologies", "h3", c.LABEL_PRIMARY)
    content.addWidget(technos)
    content.addLayout(_build_chips_row(window))

    content.addWidget(_build_credits_card(window))
    content.addWidget(_build_privacy_card(window))
    content.addWidget(_build_tech_card(window))

    if info.repo:
        card = c.Card(window.theme_manager)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(12)
        layout.addWidget(c.make_label("Liens utiles", "h3",
                                      c.LABEL_PRIMARY))
        row_links = QHBoxLayout()
        row_links.setSpacing(12)
        button = c.pill_button("Code source", "Secondary")
        button.clicked.connect(
            lambda _checked=False, target=info.repo: _open_url(target))
        row_links.addWidget(button)
        button = c.pill_button("Signaler un bug", "Secondary")
        button.clicked.connect(
            lambda _checked=False, target=info.issues: _open_url(target))
        row_links.addWidget(button)
        row_links.addStretch()
        layout.addLayout(row_links)
        content.addWidget(card)

    content.addStretch()
    return page
