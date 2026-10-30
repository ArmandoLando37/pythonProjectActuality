# -*- coding: utf-8 -*-
"""Sélection multiple d'articles (étape 3 de la tâche d'export PDF).

Modèle pur (pas de widget ici) : stocke une liste de clés stables et
l'article correspondant. La clé stable est l'URL de l'article ; quand
elle est absente on retombe sur « titre | source » (deux articles sans
URL mais de titres/sources identiques partagent alors une sélection,
compromis assumé faute d'identifiant plus fiable dans le dict article).
"""

from PyQt5.QtCore import QObject, pyqtSignal


def article_key(article):
    """Clé stable d'un article : URL sinon « titre | source »."""
    url = (article.get("url") or "").strip()
    if url:
        return url
    title = (article.get("title") or "").strip()
    source = (article.get("source") or "").strip()
    return title + "|" + source


class ArticleSelection(QObject):
    """Ensemble de clés sélectionnées + registre article par clé.

    Signal `changed` émis après toute modification de la sélection afin
    que MainWindow mette à jour barres et compteurs.
    """

    changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._articles = {}  # clé -> article (ordre d'insertion stable)

    # ------------------------------------------------------------ mutations

    def toggle(self, article, selected):
        """Cocher / décocher une carte et émettre si l'état a changé."""
        key = article_key(article)
        changed = False
        if selected:
            if key not in self._articles:
                self._articles[key] = dict(article)
                changed = True
        elif key in self._articles:
            del self._articles[key]
            changed = True
        if changed:
            self.changed.emit()

    def select_all(self, articles):
        """Coche toute une liste (articles visibles de la page)."""
        before = len(self._articles)
        for article in articles:
            self._articles[article_key(article)] = dict(article)
        if len(self._articles) != before:
            self.changed.emit()

    def remove_all(self, articles):
        """Décoche une liste précise (sans toucher au reste)."""
        removed = False
        for article in articles:
            key = article_key(article)
            if self._articles.pop(key, None) is not None:
                removed = True
        if removed:
            self.changed.emit()

    def clear(self):
        """Vide la sélection (bouton « Annuler »)."""
        if self._articles:
            self._articles.clear()
            self.changed.emit()

    def prune_to(self, *lists):
        """Retire les clés absentes de TOUTES les listes fournies.

        Appelée par MainWindow après un rafraîchissement du flux :
        l'univers de sélection est l'union flux + favoris.
        """
        universe = set()
        for articles in lists:
            for article in articles or []:
                universe.add(article_key(article))
        stale = [key for key in self._articles if key not in universe]
        if stale:
            for key in stale:
                del self._articles[key]
            self.changed.emit()

    def is_selected(self, key):
        """True si la clé est cochée."""
        return key in self._articles

    def keys(self):
        """Clés sélectionnées (ordre de cochage)."""
        return list(self._articles)

    def articles(self):
        """Articles sélectionnés (copies fraîches, ordre de cochage)."""
        return [dict(article) for article in self._articles.values()]

    def count(self):
        """Nombre d'éléments cochés."""
        return len(self._articles)
