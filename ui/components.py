# -*- coding: utf-8 -*-
"""Composants réutilisables du design system (disign/DISIGN_RULES.md).

Toutes les couleurs viennent des tokens du ThemeManager (jamais de valeur
en dur dans un écran — §10). Les widgets peints via QPainter lisent les
tokens au moment du dessin et exposent refresh_theme() pour la bascule
clair/sombre.
"""

import os
import re

import requests
from PyQt5.QtCore import (QRect, QPropertyAnimation, QRunnable, QObject,
                          QThreadPool, Qt, QEasingCurve, pyqtProperty,
                          pyqtSignal)
from PyQt5.QtGui import (QBrush, QColor, QFont, QIcon, QPainter, QPainterPath,
                         QPen, QPixmap)
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtWidgets import (QAbstractButton, QButtonGroup, QFrame,
                             QHBoxLayout, QLabel, QLineEdit, QProgressBar,
                             QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from core.theme_manager import parse_color

# ------------------------------------------------------------------ police (§2.3)

_FONT_FAMILY = None


def init_fonts(theme_manager):
    """Charge la police embarquée et mémorise la famille."""
    global _FONT_FAMILY
    family = theme_manager.load_fonts()
    ui_family = theme_manager.preferred_family(family)
    _FONT_FAMILY = ui_family.split(",")[0].strip().strip("'\"")
    return _FONT_FAMILY


_FONT_ROLES = {
    # role: (pixel_size, poids Qt5 0-99)
    "display": (44, 57),
    "h1": (28, 63),
    "h2": (20, 63),
    "h3": (16, 63),
    "stat": (28, 75),
    "body": (14, 50),
    "label": (12, 57),
    "caption": (11, 50),
}


def role_font(role):
    size, weight = _FONT_ROLES[role]
    font = QFont(_FONT_FAMILY or "Segoe UI")
    font.setPixelSize(size)
    font.setWeight(weight)
    return font


LABEL_PRIMARY = "LabelPrimary"
LABEL_SECONDARY = "LabelSecondary"
LABEL_MUTED = "LabelMuted"
LABEL_ON_DARK = "LabelOnDark"
LABEL_ON_DARK_MUTED = "LabelOnDarkMuted"
LABEL_ON_ACCENT = "LabelOnAccent"


def make_label(text, role="body", object_name=None):
    label = QLabel(text)
    label.setFont(role_font(role))
    if object_name:
        label.setObjectName(object_name)
    return label


# ------------------------------------------------------------------ icônes (§5)

DEFAULT_ICONS_DIR = os.path.join("resources", "icons")
_ICON_CACHE = {}


def _hex_color(color):
    try:
        return parse_color(color).name()
    except Exception:
        return color


def svg_pixmap(name, color="#111111", size=24, stroke_width=1.75,
               icons_dir=None):
    """Rend une icône SVG (style Lucide) recolorée, avec cache (§8.7)."""
    color = _hex_color(color)
    key = (name, color, size, stroke_width)
    if key in _ICON_CACHE:
        return _ICON_CACHE[key]

    icons_dir = icons_dir or DEFAULT_ICONS_DIR
    path = os.path.join(icons_dir, name + ".svg")
    if not os.path.exists(path):
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.transparent)
        return pixmap

    with open(path, "r", encoding="utf-8") as f:
        svg = f.read()

    svg = svg.replace("currentColor", color)
    svg = re.sub(r'stroke-width="[0-9.]+"', 'stroke-width="%s"' % stroke_width,
                 svg)

    renderer = QSvgRenderer(svg.encode("utf-8"))
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    renderer.render(painter)
    painter.end()

    if len(_ICON_CACHE) > 400:
        _ICON_CACHE.clear()
    _ICON_CACHE[key] = pixmap
    return pixmap


def icon_for(name, color="#111111", size=24, stroke_width=1.75):
    return QIcon(svg_pixmap(name, color, size, stroke_width))


def rounded_pixmap(source, radius):
    """Pixmap aux coins arrondis (visuels des articles)."""
    if source.isNull():
        return source
    result = QPixmap(source.size())
    result.fill(Qt.transparent)
    painter = QPainter(result)
    painter.setRenderHint(QPainter.Antialiasing)
    path = QPainterPath()
    path.addRoundedRect(0, 0, source.width(), source.height(), radius, radius)
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, source)
    painter.end()
    return result


# ------------------------------------------------------------------ images async (§8.7)

class _ImageSignal(QObject):
    fetched = pyqtSignal(str, bytes)


class _ImageFetcher(QRunnable):

    def __init__(self, url, signal):
        super().__init__()
        self.url = url
        self.signal = signal

    def run(self):
        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code == 200 and response.content:
                self.signal.fetched.emit(self.url, response.content)
        except Exception:
            pass


class ImageLabel(QLabel):
    """Image téléchargée hors du thread UI (placeholder instantané)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.radius = 16
        self._current_url = ""
        self.setFixedSize(96, 96)
        self.setScaledContents(True)
        self.setAlignment(Qt.AlignCenter)
        self._fetch_signal = _ImageSignal()
        self._fetch_signal.fetched.connect(self._on_fetched)
        self.set_image("", 96, 16)

    def set_image(self, url, size=96, radius=16):
        self.radius = radius
        self.setFixedSize(size, size)
        self._current_url = url
        self.clear()
        self.setFont(role_font("h2"))
        self.setAlignment(Qt.AlignCenter)
        if url:
            self.setText("N")
            self.setObjectName("ImagePlaceholder")
            QThreadPool.globalInstance().start(
                _ImageFetcher(url, self._fetch_signal))
        else:
            self.setObjectName("ImagePlaceholder")

    def _on_fetched(self, url, data):
        if url != self._current_url:
            return
        pixmap = QPixmap()
        if pixmap.loadFromData(data):
            self.setText("")
            self.setObjectName("")
            self.setPixmap(rounded_pixmap(pixmap, self.radius))


# ------------------------------------------------------------------ conteneurs (§4.3)

class Card(QFrame):
    """Carte radius 24, elev-1 (white=True -> raised + elev-2, §4.3)."""

    def __init__(self, theme_manager, white=False, dark=False, accent=False,
                 radius=24, parent=None):
        super().__init__(parent)
        if dark:
            object_name = "CardDark"
        elif accent:
            object_name = "CardAccent"
        elif white:
            object_name = "CardRaised"
        else:
            object_name = "Card"
        self.setObjectName(object_name)
        self.setFrameShape(QFrame.NoFrame)
        self.theme_manager = theme_manager
        self._radius = radius
        self._elev = 2 if white else 1
        self._apply_elev()

    def _apply_elev(self):
        if self.objectName() != "CardDark":
            self.theme_manager.apply_shadow(self, self._elev)

    def refresh_theme(self):
        self._apply_elev()

    def raise_elevation(self, level):
        self._elev = level
        self._apply_elev()


class HeroTitle(QLabel):
    """Grand titre display (§4.2)."""

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFont(role_font("display"))
        self.setWordWrap(True)


# ------------------------------------------------------------------ boutons (§4.4)

def pill_button(text, object_name="Secondary", parent=None):
    button = QPushButton(text, parent)
    button.setObjectName(object_name)
    button.setCursor(Qt.PointingHandCursor)
    button.setFlat(True)
    return button


class RoundButton(QPushButton):
    """Rond icône (§4.4) : inset au repos, raised au survol, accent si
    checked ou always_accent."""

    def __init__(self, icon_name, size=44, theme_manager=None,
                 always_accent=False, parent=None):
        super().__init__(parent)
        self.icon_name = icon_name
        self.btn_size = size
        self.theme_manager = theme_manager
        self.always_accent = always_accent
        self.setFixedSize(size, size)
        self.setCursor(Qt.PointingHandCursor)
        self.setCheckable(True)
        self.setFlat(True)

    def refresh_theme(self):
        self.update()

    def set_icon_name(self, name):
        self.icon_name = name
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect().adjusted(1, 1, -1, -1)
        pressed = self.isDown()

        accent = self.always_accent or self.isChecked()
        if accent:
            fill = self._accent_color()
            icon_color = self.theme_manager.color("text.on-accent")
            border = None
        elif self.isEnabled() and self.underMouse():
            fill = self.theme_manager.qcolor("bg.card.raised")
            icon_color = self.theme_manager.color("text.primary")
            border = self.theme_manager.qcolor("border.subtle")
        else:
            fill = self.theme_manager.qcolor("bg.card.inset")
            icon_color = self.theme_manager.color("text.primary")
            border = self.theme_manager.qcolor("border.subtle")

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(fill))
        painter.drawEllipse(rect)
        if border is not None:
            painter.setPen(QPen(border, 1))
            painter.setBrush(Qt.NoBrush)
            painter.drawEllipse(rect)

        drop = 1 if pressed else 0
        size = max(16, int(self.btn_size * 0.40))
        icon = svg_pixmap(self.icon_name, icon_color, size)
        painter.drawPixmap(
            rect.left() + (rect.width() - size) // 2,
            rect.top() + (rect.height() - size) // 2 + drop,
            icon)

    def _accent_color(self):
        return self.theme_manager.qcolor("accent")

    def hitButton(self, pos):
        center = self.rect().center()
        dx = pos.x() - center.x()
        dy = pos.y() - center.y()
        return dx * dx + dy * dy <= (self.btn_size / 2.0) ** 2


# ------------------------------------------------------------------ sidebar (§4.1)

class Circle(QFrame):
    """Petit disque (logo, avatar)."""

    def __init__(self, hex_bg, diameter=44, parent=None):
        super().__init__(parent)
        self.setFixedSize(diameter, diameter)
        self.setStyleSheet(
            "background: %s; border-radius: %dpx;" % (hex_bg, diameter // 2))
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)

    def set_child(self, widget):
        self._layout.addWidget(widget)


class SidebarButton(QPushButton):
    """Item de navigation 44px : cercle 32px + icône + libellé."""

    def __init__(self, key, text, icon_name, theme_manager, parent=None):
        super().__init__(text, parent)
        self.nav_key = key
        self.icon_name = icon_name
        self.theme_manager = theme_manager
        self.setCheckable(True)
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(44)
        self.setFlat(True)

    def refresh_theme(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        circle_d = 32
        circle = QRect(rect.left() + 8,
                       rect.top() + (rect.height() - circle_d) // 2,
                       circle_d, circle_d)

        painter.setPen(Qt.NoPen)
        if self.isChecked():
            painter.setBrush(QBrush(self.theme_manager.qcolor("accent")))
        elif self.underMouse():
            painter.setBrush(QBrush(QColor(255, 255, 255, 36)))
        else:
            painter.setBrush(QBrush(QColor(255, 255, 255, 20)))
        painter.drawEllipse(circle)

        icon_size = 15
        color = self.theme_manager.color("text.on-accent") \
            if self.isChecked() else "rgba(255,255,255,0.75)"
        icon = svg_pixmap(self.icon_name, color, icon_size)
        painter.drawPixmap(
            circle.left() + (circle_d - icon_size) // 2,
            circle.top() + (circle_d - icon_size) // 2,
            icon)

        text_rect = rect.adjusted(circle.right() + 10, 6, -6, -6)
        if self.isChecked():
            painter.setPen(QColor(self.theme_manager.color("text.on-dark")))
            font = role_font("label")
            font.setWeight(63)
        else:
            painter.setPen(QColor(255, 255, 255, 170))
            font = role_font("label")
        painter.setFont(font)
        painter.drawText(text_rect, int(Qt.AlignVCenter), self.text())


class SidebarWidget(QFrame):
    """Sidebar 220px : logo, navigation exclusive, CTA + éclair (§4.1)."""

    nav_changed = pyqtSignal(str)
    refresh_requested = pyqtSignal()

    NAV_ITEMS = [
        ("home", "Accueil", "home"),
        ("articles", "Articles", "newspaper"),
        ("favorites", "Favoris", "star"),
        ("analysis", "Analyse", "bar-chart-3"),
    ]

    def __init__(self, theme_manager, parent=None):
        super().__init__(parent)
        self.setObjectName("Sidebar")
        self.setFixedWidth(220)
        self.theme_manager = theme_manager

        self._group = QButtonGroup(self)
        self._group.setExclusive(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 24, 16, 16)
        layout.setSpacing(6)

        logo = Circle(theme_manager.color("bg.card.raised"), 44)
        logo_child = make_label("N", "h2", LABEL_PRIMARY)
        logo_child.setAlignment(Qt.AlignCenter)
        logo_child.setAttribute(Qt.WA_TransparentForMouseEvents)
        logo.set_child(logo_child)

        header = QHBoxLayout()
        header.setSpacing(12)
        header.addWidget(logo)

        col = QVBoxLayout()
        col.setSpacing(2)
        col.addWidget(make_label("Actus", "h2", LABEL_ON_DARK))
        col.addWidget(make_label("Lecteur d'actualités", "caption",
                                 LABEL_ON_DARK_MUTED))
        header.addLayout(col)
        header.addStretch()

        layout.addLayout(header)
        layout.addSpacing(20)

        self.buttons = {}
        for key, text, icon in self.NAV_ITEMS:
            button = SidebarButton(key, text, icon, theme_manager)
            self._group.addButton(button)
            self.buttons[key] = button
            layout.addWidget(button)
        self.buttons["home"].setChecked(True)
        for button in self.buttons.values():
            button.toggled.connect(self._on_toggled)

        layout.addStretch()
        self._build_cta(layout)

    def _on_toggled(self, checked):
        sender = self.sender()
        if checked and getattr(sender, "nav_key", None):
            self.nav_changed.emit(sender.nav_key)

    def set_active(self, key):
        if key in self.buttons:
            self.buttons[key].setChecked(True)

    def active_key(self):
        for key, button in self.buttons.items():
            if button.isChecked():
                return key
        return "home"

    def refresh_theme(self):
        for button in self.buttons.values():
            button.refresh_theme()
        self.zap.setPixmap(svg_pixmap("zap", self.theme_manager.color("accent"),
                                      30))

    def _build_cta(self, parent_layout):
        cta = QFrame()
        cta.setObjectName("SidebarCta")
        inner = QVBoxLayout(cta)
        inner.setContentsMargins(14, 14, 14, 14)
        inner.setSpacing(6)

        title = make_label("Restez informé", "h3", LABEL_ON_DARK)
        title.setWordWrap(True)
        inner.addWidget(title)
        text = make_label("Actualisez pour ne rien manquer.", "caption",
                          LABEL_ON_DARK_MUTED)
        text.setWordWrap(True)
        inner.addWidget(text)
        inner.addSpacing(6)
        refresh = pill_button("Actualiser", "SidebarCtaButton")
        refresh.clicked.connect(self.refresh_requested)
        inner.addWidget(refresh)

        self.zap = QLabel()
        self.zap.setPixmap(svg_pixmap("zap", self.theme_manager.color("accent"),
                                      26))
        self.zap.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.zap.setFixedSize(30, 30)
        self.zap.setAlignment(Qt.AlignRight | Qt.AlignTop)

        inner.addWidget(self.zap, alignment=Qt.AlignRight | Qt.AlignBottom)
        parent_layout.addWidget(cta)


# ------------------------------------------------------------------ actions rapides (§4.5)

class QuickAction(QFrame):
    clicked = pyqtSignal(str)

    def __init__(self, key, label, icon_name, theme_manager, parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.action_key = key
        self.icon_name = icon_name
        self.setObjectName("QuickAction")
        self.setFixedSize(84, 118)
        self.setCursor(Qt.PointingHandCursor)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 14, 8, 12)
        layout.setSpacing(8)

        circle = QFrame()
        circle.setObjectName("QuickActionCircle")
        circle.setFixedSize(56, 56)
        circle_layout = QVBoxLayout(circle)
        circle_layout.setContentsMargins(0, 0, 0, 0)
        self.icon = QLabel()
        self.icon.setAlignment(Qt.AlignCenter)
        self._update_icon()
        circle_layout.addWidget(self.icon)

        layout.addWidget(circle, alignment=Qt.AlignHCenter)
        text = make_label(label, "caption", LABEL_SECONDARY)
        text.setAlignment(Qt.AlignCenter)
        layout.addWidget(text)

    def _update_icon(self):
        self.icon.setPixmap(
            svg_pixmap(self.icon_name,
                       self.theme_manager.color("text.primary"), 22))

    def refresh_theme(self):
        self._update_icon()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.action_key)


class QuickActionBar(QFrame):
    action_clicked = pyqtSignal(str)

    def __init__(self, actions, theme_manager, parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.actions = []
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)
        for key, label, icon in actions:
            action = QuickAction(key, label, icon, theme_manager)
            action.clicked.connect(self.action_clicked)
            self.actions.append(action)
            layout.addWidget(action)
        layout.addStretch()

    def refresh_theme(self):
        for action in self.actions:
            action.refresh_theme()


# ------------------------------------------------------------------ contrôle segmenté (§4.9)

class SegmentedControl(QFrame):
    changed = pyqtSignal(str)

    def __init__(self, items, keys, active_index=0, parent=None):
        super().__init__(parent)
        self.setObjectName("Segmented")
        self.keys = list(keys)
        self._current_key = self.keys[active_index]
        self._active = active_index
        self.buttons = []

        self.slider = QWidget(self)
        self.slider.setObjectName("SegmentSlider")
        self.slider.setAttribute(Qt.WA_TransparentForMouseEvents)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(0)
        for i, text in enumerate(items):
            button = QPushButton(text)
            button.setObjectName("Segment")
            button.setCursor(Qt.PointingHandCursor)
            button.setMinimumHeight(32)
            button.clicked.connect(lambda _checked=False, idx=i: self.select(i))
            self.buttons.append(button)
            layout.addWidget(button, 1)

    def current_key(self):
        return self._current_key

    def select(self, index, emit=True):
        index = max(0, min(index, len(self.keys) - 1))
        self._active = index
        self._current_key = self.keys[index]
        self.move_slider(animate=True)
        if emit:
            self.changed.emit(self._current_key)

    def set_value(self, key, emit=True):
        if key in self.keys:
            self.select(self.keys.index(key), emit=emit)

    def move_slider(self, animate=False):
        if not self.buttons or self._active >= len(self.buttons):
            return
        target = self.buttons[self._active].geometry()
        if target.width() <= 0:
            return
        if animate:
            anim = QPropertyAnimation(self.slider, b"geometry", self)
            anim.setDuration(200)
            anim.setStartValue(self.slider.geometry())
            anim.setEndValue(target)
            anim.setEasingCurve(QEasingCurve.OutCubic)
            anim.start()
            self._anim = anim
        else:
            self.slider.setGeometry(target)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.move_slider(animate=False)

    def showEvent(self, event):
        super().showEvent(event)
        self.move_slider(animate=False)


# ------------------------------------------------------------------ progression (§4.6 / §4.7)

class TokenProgressBar(QProgressBar):
    """Barre pill avec animation 600ms OutCubic (§4.6)."""

    def __init__(self, maximum=100, accent=False, parent=None):
        super().__init__(parent)
        if accent:
            self.setObjectName("ProgressAccent")
        self.setMinimum(0)
        self.setMaximum(max(1, maximum))
        self.setTextVisible(False)
        self._anim = None

    def animate_to(self, value):
        anim = QPropertyAnimation(self, b"value", self)
        anim.setDuration(600)
        anim.setStartValue(self.value())
        anim.setEndValue(value)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start()
        self._anim = anim


class RingProgress(QWidget):
    """Anneau custom QPainter (§4.7) : piste inset + arc accent."""

    def __init__(self, theme_manager, size=120, thickness=10, parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.thickness = thickness
        self._value = 0.0
        self.setMinimumSize(size, size)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def get_ring_value(self):
        return self._value

    def set_ring_value(self, fraction):
        self._value = float(fraction)
        self.update()

    ringValue = pyqtProperty(float, fget=get_ring_value, fset=set_ring_value)

    def get_value(self):
        return self._value

    def set_value(self, fraction, animate=True):
        fraction = max(0.0, min(1.0, float(fraction)))
        if animate:
            anim = QPropertyAnimation(self, b"ringValue", self)
            anim.setDuration(800)
            anim.setStartValue(self._value)
            anim.setEndValue(fraction)
            anim.setEasingCurve(QEasingCurve.OutCubic)
            anim.start()
            self._anim = anim
        else:
            self._value = fraction
            self.update()

    def refresh_theme(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        track = self.theme_manager.qcolor("bg.card.inset")
        accent = self.theme_manager.qcolor("accent")

        side = min(self.width(), self.height()) - self.thickness * 2
        rect = QRect((self.width() - side) // 2,
                     (self.height() - side) // 2, side, side)

        painter.setPen(QPen(track, self.thickness, Qt.SolidLine, Qt.RoundCap))
        painter.drawArc(rect, 0, 360 * 16)
        painter.setPen(QPen(accent, self.thickness, Qt.SolidLine, Qt.RoundCap))
        span = int(360 * 16 * self._value)
        painter.drawArc(rect, 90 * 16, -span)


# ------------------------------------------------------------------ graphique barres (§4.8)

class BarChartWidget(QWidget):
    """Barres fines verticales : piste grise + remplissage sombre,
    barre max en accent, aucun axe (§4.8)."""

    def __init__(self, theme_manager, parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self._items = []
        self._highlight = -1
        self.setMinimumSize(260, 170)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def set_data(self, items, highlight_max=True):
        self._items = list(items)
        values = [v for _label, v in self._items] or [0]
        self._highlight = values.index(max(values)) if highlight_max else -1
        self.update()

    def refresh_theme(self):
        self.update()

    def paintEvent(self, event):
        if not self._items:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        track_color = self.theme_manager.qcolor("chart.track")
        bar_color = self.theme_manager.qcolor("chart.bar")
        accent = self.theme_manager.qcolor("accent")
        caption_color = self.theme_manager.qcolor("text.secondary")

        margin_left = margin_right = 16
        margin_top = 8
        caption_height = 18
        plot_height = max(10, self.height() - margin_top - caption_height)
        plot_width = max(10, self.width() - margin_left - margin_right)
        n = max(1, len(self._items))
        gap = plot_width / n
        bar_width = max(4, min(10, int(gap * 0.45)))
        radius = max(1, bar_width // 2)

        max_value = max(float(value) for _label, value in self._items)
        if max_value <= 0:
            max_value = 1.0
        caption_font = role_font("caption")
        painter.setPen(Qt.NoPen)
        for i, (label, value) in enumerate(self._items):
            center = margin_left + int(i * gap) + int(gap) // 2
            x = max(0, center - bar_width // 2)

            painter.setBrush(QBrush(track_color))
            painter.drawRoundedRect(
                QRect(x, margin_top, bar_width, plot_height),
                radius, radius)

            fraction = min(1.0, max(0.0, float(value) / max_value))
            height = max(radius * 2, int(plot_height * fraction))
            fill = accent if i == self._highlight else bar_color
            painter.setBrush(QBrush(fill))
            painter.drawRoundedRect(
                QRect(x, margin_top + plot_height - height, bar_width,
                      height),
                radius, radius)

            painter.setPen(QPen(caption_color))
            painter.setFont(caption_font)
            label_x = max(0, min(self.width() - int(gap), center - int(gap) // 2))
            painter.drawText(
                QRect(label_x, margin_top + plot_height + 4, max(1, int(gap)),
                      caption_height),
                int(Qt.AlignHCenter | Qt.AlignTop), str(label))


# ------------------------------------------------------------------ carte d'article (§9)

class ArticleCard(QFrame):
    """Carte d'article : visuel 96px, h3, source label, date caption, ★."""

    article_opened = pyqtSignal(dict)
    favorite_toggled = pyqtSignal(dict, bool)

    def __init__(self, article, theme_manager, is_favorite=False, parent=None):
        super().__init__(parent)
        self.article = dict(article)
        self.theme_manager = theme_manager
        self.setObjectName("Card")
        theme_manager.apply_shadow(self, 1)
        self.setCursor(Qt.PointingHandCursor)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        row = QHBoxLayout(self)
        row.setContentsMargins(20, 20, 20, 20)
        row.setSpacing(16)

        self.image = ImageLabel()
        self.image.set_image(self.article.get("image_url", ""), 96, 16)
        row.addWidget(self.image, alignment=Qt.AlignTop)

        col = QVBoxLayout()
        col.setSpacing(4)

        title = QLabel(self.article.get("title", "Sans titre"))
        title.setFont(role_font("h3"))
        title.setWordWrap(True)
        col.addWidget(title)

        col.addWidget(make_label(self.article.get("source", "Source inconnue"),
                                 "label", LABEL_SECONDARY))
        col.addWidget(make_label(
            self.article.get("published_at", "Date inconnue"),
            "caption", LABEL_MUTED))
        col.addStretch()

        row.addLayout(col, 1)

        self.star = RoundButton("star", 36, theme_manager)
        self.star.setChecked(bool(is_favorite))
        self.star.clicked.connect(self._toggle_favorite)
        self.star.refresh_theme()
        row.addWidget(self.star, alignment=Qt.AlignTop)

    def _toggle_favorite(self, checked):
        self.favorite_toggled.emit(self.article, bool(checked))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            child = self.childAt(event.pos())
            if not isinstance(child, QAbstractButton):
                self.article_opened.emit(self.article)

    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)

    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)


# ------------------------------------------------------------------ recherche (§4.11)

class SearchBar(QWidget):
    """Champ pill h44 + bouton rond accent d'envoi (§4.13)."""

    submitted = pyqtSignal(str)

    def __init__(self, theme_manager, placeholder="Rechercher…", parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)

        self.input = QLineEdit()
        self.input.setPlaceholderText(placeholder)
        self.input.setMinimumHeight(44)
        self.input.returnPressed.connect(self._submit)
        layout.addWidget(self.input, 1)

        self.send = RoundButton("search", 44, theme_manager,
                                always_accent=True)
        self.send.clicked.connect(self._submit)
        layout.addWidget(self.send)

    def _submit(self):
        query = self.input.text().strip()
        if query:
            self.submitted.emit(query)

    def text(self):
        return self.input.text()

    def clear(self):
        self.input.clear()

    def refresh_theme(self):
        self.send.refresh_theme()
