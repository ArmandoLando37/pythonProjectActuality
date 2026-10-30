# -*- coding: utf-8 -*-
"""Informations « À propos » lues depuis le fichier .env (python-dotenv).

Les valeurs (nom, rôle, bio, liens du développeur, dépôt) sont modifiables
sans toucher au code. Ce module n'affiche rien et n'imprime rien.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

APP_NAME = "Actus"
APP_TAGLINE = "Lecteur d'actualités"
APP_VERSION = "1.0.0"

DEFAULT_DEV_NAME = "Développeur"


def _clean_text(value):
    """Texte quelconque : débarrassé des espaces parasites."""
    return (value or "").strip()


def _clean_url(value):
    """URL utilisable : http(s) uniquement, sinon chaîne vide."""
    value = _clean_text(value)
    if value.startswith(("http://", "https://")):
        return value
    return ""


@dataclass(frozen=True)
class AboutInfo:
    """Fiche développeur / projet affichée sur la page « À propos »."""

    name: str
    role: str
    bio: str
    email: str
    portfolio: str
    github: str
    linkedin: str
    repo: str

    @property
    def issues(self):
        """Lien pour rapporter un bug (dépend du dépôt)."""
        return f"{self.repo}/issues" if self.repo else ""


def load_about_info():
    """Lit les variables DEV_* / APP_REPO_URL et retourne une AboutInfo."""
    load_dotenv()

    name = _clean_text(os.getenv("DEV_NAME")) or DEFAULT_DEV_NAME
    return AboutInfo(
        name=name,
        role=_clean_text(os.getenv("DEV_ROLE")),
        bio=_clean_text(os.getenv("DEV_BIO")),
        email=_clean_text(os.getenv("DEV_EMAIL")),
        portfolio=_clean_url(os.getenv("DEV_PORTFOLIO_URL")),
        github=_clean_url(os.getenv("DEV_GITHUB_URL")),
        linkedin=_clean_url(os.getenv("DEV_LINKEDIN_URL")),
        repo=_clean_url(os.getenv("APP_REPO_URL")),
    )
