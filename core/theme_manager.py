import os
import re
from string import Template

from PyQt5.QtGui import QColor, QFontDatabase


class ThemeManager:
    """Source unique du design (disign/DISIGN_RULES.md).

    - Tokens de couleurs clair/sombre (§2).
    - Construction du QSS à partir de resources/style.css avec $placeholders (§8.2).
    - Ombres diffuseurs via QGraphicsDropShadowEffect (§8.3).
    - Bascule et persistance du thème.
    """

    LIGHT = "light"
    DARK = "dark"

    FONT_FILES = (
        "SpaceGrotesk-Light.ttf",
        "SpaceGrotesk-Regular.ttf",
        "SpaceGrotesk-Medium.ttf",
        "SpaceGrotesk-SemiBold.ttf",
        "SpaceGrotesk-Bold.ttf",
    )

    ELEVATIONS = {
        1: (24, 6, 20),
        2: (36, 12, 31),
        3: (60, 24, 46),
    }

    TOKENS = {
        "light": {
            "font.family": "'Space Grotesk', 'Segoe UI Variable', 'Segoe UI', sans-serif",
            "bg.gradient.top": "#C9C9C9",
            "bg.gradient.bottom": "#DADADA",
            "bg.surface": "#EFEFEF",
            "bg.card": "#F6F6F6",
            "bg.card.raised": "#FFFFFF",
            "bg.card.inset": "#E9E9E9",
            "bg.sidebar.top": "#4B4B4B",
            "bg.sidebar.bottom": "#2F2F2F",
            "bg.card.dark.top": "#5A5A5A",
            "bg.card.dark.bottom": "#3A3A3A",
            "accent": "#E8603C",
            "accent.hover": "#F07350",
            "accent.pressed": "#CF4F2D",
            "accent.soft": "rgba(232, 96, 60, 0.18)",
            "text.primary": "#111111",
            "text.secondary": "#6B6B6B",
            "text.muted": "#9A9A9A",
            "text.on-dark": "#FFFFFF",
            "text.on-dark.muted": "rgba(255, 255, 255, 0.60)",
            "text.on-accent": "#FFFFFF",
            "border.subtle": "rgba(255, 255, 255, 0.65)",
            "shadow": "rgba(0, 0, 0, 0.10)",
            "scrollbar": "rgba(0, 0, 0, 0.18)",
            "scrollbar.hover": "rgba(0, 0, 0, 0.30)",
            "chart.track": "#E3E3E3",
            "chart.bar": "#111111",
            "success": "#3FA66B",
            "warning": "#E8A23C",
            "error": "#D64545",
        },
        "dark": {
            "font.family": "'Space Grotesk', 'Segoe UI Variable', 'Segoe UI', sans-serif",
            "bg.gradient.top": "#121212",
            "bg.gradient.bottom": "#1B1B1B",
            "bg.surface": "#1E1E1E",
            "bg.card": "#262626",
            "bg.card.raised": "#2E2E2E",
            "bg.card.inset": "#1A1A1A",
            "bg.sidebar.top": "#2A2A2A",
            "bg.sidebar.bottom": "#151515",
            "bg.card.dark.top": "#303030",
            "bg.card.dark.bottom": "#1C1C1C",
            "accent": "#F0714D",
            "accent.hover": "#F98A6B",
            "accent.pressed": "#D45A33",
            "accent.soft": "rgba(240, 113, 77, 0.22)",
            "text.primary": "#F2F2F2",
            "text.secondary": "#A8A8A8",
            "text.muted": "#707070",
            "text.on-dark": "#FFFFFF",
            "text.on-dark.muted": "rgba(255, 255, 255, 0.60)",
            "text.on-accent": "#FFFFFF",
            "border.subtle": "rgba(255, 255, 255, 0.10)",
            "shadow": "rgba(0, 0, 0, 0.45)",
            "scrollbar": "rgba(255, 255, 255, 0.18)",
            "scrollbar.hover": "rgba(255, 255, 255, 0.30)",
            "chart.track": "#333333",
            "chart.bar": "#F2F2F2",
            "success": "#4BB578",
            "warning": "#F0AC4A",
            "error": "#E05A5A",
        },
    }

    def __init__(self, resources_dir="resources", prefs_filename="ui_prefs.json"):
        self.resources_dir = resources_dir
        self.prefs_filename = prefs_filename
        self.template_path = os.path.join(resources_dir, "style.css")
        self.fonts_dir = os.path.join(resources_dir, "fonts")
        self.icons_dir = os.path.join(resources_dir, "icons")
        self.theme = self.load_prefs().get("theme", self.LIGHT)

    # ----------------------------- tokens

    def tokens(self, theme=None):
        return dict(self.TOKENS[theme or self.theme])

    def color(self, name, theme=None):
        """Valeur brute du token (ex. '#E8603C' ou 'rgba(...)')."""
        return self.TOKENS[theme or self.theme][name]

    def qcolor(self, name, theme=None):
        """Token converti en QColor pour le dessin custom (paintEvent)."""
        return parse_color(self.color(name, theme))

    # ----------------------------- ombres (§8.3)

    def shadow_levels(self, theme=None):
        """{niveau: (blurRadius, dy, alpha)} pour apply_shadow (§2.6)."""
        theme = theme or self.theme
        alphas = (46, 62, 90) if theme == self.DARK else (20, 31, 46)
        levels = {}
        for lvl, (blur, dy, _norm) in self.ELEVATIONS.items():
            alpha = alphas[lvl - 1]
            levels[lvl] = (blur, dy, alpha, QColor(0, 0, 0, alpha))
        return levels

    def apply_shadow(self, widget, level=1):
        """Pose UNE ombre diffuse sur un conteneur (un seul effet par widget)."""
        from PyQt5.QtWidgets import QGraphicsDropShadowEffect

        blur, dy, _alpha, color = self.shadow_levels()[level]
        effect = QGraphicsDropShadowEffect(widget)
        effect.setBlurRadius(blur)
        effect.setOffset(0, dy)
        effect.setColor(QColor(color))
        widget.setGraphicsEffect(effect)

    # ----------------------------- QSS (§8.2)

    def build_qss(self, theme=None, template=None):
        theme = theme or self.theme
        if template is None:
            template = self.read_template()
        qss = Template(template)
        # string.Template n'accepte pas '.' ni '-' : bg.card / on-dark ->
        # bg_card / on_dark
        mapping = {re.sub(r"[.\-]", "_", k): v
                   for k, v in self.tokens(theme).items()}
        return qss.substitute(mapping)

    def read_template(self):
        if os.path.exists(self.template_path):
            with open(self.template_path, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    def apply_theme(self, app):
        app.setStyleSheet(self.build_qss(self.theme))

    def switch_theme(self, name, app):
        if name not in self.TOKENS:
            return self.theme
        self.theme = name
        self.apply_theme(app)
        self.save_prefs()
        return name

    def toggle_theme(self, app):
        return self.switch_theme(
            self.DARK if self.theme == self.LIGHT else self.LIGHT, app
        )

    # ----------------------------- persistance

    def load_prefs(self):
        try:
            import json

            if os.path.exists(self.prefs_filename):
                with open(self.prefs_filename, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        return {}

    def save_prefs(self):
        try:
            import json

            data = self.load_prefs()
            data["theme"] = self.theme
            with open(self.prefs_filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    # ----------------------------- polices (§2.3, §8.1)

    def load_fonts(self):
        loaded = None
        for filename in self.FONT_FILES:
            path = os.path.join(self.fonts_dir, filename)
            if not os.path.exists(path):
                continue
            font_id = QFontDatabase.addApplicationFont(path)
            families = []
            if font_id != -1:
                families = QFontDatabase.applicationFontFamilies(font_id)
            if families:
                if "Space Grotesk" in families:
                    return "Space Grotesk"
                loaded = families[0]
        return loaded

    def preferred_family(self, loaded_family):
        if loaded_family:
            return loaded_family
        return "Segoe UI Variable, Segoe UI"

    # ----------------------------- icônes (§5)

    def icon_path(self, name):
        return os.path.join(self.icons_dir, name + ".svg")

    def icon_exists(self, name):
        return os.path.exists(self.icon_path(name))


def parse_color(value):
    """'rgba(232, 96, 60, 0.18)' ou '#RRGGBB' -> QColor."""
    if isinstance(value, QColor):
        return QColor(value)
    value = value.strip()
    if value.startswith("rgba"):
        inner = value[value.index("(") + 1 : value.rindex(")")]
        p = [s.strip() for s in inner.split(",")]
        alpha = int(round(float(p[3]) * 255)) if len(p) > 3 else 255
        return QColor(int(p[0]), int(p[1]), int(p[2]), alpha)
    return QColor(value)
