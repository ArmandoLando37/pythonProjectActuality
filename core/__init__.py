"""
Package core - Modules de fonctionnalités principales de l'application Lecteur d'Actualités

Ce package contient :
- FavoritesManager : Gestion des articles favoris
- ThemeManager : Gestion des thèmes d'interface
- ExportManager : Fonctionnalités d'exportation des données
"""

from .favorites_manager import FavoritesManager
from .theme_manager import ThemeManager
from .export_manager import ExportManager

# Version du package
__version__ = "1.0.0"
__author__ = "Votre Nom"
__description__ = "Modules de base pour l'application Lecteur d'Actualités"

# Liste des modules exportés
__all__ = [
    'FavoritesManager',
    'ThemeManager', 
    'ExportManager'
]

# Initialisation du package (sans sortie console)
