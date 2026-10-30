# AGENTS.md — Aide au démarrage pour IA

Ce document permet à une IA (ou un nouveau développeur) de comprendre rapidement
le projet, ses conventions et ses pièges. Il décrit l'état réel du dépôt.

---

## 1. C'est quoi ce projet ?

Application de bureau Windows **Python 3.12 + PyQt5** : lecteur d'actualités
(~« Lecteur d'actualités ») connecté à **NewsAPI**.

Fonctions principales :
- Récupérer des articles d'actualité (top headlines ou recherche par mot-clé)
- Consulter le détail d'un article
- Marquer des articles en favoris (persistés localement)
- Analyser les articles (statistiques, graphiques natifs)
- Exporter les articles en **PDF** (police embarquée + signature) et **CSV/XLSX**

---

## 2. Commandes utiles

```powershell
# Lancer l'application (venv à la racine, Python 3.12, créé avec uv)
python .\main.py

# Vérifier la syntaxe de tout le code
python -m compileall -q main.py api.py analysis.py pdf_exporter.py core ui

# Test sans écran (CI / vérification IA) — instancie l'UI complète sans crash
$env:QT_QPA_PLATFORM='offscreen'
python -X utf8 -c "from PyQt5.QtWidgets import QApplication; import main;
from core.theme_manager import ThemeManager; from ui import components as c;
app=QApplication([]); tm=ThemeManager(); c.init_fonts(tm); tm.apply_theme(app);
w=main.MainWindow(); print('OK')"
```

---

## 3. Structure du dépôt

```
main.py                  Point d'entrée : QApplication (High-DPI), MainWindow
                         (sidebar + panneau principal), threads d'arrière-plan
api.py                   NewsAPIClient : appels NewsAPI (top-headlines/search),
                         extraction de la clé API (env -> news_api_key.txt)
analysis.py              DataAnalyzer : calculs purs (by_day, by_source, stats)
                         + export CSV. AUCUN rendu graphique ici.
pdf_exporter.py          PDFExporter : PDF stylé (charte graphique) via reportlab
                         avec signature paramétrable (variable PDF_SIGNATURE)
core/
  theme_manager.py       ThemeManager : tokens de couleurs clair/sombre,
                         génération QSS, ombres portées, bascule/persistance
  about_info.py          load_about_info() : fiche « À propos » lue depuis le
                         .env (DEV_*, APP_REPO_URL), URLs validées http(s)
  favorites_manager.py   FavoritesManager : favoris persistés en favorites.json
  selection.py           ArticleSelection : sélection multi-articles partagée
                         par les pages Articles/Favoris ; clé stable =
                         URL sinon « titre | source » ; signal changed
  export_manager.py      ExportManager : export XLSX/CSV (openpyxl importé
                         PARESSEUSEMENT — la dépendance peut être absente)
  __init__.py            (silencieux, ne rien y ajouter qui imprime)
ui/
  components.py          Bibliothèque de composants (voir §5) — toutWidget
                         peint doit implémenter refresh_theme()
  pages.py               Builders des 5 pages : build_home, build_articles,
                         build_favorites, build_analysis, build_about(window)
  article_detail.py      ArticleDetailDialog : fiche détaillée d'un article
                         + signal export_requested(dict) — l'export est
                         centralisé dans MainWindow (jamais de QFileDialog
                         ailleurs)
tools/
  check_contrast.py      Audit WCAG des tokens (ThemeManager importé) :
                         tableau paires/seuils/ratios ; exit 0 = zéro échec
                         bloquant. PAS importé par l'application.
tests/
  test_selection.py      Tests auto-exécutables du modèle ArticleSelection
resources/
  fonts/                 Space Grotesk (5 graisses), chargées par init_fonts()
  icons/                 17 icônes SVG (Lucide, stroke=currentColor)
  style.css              Feuille de style QSS en TEMPLATE string.Template
disign/DISIGN_RULES.md   REGLE ABSOLUE : charte graphique du projet
env.exemple              Modèle de .env (NEWS_API_KEY, PDF_SIGNATURE)
architecture.md          Inventaire brute généré (ancien, pas une doc fiable)
```

---

## 4. Flux de données

```
MainWindow (main.py)
  |-- FetchArticlesThread (QThread) --> NewsAPIClient --> liste de dicts
  |        signal articles_ready -> window.set_articles(articles)
  |-- pages de ui/pages.py : accueil | articles | favoris | analyse | à propos
  |-- MainWindow._navigate(key) construit/ré-affiche la page + refresh_analysis
  |        ensure_articles_loaded() : le flux se charge la 1re fois qu'on
  |        ouvre la page Articles (drapeau _is_loading + séquence _fetch_seq
  |        qui rejette les réponses périmées)
  |-- ExportThread (QThread) --> PDFExporter.export_to_pdf(articles, chemin)
  |        tout passe par window.export_articles_to_pdf(articles, nom) ;
  |        sortie AUTO : pdf/<jj-mm-aaaa>/<nom>_<AAAAMMJJ_HHMMSS>.pdf
  |        (dossier créé au vol ; regroupement par date seule) ; un seul
  |        export à la fois (_export_running)
  |-- ArticleSelection (core) : coches multi-articles, signal changed,
  |        prune_to(flux, favoris) après chaque rafraîchissement
  |-- FavoritesManager (core) --★ sur ArticleCard
  x  ThemeManager fournit le thème à TOUS les widgets
```

### Schéma d'un article (dict, utilisé partout)

```python
{
  "title": str,            # jamais None
  "description": str,      # "Aucune description disponible" si vide
  "url": str,
  "image_url": str|"",     # vide -> ImageLabel affiche un placeholder
  "source": str,
  "published_at": str,     # déjà formaté en fr par api.py
  "author": str,
  "content": str,          # optionnel
}
```

---

## 5. Système de design (obligatoire)

Référence unique : **`disign/DISIGN_RULES.md`** (§ numérotés).

- **Tokens** : `ThemeManager.TOKENS["light"|"dark"]` dictionnaires ; accent
  unique `#E8603C` (clair) / `#F0714D` (sombre) — jamais une autre couleur vive.
- **QSS** : `resources/style.css` est un template `string.Template` lu par
  `build_qss()`. Les clés ne contiennent NI point NI tiret
  (ex : `text.on-dark` -> `$text_on_dark`, car `${foo.bar}` est invalide).
- **PIEGE** : tout commentaire dans style.css ne doit JAMAIS contenir un
  `$` suivi d'un mot (substitution KeyError). Idem pour `$underscore`.
- **Graisses** : Qt5 utilise une échelle 0-99 (PAS les équivalents Qt6) :
  Regular=50, Medium=57, DemiBold=63, Bold=75 (`role_font()` en dépend).
- **Police** : famille exacte « Space Grotesk » ; `init_fonts()` doit être
  appelée avant toute création de widget qui titre des rôles.
- **Ombres** : `apply_shadow(widget, n)` niveaux 1-3 (QGraphicsDropShadowEffect).
- **Thème appliqué** : `tm.switch_theme("light"|"dark")` + pour tout widget
  qui peint lui-même (RoundButton, SegmentedControl, charts...) implémenter
  `refresh_theme()` et l'enregistrer dans le registre `_themable` de MainWindow.
- **Rayons** : fenêtre 32, cartes 24, primary pill 26 (pill), images 20 min.
- Composants réutilisables : voir signatures de `ui/components.py`
  (Card, HeroTitle, RoundButton, SidebarWidget, QuickAction(Bar),
  SegmentedControl, TokenProgressBar, RingProgress, BarChartWidget,
  ArticleCard, SearchBar, ImageLabel async).

---

## 6. Règles de fiabilité (ne pas casser)

1. **Aucune opération lente sur le thread UI** : réseau = `FetchArticlesThread`,
   export PDF = `ExportThread`, images = `QThreadPool` (`ImageLabel`).
   L'analyse reste en calculs purs (rapide).
2. **openpyxl** : importé seulement à l'intérieur des méthodes de
   `ExportManager` (la dépendance peut être absente du venv).
3. **BarChartWidget.paintEvent** : bornes entières strictes (dimensions
   ≥ 10 px, radius ≥ 1, clamp 0-1). Un float non borné a déjà causé un crash
   natif Qt (0xC0000409). Garder les garde-fous.
4. **Pas de `font-size` global dans le QSS** : il écrase les `QFont` définis
   par `role_font`. Les tailles viennent des QFont, pas du QSS.
5. High-DPI : attributs Qt placés AVANT la création de `QApplication` (§8.6).
6. **PDFExporter** : enregistre 3 graisses Space Grotesk via TTFont ; si le
   chemin des fonts change, mettre à jour `FONT_FILES`. La signature est
   échappée HTML puis centrée (TA_CENTER) — le wrap évite tout débordement.
7. **Chargement du flux** : un seul à la fois (`_is_loading`), réponses
   périmées ignorées (`_fetch_seq`) ; les données déjà affichées ne sont
   JAMAIS effacées par une erreur ; ordre = notification, puis refresh.
8. **Sélection multi-articles** : toute coche passe par
   `ArticleSelection` (clé = URL sinon « titre | source ») et est
   `prune_to(flux, favoris)` après chaque rafraîchissement.
9. **Export PDF** : unique porte = `MainWindow.export_articles_to_pdf`
   (ExportThread) ; sortie automatique `pdf/<jj-mm-aaaa>/` (date seule,
   heure ignorée pour le regroupement, dossier créé au vol) ; le détail
   de l'article passe par le signal `export_requested(dict)` de
   `ArticleDetailDialog` ; un seul export à la fois (`_export_running`).

---

## 7. Environnement & fichiers runtime

Variables (chargées par `python-dotenv`, cf. `.env` à la racine, jamais
commité ; modèle dans `env.exemple`) :

| Variable         | Rôle                                                        |
|------------------|-------------------------------------------------------------|
| `NEWS_API_KEY`   | Clé NewsAPI (fallback : fichier `news_api_key.txt`)         |
| `PDF_SIGNATURE`  | Signature en bas des PDF, défaut `Armando Lando - bandy mlay` |
| `DEV_NAME`       | Page « À propos » : nom du développeur (défaut `Développeur`) |
| `DEV_ROLE`       | Rôle affiché                                                |
| `DEV_BIO`        | Bio affichée                                                |
| `DEV_EMAIL`      | Bouton e-mail (mailto) si renseigné                         |
| `DEV_PORTFOLIO_URL` | Bouton Portfolio — http(s) uniquement, sinon ignoré      |
| `DEV_GITHUB_URL` | Bouton GitHub — http(s) uniquement                          |
| `DEV_LINKEDIN_URL`| Bouton LinkedIn — http(s) uniquement                       |
| `APP_REPO_URL`   | Dépôt : active « Code source » / « Signaler un bug »        |

Fichiers runtime (générés, ignorés par git, ne pas committer) :
- `ui_prefs.json` : dernier thème utilisé (light/dark)
- `favorites.json` : favoris de l'utilisateur
- `news_api_key.txt` : clé API en fallback
- `pdf/<jj-mm-aaaa>/<nom>_<AAAAMMJJ_HHMMSS>.pdf` : exports regroupés
  par jour (date seule ; l'heure du nom est ignorée au regroupement)

---

## 8. Conventions de code

- Python 3.12, PyQt5 uniquement (PAS de PyQt6 — échelle des poids etc.).
- Docstrings en français, commentaires en français.
- Nommage : classes PascalCase, fonctions snake_case ; widgets stylés via
  `objectName` (écho aux identifiants du QSS : `Card`, `Primary`, `Ghost`...).
- Aucun print industriel dans les modules GUI (le `statusBar` natif sert de
  feedback utilisateur).
- Les messages d'erreur API et les exceptions sont gérés dans `api.py`
  (raise) puis traduits en messages UI dans `main.py`.
- Les états vides (aucun article / aucun favori) ont TOUJOURS un empty-state
  dans la page (cf. `_empty_state` de `ui/pages.py`).

---

## 9. Ce qu'une IA NE DOIT PAS faire

- Commiter `ui_prefs.json`, `favorites.json`, `.env`, `news_api_key.txt`,
  les PDF générés ou les codes API réels.
- Réintroduire matplotlib dans l'UI (le rendu natif QPainter est plus rapide
  et stable).
- Ajouter une 2e couleur vive d'accent (violon de la charte §3).
- Utiliser des ponds Qt6 (0-7) au lieu de l'échelle Qt5 (0-99).
- Modifier `resources/style.css` sans vérifier que le template
  `string.Template` s'y substitue bien (voir les pièges du §5).
- Modifier main.py sans relancer le smoke test offscreen (§2) : un crash natif
  (exit -1073741819) peut apparaître même si le code compile.
