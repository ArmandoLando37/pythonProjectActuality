# -*- coding: utf-8 -*-
"""Tests du modèle ArticleSelection (étape 3 : sélection + export PDF).

Auto-exécutable : python tests/test_selection.py
Aucune dépendance d'affichage (QCoreApplication suffit).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt5.QtCore import QCoreApplication

from core.selection import ArticleSelection, article_key

app = QCoreApplication(sys.argv)

URL_A = "https://example.org/a"
URL_B = "https://example.org/b"

ART_A = {"title": "Article A", "url": URL_A, "source": "Reuters"}
ART_B = {"title": "Article B", "url": URL_B, "source": "Le Monde"}
ART_C = {"title": "Sans URL", "source": "L'Equipe"}
ART_C_DUPLICATE = {"title": "Sans URL", "source": "L'Equipe",
                   "view": "doublon sans url"}

selection = ArticleSelection()

# 1. clé stable : URL d'abord, titre+source en secours
assert article_key(ART_A) == URL_A
assert article_key(ART_C) == article_key(ART_C_DUPLICATE) == \
    "Sans URL|L'Equipe"
print("1. clé stable : OK")

# 2. toggle : cochage / décochage + signal
seen = []
selection.changed.connect(lambda: seen.append(1))
selection.toggle(ART_A, True)
assert selection.count() == 1 and selection.is_selected(URL_A)
assert seen[-1:] == [1]
selection.toggle(ART_A, True)  # re-cocher ne change rien
assert len(seen) == 1
selection.toggle(ART_A, False)
assert selection.count() == 0
print(f"2. toggle + signal émis {len(seen)}x : OK")
selection.changed.disconnect()

# 3. toggle sur article SANS URL : clé de repli titre|source (stable)
selection.toggle(ART_C, True)
selection.toggle(ART_C_DUPLICATE, False)  # même clé -> décoche
assert selection.count() == 0
print("3. repli titre|source : OK")

# 4. select_all / remove_all / clear
selection.select_all([ART_A, ART_B, ART_C])
assert selection.count() == 3
selection.remove_all([ART_B])
assert selection.count() == 2 and not selection.is_selected(URL_B)
articles = selection.articles()
assert len(articles) == 2
assert {a.get("url", "") for a in articles} == {URL_A, ""}
selection.toggle(ART_C_DUPLICATE, False)  # même clé que ART_C
assert selection.count() == 1
selection.clear()
assert selection.count() == 0
print("4. select_all / remove_all / clear : OK")

# 5. prune_to : seul l'union flux + favoris garde la sélection
selection.toggle(ART_A, True)
selection.toggle(ART_B, True)
selection.prune_to([ART_A], [ART_B])          # rien à retirer
assert selection.count() == 2
selection.prune_to([ART_A], [ART_C])          # ART_B absent -> décoché
assert selection.count() == 1 and selection.is_selected(URL_A)
selection.prune_to([], [])                    # flux vide -> tout retire
assert selection.count() == 0
print("5. prune_to (union flux+favoris) : OK")

print("TESTS ARTICLE SELECTION : OK")
