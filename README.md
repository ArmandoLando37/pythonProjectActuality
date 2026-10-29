# Lecteur d'actualités

Application de bureau en Python permettant de consulter et rechercher des articles d'actualité avec NewsAPI. Elle propose plusieurs catégories, une analyse des articles sous forme de graphiques et l'export des articles en PDF.

## Prérequis

- Windows
- Python 3.12
- [uv](https://docs.astral.sh/uv/)
- Une clé API NewsAPI : https://newsapi.org/

## Installation

Ouvrez PowerShell à la racine du projet, puis créez et activez l'environnement virtuel :

```powershell
uv venv venv --python 3.12
venv\Scripts\activate
```

Installez les dépendances :

```powershell
uv pip install -r requirements.txt
```

## Configuration de NewsAPI

Créez le fichier local `.env` à partir du modèle, puis ajoutez votre clé API :

```powershell
Copy-Item env.exemple .env
```

Ouvrez `.env` et remplacez la valeur de `NEWS_API_KEY` :

```dotenv
NEWS_API_KEY=votre_cle_newsapi
```

Le fichier `.env` est ignoré par Git : ne partagez pas votre clé et ne la commitez pas. Le fichier `env.exemple` sert uniquement de modèle.

## Lancement

Depuis la racine du projet, avec l'environnement virtuel activé :

```powershell
python .\main.py
```

Une connexion Internet et une clé NewsAPI valide sont nécessaires pour charger les actualités.

## Fonctionnalités

- Consultation des actualités par catégorie.
- Recherche d'articles.
- Visualisation de statistiques par source et par date.
- Export des articles affichés au format PDF.

## Structure du projet

```text
.
├── api.py                 # Accès à NewsAPI et traitement des articles
├── analysis.py            # Analyses et graphiques
├── main.py                # Point d'entrée et interface principale
├── pdf_exporter.py        # Export PDF
├── requirements.txt       # Dépendances Python
├── env.exemple            # Modèle de configuration
├── core/                  # Gestionnaires de fonctions de l'application
├── resources/             # Feuille de style et ressources graphiques
└── ui/                    # Composants et fenêtres de l'interface
```
