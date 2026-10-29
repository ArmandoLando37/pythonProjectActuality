# -*- coding: utf-8 -*-
"""Pages de l'application, assemblées exclusivement à base des composants
du design system (disign/DISIGN_RULES.md §9).
Chaque builder prend la MainWindow et retourne le QWidget de la page.
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QFrame, QHBoxLayout, QScrollArea, QVBoxLayout,
                             QWidget)

from ui import components as c


# ------------------------------------------------------------------ helpers

def _v_spacer(height):
    spacer = QWidget()
    spacer.setFixedHeight(height)
    return spacer


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
