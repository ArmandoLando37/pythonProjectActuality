# -*- coding: utf-8 -*-
"""Audit de contraste WCAG des tokens de couleurs (ThemeManager).

Usage : python tools/check_contrast.py
Ce script n'est PAS importé par l'application : il relie les paires de
tokens à un seuil WCAG et affiche un tableau lisible.

Règles appliquées (cf. disign/DISIGN_RULES.md §7) :
- texte courant essentiel : ratio >= 4.5:1 (WCAG AA) ;
- textes/adonf non essentiels (dates, placeholders) : >= 3:1 ;
- éléments graphiques utiles : >= 3:1 (WCAG 1.4.11) ;
- pures décorations (pistes, ombres) : rapport >= 1.5 visuel, signalé DEC ;
- exceptions « charte » : texte blanc sur accent (gras >= 14 px) et
  barre max accent (§4.8) : signalées CHA sans échec bloquant.
"""

import os
import sys

from PyQt5.QtGui import QColor

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.theme_manager import ThemeManager, parse_color

TEXTE_COURANT = 4.5
TEXTE_SECOND = 4.5
NON_ESSENTIEL = 3.0
GRAPHIQUE = 3.0
DECORATIF = 1.5

# (libellé, fg, bg, seuil, nature, usage)
PAIRS = [
    ("P1", "text.primary", "bg.card", TEXTE_COURANT, "C", "Titres sur carte"),
    ("P2", "text.primary", "bg.surface", TEXTE_COURANT, "C",
     "Texte courant sur panneau"),
    ("P3", "text.primary", "bg.card.raised", TEXTE_COURANT, "C",
     "Titres sur carte blanche"),
    ("P4", "text.primary", "bg.card.inset", TEXTE_COURANT, "C",
     "Texte dans zone enfoncée"),
    ("S1", "text.secondary", "bg.card", TEXTE_SECOND, "C",
     "Libellés sources sur carte"),
    ("S2", "text.secondary", "bg.card.raised", TEXTE_SECOND, "C",
     "Libellés sur carte blanche"),
    ("S3", "text.secondary", "bg.card.inset", TEXTE_SECOND, "C",
     "Texte dans zone enfoncée"),
    ("S4", "text.secondary", "bg.surface", TEXTE_SECOND, "C",
     "Sous-titres sur panneau"),
    ("M1", "text.muted", "bg.card", NON_ESSENTIEL, "C",
     "Dates / caption (non essentiel)"),
    ("M2", "text.muted", "bg.card.raised", NON_ESSENTIEL, "C",
     "Caption sur carte blanche"),
    ("M3", "text.muted", "bg.card.inset", NON_ESSENTIEL, "C",
     "Placeholder image / champs"),
    ("D1", "text.on-dark", "bg.sidebar.top", TEXTE_COURANT, "C",
     "Navigation sur sidebar"),
    ("D2", "text.on-dark", "bg.card.dark.top", TEXTE_COURANT, "C",
     "Chiffre clé carte sombre"),
    ("D3", "text.on-dark.muted", "bg.sidebar.top", NON_ESSENTIEL, "C",
     "Sous-titres sidebar (rgba applati)"),
    ("D4", "text.on-dark.muted", "bg.card.dark.top", NON_ESSENTIEL, "C",
     "Méta carte sombre (rgba applati)"),
    ("SB1", "text.on-dark", "bg.sidebar.bottom", TEXTE_COURANT, "C",
     "Navigation bas sidebar"),
    ("CT1", "sidebar.cta.text", "sidebar.cta.bg", TEXTE_COURANT, "C",
     "Texte bouton CTA"),
    ("A1", "text.on-accent", "accent", GRAPHIQUE, "CHA",
     "Texte blanc sur accent (gras >= 14 px, charte)"),
    ("A2", "accent", "bg.card", GRAPHIQUE, "CHA",
     "Liseré / coche accent sur carte"),
    ("A3", "accent", "bg.card.raised", GRAPHIQUE, "CHA",
     "Bouton accent sur carte blanche"),
    ("A4", "accent", "chart.track", GRAPHIQUE, "CHA",
     "Barre max accent sur piste (charte §4.8)"),
    ("G1", "chart.bar", "chart.track", GRAPHIQUE, "C",
     "Barres / remplissage sur piste"),
    ("G2", "chart.track", "bg.card", DECORATIF, "DEC",
     "Piste visible sur carte (décoratif)"),
    ("R1", "chart.bar", "bg.card.inset", GRAPHIQUE, "C",
     "Arc anneau sur piste inset"),
    ("E1", "error", "bg.card", GRAPHIQUE, "C", "Erreur graphique sur carte"),
    ("W1", "warning", "bg.card", GRAPHIQUE, "C", "Avertissement sur carte"),
    ("K1", "success", "bg.card", GRAPHIQUE, "C", "Succès graphique sur carte"),
]


def _blend(fg, bg):
    """Applique l'alpha d'un rgba semi-transparent sur une couleur pleine."""
    fg = parse_color(fg)
    bg = parse_color(bg)
    if fg.alpha() == 255:
        return fg
    a = fg.alphaF()
    return QColor(int(fg.red() * a + bg.red() * (1 - a)),
                  int(fg.green() * a + bg.green() * (1 - a)),
                  int(fg.blue() * a + bg.blue() * (1 - a)))


def _luminance(color):
    rgb = [max(0.0, min(1.0, c / 255.0)) for c in
           (color.red(), color.green(), color.blue())]
    lin = [0.01298 * c * 12.92 if c <= 0.04045
           else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def _ratio(fg, bg):
    l1, l2 = sorted((_luminance(fg), _luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def _color_for(name, theme):
    """Token brut par nom (les rgba sont aplaties plus loin)."""
    return ThemeManager.TOKENS[theme][name]


def main() -> int:
    ko_total = 0
    for theme in ("light", "dark"):
        tokens = ThemeManager.TOKENS[theme]
        print("=" * 96)
        print(f"THEME {theme.upper()}")
        print("=" * 96)
        header = (f"{'ID':<4}{'Premier':<26}{'Fond':<22}{'Ratio':>8}"
                  f"  {'Seuil':>6}  {'Etat':<6}  Usage")
        print(header)
        print("-" * 96)
        for pid, fg_name, bg_name, threshold, nature, usage in PAIRS:
            bg_color = parse_color(tokens[bg_name])
            fg_color = parse_color(_color_for(fg_name, theme))
            if fg_color.alpha() < 255:
                fg_color = _blend(fg_color, bg_color)
            ratio = _ratio(fg_color, bg_color)
            if nature == "DEC":
                ok = ratio >= DECORATIF
                state = "OK" if ok else "KO"
            elif nature == "CHA":
                state = "CHA" if ratio >= 3.0 else "CHA*"
            else:
                ok = ratio >= threshold
                state = "OK" if ok else "KO"
                if not ok:
                    ko_total += 1
            print(f"{pid:<4}{fg_name:<26}{bg_name:<22}{ratio:>8.2f}"
                  f"  {threshold:>6.2f}  {state:<6}  {usage}")
        print()
    print("-" * 96)
    print(f"Resultat : {ko_total} echec(s) bloquant(s) "
          f"(CHA = exception charte documentee, NON bloquant).")
    return 0 if not ko_total else 1


if __name__ == "__main__":
    sys.exit(main())
