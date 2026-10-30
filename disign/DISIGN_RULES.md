# DISIGN_RULES.md — Règles de design (inspirées de `disign/006220fd...webp`)

> Guide de design pour l'application **desktop Python / PyQt5**.
> Source d'inspiration : dashboard "fitness" au style **soft-neumorphism / glass**, gris neutres, un seul accent orange-rouge, grandes cartes arrondies, typographie géométrique.
> Ce fichier est la référence unique : tout nouveau widget doit respecter ces règles.

---

## 1. Philosophie

1. **Calme et aéré** : beaucoup d'espace vide, peu d'éléments par zone.
2. **Neutre + un seul accent** : tout est en gris/blanc cassé/anthracite ; l'orange-rouge sert UNIQUEMENT à guider l'œil (action principale, progression, donnée clé).
3. **Tout est arrondi** : aucun angle droit visible (cartes, boutons, champs, barres).
4. **Profondeur douce** : ombres très diffuses et claires, jamais de bordures noires dures.
5. **Hiérarchie par la taille** : un grand titre, des chiffres gros et gras, des libellés petits et gris.
6. **Cohérence** : mêmes rayons, mêmes espacements, mêmes ombres partout.

---

## 2. Design tokens

### 2.1 Couleurs — thème clair (défaut)

| Token | Valeur | Usage |
|---|---|---|
| `bg.app` | `#C9C9C9` → `#DADADA` (dégradé vertical) | Fond derrière la fenêtre principale (si fenêtre flottante) |
| `bg.surface` | `#EFEFEF` | Grand panneau principal |
| `bg.card` | `#F6F6F6` | Cartes de niveau 1 |
| `bg.card.raised` | `#FFFFFF` | Cartes mises en avant, bulles, champs, onglet actif |
| `bg.card.inset` | `#E9E9E9` | Pistes de barres, boutons ronds au repos, zones "enfoncées" |
| `bg.sidebar.top` | `#4B4B4B` | Haut du dégradé de la barre latérale |
| `bg.sidebar.bottom` | `#2F2F2F` | Bas du dégradé de la barre latérale |
| `bg.card.dark.top` | `#5A5A5A` | Carte sombre (ex. "Distance") |
| `bg.card.dark.bottom` | `#3A3A3A` | idem |
| `accent` | `#E8603C` | Action principale, progression, graphiques |
| `accent.hover` | `#F07350` | Survol de l'accent |
| `accent.pressed` | `#CF4F2D` | Clic sur l'accent |
| `accent.soft` | `rgba(232, 96, 60, 0.18)` | Halo/lueur derrière un élément accentué |
| `text.primary` | `#111111` | Titres, chiffres |
| `text.secondary` | `#5F5F5F` | Libellés, sous-titres (≥ 4.5:1 sur cartes/enfoncé) |
| `text.muted` | `#808080` | Placeholder, horodatage, éléments inactifs (≥ 3:1, non essentiel) |
| `text.on-dark` | `#FFFFFF` | Texte sur sidebar / carte sombre |
| `text.on-dark.muted` | `rgba(255,255,255,0.60)` | Texte secondaire sur fond sombre |
| `text.on-accent` | `#FFFFFF` | Texte/icône sur bouton accent |
| `border.subtle` | `rgba(255,255,255,0.65)` | Liseré clair 1 px sur les cartes (effet verre) |
| `shadow` | `rgba(0,0,0,0.10)` | Ombres |
| `chart.track` | `#C9C9C9` | Pistes de graphiques / barres (visibles sur `bg.card`) |
| `chart.bar` | `#111111` | Remplissage de barres / arc d'anneau (≥ 3:1 sur piste) |
| `success` / `warning` / `error` | `#2E8549` / `#B17300` / `#D64545` | États (≥ 3:1 graphique sur carte) |
| `sidebar.rest` | `rgba(255,255,255,0.08)` | Pastille au repos d'un item de navigation |
| `sidebar.hover` | `rgba(255,255,255,0.14)` | Pastille au survol (identique en sombre) |
| `sidebar.cta.bg` | `#FFFFFF` | Bouton CTA sidebar (pill "Actualiser") |
| `sidebar.cta.text` | `#111111` | Texte du CTA |
| `sidebar.cta.hover` | `#F2F2F2` | Survol CTA |
| `sidebar.cta.pressed` | `#E6E6E6` | Clic CTA |

### 2.2 Couleurs — thème sombre (déclinaison pour `theme_manager.py`)

| Token | Valeur |
|---|---|
| `bg.app` | `#121212` → `#1B1B1B` |
| `bg.surface` | `#1E1E1E` |
| `bg.card` | `#262626` |
| `bg.card.raised` | `#2E2E2E` |
| `bg.card.inset` | `#1A1A1A` |
| `bg.sidebar.*` | `#2A2A2A` → `#151515` |
| `accent` | `#F0714D` (légèrement éclairci pour garder le contraste) |
| `text.primary` | `#F2F2F2` |
| `text.secondary` | `#A8A8A8` |
| `text.muted` | `#808080` (≥ 3:1 sur cartes) |
| `shadow` | `rgba(0,0,0,0.45)` |
| `chart.track` | `#505050` (piste visible sur `#262626`) |
| `chart.bar` | `#F2F2F2` |
| `sidebar.rest` / `sidebar.hover` / `sidebar.cta.*` | identiques au clair (surfaces déjà sombres) |

### 2.3 Typographie

- **Famille** : géométrique grotesque, arrondie et moderne. Ordre de préférence :
  `"Space Grotesk"`, `"Plus Jakarta Sans"`, `"Segoe UI Variable"`, `"Segoe UI"`, `sans-serif`.
- Embarquer la police dans `resources/fonts/` et la charger avec `QFontDatabase.addApplicationFont()`.
- Pas de police serif, pas de police monospace sauf pour du code.

| Rôle | Taille | Graisse | Couleur | Exemple |
|---|---|---|---|---|
| `display` | 44–56 px | 500 | `text.primary` | "Let's start strong!" (titre d'accueil) |
| `h1` | 28 px | 600 | `text.primary` | Titre de page |
| `h2` | 20 px | 600 | `text.primary` | Titre de section ("Summary") |
| `h3` | 16 px | 600 | `text.primary` | Titre de carte |
| `stat` | 24–32 px | 700 | `text.primary` | Chiffre clé ("240/600min", "3.4km") |
| `body` | 14 px | 400 | `text.primary` | Texte courant |
| `label` | 12 px | 500 | `text.secondary` | Libellés sous icônes, légendes |
| `caption` | 11 px | 400 | `text.muted` | Horodatage, aide |

Règles :
- Interligne titre `display` : serré (~1.05). Texte courant : ~1.4.
- Les chiffres importants sont **toujours plus gros et plus gras** que leur libellé.
- Jamais plus de **3 tailles différentes** dans une même carte.
- Le texte est aligné à gauche (sauf libellés sous icônes, centrés).

### 2.4 Espacements (échelle de 4 px)

`4 · 8 · 12 · 16 · 20 · 24 · 32 · 48`

| Usage | Valeur |
|---|---|
| Marge interne d'une carte | 20–24 px |
| Espace entre deux cartes | 16–20 px |
| Marge interne du panneau principal | 32 px |
| Espace icône ↔ texte | 12 px |
| Marge de la fenêtre (fond visible autour) | 24–32 px |

### 2.5 Rayons (border-radius)

| Élément | Rayon |
|---|---|
| Fenêtre principale / grand panneau | 32 px |
| Sidebar | 28 px |
| Carte standard | 24 px |
| Petite carte / bulle de chat | 20 px |
| Bouton pill / champ de saisie / onglet | **50 % de la hauteur** (forme pilule) |
| Bouton rond | 50 % (cercle) |
| Barre de progression (piste + remplissage) | 50 % de la hauteur |

> Règle : **un enfant a un rayon ≤ celui de son parent** moins sa marge (rayon concentrique).

### 2.6 Ombres et profondeur

Qt n'a pas de `box-shadow` en QSS → utiliser `QGraphicsDropShadowEffect`.

| Niveau | blurRadius | offset (x, y) | Couleur | Usage |
|---|---|---|---|---|
| `elev-1` | 24 | (0, 6) | `rgba(0,0,0,0.08)` | Cartes standard |
| `elev-2` | 36 | (0, 12) | `rgba(0,0,0,0.12)` | Cartes blanches, bulles, onglet actif |
| `elev-3` | 60 | (0, 24) | `rgba(0,0,0,0.18)` | Fenêtre principale, sidebar |

- Ajouter un **liseré intérieur clair 1 px** (`border.subtle`) sur les cartes pour l'effet "verre".
- Effet "enfoncé" (pistes, boutons ronds au repos) : fond `bg.card.inset`, sans ombre externe.
- **Halo accent** : petit disque flou `accent.soft` derrière le bouton principal ou le badge actif (ex. "AI Chatbot", éclair de la sidebar).

---

## 3. Layout général (desktop)

```
┌──────────────────────────────────────────────────────────────┐
│ marge 24–32 px                                               │
│  ┌─────────┐  ┌──────────────────────────────────────────┐   │
│  │ SIDEBAR │  │ PANNEAU PRINCIPAL (radius 32)            │   │
│  │ 220 px  │  │  ┌──────────────────────┐ ┌───────────┐  │   │
│  │ sombre  │  │  │ Titre + carte objectif│ │ Panneau   │  │   │
│  │         │  │  │ + actions rapides     │ │ latéral   │  │   │
│  │         │  │  └──────────────────────┘ │ (chat/…)  │  │   │
│  │ [CTA]   │  │  Section "Summary" + onglets└───────────┘  │   │
│  │         │  │  [Carte][Carte][Carte sombre]              │   │
│  └─────────┘  └──────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

- **Sidebar** : largeur fixe **220 px**, min 72 px en mode réduit (icônes seules).
- **Panneau principal** : `QStackedWidget` qui change de page via la sidebar.
- **Grille de contenu** : 12 colonnes logiques → `QGridLayout`, colonnes extensibles, `spacing = 20`.
- **Taille minimale de fenêtre** : 1100 × 700 px. Prévoir un comportement correct jusqu'à 1920 × 1080.
- **Zone gauche large (≈ 60 %) + panneau latéral (≈ 40 %)** en haut ; **3 cartes de stats** en bas.
- Le contenu qui dépasse défile **verticalement** dans un `QScrollArea` (barre de défilement fine, voir 4.12).

---

## 4. Composants

### 4.1 Barre latérale (`Sidebar`)

- Fond : dégradé vertical `bg.sidebar.top → bg.sidebar.bottom`, rayon 28, `elev-3`.
- Items de navigation (Dashboard, Progress, Insights, Mood, Stats, Profile, Settings) :
  - Hauteur 44 px, icône dans un **cercle de 32 px** + libellé 13 px à droite.
  - Repos : cercle `rgba(255,255,255,0.08)`, texte `text.on-dark.muted`.
  - **Actif** : cercle rempli (blanc ou accent), texte `text.on-dark` en 600.
  - Survol : cercle `rgba(255,255,255,0.14)`, transition 150 ms.
- Bas de sidebar : **carte promo/CTA** (fond `rgba(255,255,255,0.08)`, radius 20, padding 16) avec titre 15 px blanc, texte 11 px `text.on-dark.muted`, bouton pill blanc "Get Started" (texte noir) et grosse icône éclair accent à moitié coupée dans le coin avec halo.
- Un seul item actif à la fois.

### 4.2 Titre d'accueil (`HeroTitle`)

- Style `display`, sur 2 lignes max, couleur `text.primary`.
- Une phrase courte, motivante (ex. "Bonjour, prêt à lire ?"). Pas de sous-titre long.

### 4.3 Cartes (`Card`)

- Fond `bg.card` (ou `bg.card.raised`), radius 24, padding 20–24, `elev-1`, liseré `border.subtle`.
- Contenu : **un titre court + une donnée principale + éventuellement un visuel**. Pas de tableau dense dans une carte.
- Variante **`CardDark`** : dégradé `bg.card.dark.*`, texte blanc, visuel en trait fin accent (ligne/itinéraire).
- Variante **`CardAccent`** (rare, max 1 par écran) : fond accent, texte blanc.

### 4.4 Boutons

| Type | Forme | Fond | Texte | Usage |
|---|---|---|---|---|
| **Primaire** | Pill, h 44 | `accent` | blanc 600 | Action principale (1 par zone) |
| **Secondaire** | Pill, h 44 | `bg.card.raised` | `text.primary` | Actions secondaires |
| **Fantôme** | Pill, h 36 | transparent | `text.secondary` | Actions discrètes |
| **Rond icône** | Cercle 40–56 px | `bg.card.inset` (repos) / `bg.card.raised` | icône `text.primary` | Actions rapides (Workout, Meal, Water…) |
| **Rond accent** | Cercle 44–52 px | `accent` + halo | icône blanche | Bouton phare d'une carte (éclair) |
| **Sur fond sombre** | Pill, h 36 | blanc | noir 600 | CTA de la sidebar |

États (tous les boutons) :
- `hover` : +6 % de luminosité ou `accent.hover`, curseur main.
- `pressed` : `accent.pressed`, translation de 1 px vers le bas.
- `focus` : anneau 2 px `accent` à 40 % d'opacité (accessibilité clavier).
- `disabled` : opacité 40 %, pas d'ombre, pas de hover.

### 4.5 Actions rapides (`QuickActionBar`)

- Rangée de **5 capsules verticales** (≈ 80 × 120 px, radius 40) fond `bg.card.inset`.
- Dans chaque capsule : cercle blanc 48 px avec icône noire + libellé `label` en dessous.
- Au survol : capsule `bg.card.raised`, légère élévation `elev-1`.

### 4.6 Barre de progression linéaire (`ProgressBar`)

- Piste : hauteur 28–32 px, `chart.track` (clair `#C9C9C9` / sombre `#505050`), radius 50 %.
- Remplissage : `chart.bar` (noir sur clair / blanc sur sombre) — garantit ≥ 3:1 sur la piste ; `accent` réservé à la variante `ProgressAccent` (élément phare).
- Valeur à droite : "**2 340**/8 000" → valeur courante en gras `text.primary`, total en `text.muted`.
- Animation du remplissage : 600 ms, `QEasingCurve.OutCubic`.
- Titre au-dessus : "You're **45%** to your daily goal" → le pourcentage peut être en 600.

### 4.7 Anneau de progression (`RingProgress`)

- Widget **custom** (`paintEvent` avec `QPainter`, antialiasing activé).
- Épaisseur : 8–12 px, extrémités arrondies (`Qt.RoundCap`).
- Piste : `bg.card.inset`. Valeur : `chart.bar` (noir sur clair / blanc sur sombre ; ≥ 3:1 garanti — l'accent en clair ne tient pas 3:1 sur la piste, cf. `tools/check_contrast.py`).
- Petit anneau (≈ 28 px, trait 4 px) dans les mini-cartes ; grand arc (demi-cercle, 2 anneaux concentriques noir + accent) dans les cartes de synthèse.
- Légende : puce ronde de 8 px colorée + libellé `label` + valeur `stat`.

### 4.8 Graphique en barres (`BarChart`)

- **Barres fines verticales** (largeur ≈ 8–10 px), espacées régulièrement, coins arrondis.
- Toutes les barres existent en **gris de piste** (`chart.track`, hauteur max = piste) ; les barres avec valeur sont **remplies en `chart.bar`** (noir sur clair / blanc sur sombre) à leur hauteur réelle.
- Aucun axe, aucun quadrillage, aucune bordure. Libellé + valeur à gauche ("Steps / 2.340").
- Avec `matplotlib` : fond transparent, `spines` masqués, `ax.axis('off')`, `bar(width=0.5)`, couleurs ci-dessus. Préférer le rendu `QPainter` pour les petites cartes (plus net et plus léger).
- Mettre en avant une barre (max/sélection) en `accent` — intention décorative de la charte, le remplissage informatif reste `chart.bar` (≥ 3:1).

### 4.9 Contrôle segmenté / onglets (`SegmentedControl`)

- Conteneur pill `bg.card.inset`, h 40, padding 4.
- Segment actif : pill `bg.card.raised`, texte `text.primary` 600, `elev-2`.
- Segments inactifs : texte `text.muted`.
- Animation du "slider" blanc qui glisse vers le segment choisi (200 ms, `OutCubic`).
- Usage : Daily / Weekly / Monthly, ou toute bascule à 2–4 choix.

### 4.10 Panneau de chat / assistant (`ChatPanel`)

- Grande carte `bg.card` radius 28 avec **badge pill accent** centré en haut (icône + "AI Chatbot"), halo `accent.soft`.
- **Bulle utilisateur** : alignée à droite, fond `bg.card.inset`, texte `text.primary`, radius 20 (coin bas-droit réduit à 6).
- **Bulle assistant** : alignée à gauche, fond `bg.card.raised`, `elev-1`, radius 20 (coin bas-gauche réduit à 6).
- Horodatage `caption` sous la bulle ("2 hours ago").
- **Mini-cartes de résultat** dans la conversation : pill blanche avec libellé, valeur en gras et petit anneau à droite.
- **Champ de saisie** : pill blanche h 48, placeholder `text.muted` ("Type something…"), bouton micro/envoi rond à droite.

### 4.11 Champs de formulaire

- `QLineEdit` / `QComboBox` / `QSpinBox` : fond `bg.card.raised`, radius pill (h 44), padding horizontal 16, pas de bordure.
- `focus` : anneau 2 px `accent`.
- Erreur : texte `error` sous le champ (12 px), anneau `error`.

### 4.12 Barres de défilement

- Fines (8 px), piste transparente, poignée `rgba(0,0,0,0.18)` radius 4, `hover` → `0.30`.
- Pas de flèches.

### 4.13 Infobulles, menus, dialogues

- Fond `bg.card.raised`, radius 16, `elev-2`, texte `text.primary` 13 px, padding 8–12.
- Dialogues : même style que les cartes, radius 28, bouton primaire à droite, bouton secondaire à gauche.
- Overlay modal : `rgba(0,0,0,0.25)`.

---

## 5. Iconographie

- **Style** : trait (outline) **1.75 px**, extrémités arrondies, coins arrondis, 24 × 24 px (grille de 24).
- Format **SVG** dans `resources/icons/`, chargés via `QIcon` / `QSvgRenderer` (module `QtSvg` disponible).
- Couleur : suivre le thème (`text.primary` sur clair, `text.on-dark` sur sombre, blanc sur accent). Recolorer via `currentColor` ou en repeignant le `QPixmap`.
- Toujours placées dans un **conteneur circulaire** quand elles sont cliquables.
- Jeu d'icônes conseillé : Lucide / Phosphor (licence libre). Ne pas mélanger plusieurs familles.

---

## 6. Interaction et animation

| Élément | Durée | Courbe |
|---|---|---|
| Survol (couleur, élévation) | 120–150 ms | `OutQuad` |
| Pression de bouton | 80 ms | `OutQuad` |
| Changement de page (fondu) | 200–250 ms | `InOutQuad` |
| Remplissage de progression / anneau | 600–800 ms | `OutCubic` |
| Slider du contrôle segmenté | 200 ms | `OutCubic` |

- Utiliser `QPropertyAnimation` / `QVariantAnimation`. Aucune animation > 800 ms.
- Respecter la réduction des animations si l'option système est activée (désactiver les transitions longues).
- Jamais d'animation qui bloque l'interface (pas de `time.sleep` dans le thread UI → `QThread`/`QRunnable` pour `api.py`, `analysis.py`, `pdf_exporter.py`).

---

## 7. Accessibilité

- **Contraste** : audité par `tools/check_contrast.py` (tokens × seuils WCAG, 0 échec bloquant). Repères clés : `text.primary` sur `bg.card` ≈ 17:1 ✔ ; `text.secondary` sur cartes/enfoncé ≥ 5.2:1 ✔ ; `chart.bar` sur `chart.track` ≥ 7:1 ✔.
- ⚠️ `accent` (`#E8603C`) sur fond clair ≈ 3.4:1 → **réservé aux éléments graphiques et textes ≥ 18 px/gras**. Ne jamais l'utiliser pour du petit texte courant.
- Texte blanc sur `accent` : uniquement en 14 px gras minimum.
- Cible de clic **≥ 40 × 40 px**.
- Navigation clavier complète (`Tab`, `Entrée`, `Espace`), `setFocusPolicy` et anneau de focus visibles.
- Renseigner `setAccessibleName()` sur les boutons icône.
- Ne jamais transmettre une information **uniquement par la couleur** (ajouter icône/texte).

---

## 8. Implémentation PyQt5

### 8.1 Où mettre quoi (adapté à l'arborescence du projet)

```
core/theme_manager.py     → tokens (dict clair/sombre), génération du QSS, bascule de thème, ombres
resources/style.css       → QSS template avec placeholders {token}  (voir 8.2)
resources/fonts/          → polices embarquées
resources/icons/          → icônes SVG
ui/components.py          → widgets réutilisables : Card, CardDark, PillButton, RoundButton,
                            SegmentedControl, ProgressBar, RingProgress, BarChart, ChatBubble, Sidebar
ui/article_detail.py      → écrans qui n'utilisent QUE les composants ci-dessus
main.py                   → QApplication, chargement polices + thème, fenêtre principale
```

### 8.2 QSS : pas de variables → utiliser des placeholders

Qt Style Sheets **ne supportent pas** `var(--x)`. Écrire `style.css` avec des `{placeholders}` et les remplacer au chargement :

```css
/* resources/style.css */
QWidget { font-family: {font.family}; color: {text.primary}; font-size: 14px; }

#MainPanel { background: {bg.surface}; border-radius: 32px; }

QFrame#Card { background: {bg.card}; border-radius: 24px;
              border: 1px solid {border.subtle}; }

QPushButton#Primary { background: {accent}; color: {text.on-accent};
                      border: none; border-radius: 22px; min-height: 44px;
                      padding: 0 24px; font-weight: 600; }
QPushButton#Primary:hover   { background: {accent.hover}; }
QPushButton#Primary:pressed { background: {accent.pressed}; }
QPushButton#Primary:focus   { outline: none; border: 2px solid {accent.soft}; }

QLineEdit { background: {bg.card.raised}; border: none; border-radius: 22px;
            min-height: 44px; padding: 0 16px; }
QLineEdit:focus { border: 2px solid {accent}; }
```

```python
# core/theme_manager.py (principe)
TOKENS = {
    "light": {"bg.surface": "#EFEFEF", "bg.card": "#F6F6F6", "accent": "#E8603C", ...},
    "dark":  {"bg.surface": "#1E1E1E", "bg.card": "#262626", "accent": "#F0714D", ...},
}

def build_qss(theme: str, template: str) -> str:
    qss = template
    for key, value in TOKENS[theme].items():
        qss = qss.replace("{" + key + "}", value)
    return qss
```

> ⚠️ Attention : les accolades CSS `{ }` du QSS et les placeholders `{token}` coexistent. Utiliser un séparateur distinct (ex. `@token@`) ou `string.Template` (`$token`) pour éviter les conflits avec `str.format`.

### 8.3 Ombres

```python
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

def apply_shadow(widget, blur=24, dy=6, alpha=20):
    fx = QGraphicsDropShadowEffect(widget)
    fx.setBlurRadius(blur)
    fx.setOffset(0, dy)
    fx.setColor(QColor(0, 0, 0, alpha))
    widget.setGraphicsEffect(fx)
```

- Un seul `QGraphicsEffect` par widget. **Ne pas mettre d'ombre sur des dizaines de petits widgets** (coût de rendu) : ombrer les conteneurs (cartes), pas leurs enfants.
- Laisser de la marge autour du widget ombré (sinon l'ombre est coupée par le layout).

### 8.4 Fenêtre arrondie / flottante (optionnel, fidèle à l'image)

```python
self.setWindowFlags(Qt.FramelessWindowHint)
self.setAttribute(Qt.WA_TranslucentBackground)
# Le QWidget racine peint le fond dégradé ; le panneau principal a radius 32.
```

- Si `FramelessWindowHint` est utilisé : fournir **barre de titre personnalisée** (déplacement, réduire, agrandir, fermer) et zone de redimensionnement. Sinon garder le cadre natif (plus simple, plus sûr).

### 8.5 Widgets custom (dessin)

- Toujours : `painter.setRenderHint(QPainter.Antialiasing)`.
- `RingProgress` : `QPen(color, width, Qt.SolidLine, Qt.RoundCap)` + `drawArc(rect, startAngle*16, spanAngle*16)`.
- Définir `sizeHint()` / `minimumSizeHint()` pour que les layouts fonctionnent.
- Exposer les valeurs animables via `pyqtProperty` pour `QPropertyAnimation`.

### 8.6 Résolution / DPI

Avant la création de `QApplication` :

```python
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
```

- Exprimer les tailles en px logiques ; utiliser les SVG pour des icônes nettes à toutes les échelles.

### 8.7 Performance

- Pas de calcul lourd / appel réseau dans le thread UI (`api.py`, `analysis.py`, `pdf_exporter.py` → workers `QThread`).
- Listes d'articles longues : `QListView` + modèle/délégué (pas des centaines de `QWidget`).
- Mettre en cache les `QPixmap` d'icônes recolorées.

---

## 9. Adaptation au projet (articles / favoris / analyse / export PDF)

| Écran / fonction | Composants du design |
|---|---|
| Accueil (`Dashboard`) | `HeroTitle` + carte "objectif" (`ProgressBar` : ex. articles lus / objectif) + `QuickActionBar` (Rechercher, Favoris, Exporter, Analyser, Thème) |
| Liste d'articles | `Card` par article (titre `h3`, source `label`, date `caption`, bouton rond ★ pour `favorites_manager`) |
| Détail (`article_detail.py`) | Grande `Card` blanche, titre `h1`, corps `body` (interligne 1.5, largeur de texte ≤ 720 px), actions en pills |
| Favoris | Même liste, bouton ★ rempli `accent` |
| Analyse (`analysis.py`) | Section "Summary" : `SegmentedControl` (Jour/Semaine/Mois) + `RingProgress` + `BarChart` + `CardDark` (chiffre clé) |
| Export (`export_manager.py`, `pdf_exporter.py`) | Bouton primaire "Exporter en PDF" + `ProgressBar` pendant la génération |
| Assistant / recherche | `ChatPanel` si une fonction IA est ajoutée |
| Paramètres / thème (`theme_manager.py`) | Bascule clair/sombre en `SegmentedControl` |

- **Graphiques `matplotlib`** (présent dans le venv) : rendre sobres → fond transparent, pas de cadre, palette = noir + gris + `accent`, police identique à l'app.
- **Export PDF** : réutiliser les mêmes tokens (titre `h1`, accent pour les mises en avant, marges généreuses) pour que le PDF ressemble à l'app.

---

## 10. À faire / À ne pas faire

### ✅ À faire
- Réutiliser les composants de `ui/components.py` avant d'en créer un nouveau.
- Lire les couleurs/rayons/espacements **depuis les tokens** (jamais de valeur en dur dans un écran).
- Limiter l'accent à **1–2 éléments par écran**.
- Laisser respirer : si une carte est chargée, la scinder en deux.
- Tester en clair **et** en sombre, et à 100 % / 125 % / 150 % de mise à l'échelle Windows.

### ❌ À ne pas faire
- Angles droits, bordures noires épaisses, ombres dures ou colorées.
- Plus d'une couleur d'accent, dégradés criards, couleurs saturées en fond.
- Texte gris clair sur fond blanc cassé (contraste insuffisant).
- Mélange de familles d'icônes ou de polices.
- Tableaux denses / formulaires à 15 champs sur un seul écran.
- Valeurs de style codées dans les fichiers d'écran (`setStyleSheet("color:#123456")`).
- Ombres sur tous les widgets enfants.

---

## 11. Checklist avant de valider un écran

- [ ] Tous les rayons viennent de l'échelle (32 / 28 / 24 / 20 / pill).
- [ ] Espacements multiples de 4 px.
- [ ] Une seule action primaire accentuée par zone.
- [ ] Hiérarchie claire : 1 titre, chiffres gros/gras, libellés petits/gris.
- [ ] États `hover` / `pressed` / `focus` / `disabled` présents.
- [ ] Contrastes vérifiés (section 7).
- [ ] Rendu correct en thème clair et sombre.
- [ ] Aucun gel de l'interface pendant les opérations longues.
- [ ] Redimensionnement de la fenêtre sans élément coupé.
