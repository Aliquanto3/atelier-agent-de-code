"""Tests du relecteur.

Ce premier test échoue volontairement : c'est le point de départ.
L'agent écrira les autres tests à partir des critères d'acceptation de SPEC.md.
"""

from relecteur.analyse import compter_mots


def test_compte_les_mots_d_une_phrase_simple():
    assert compter_mots("Bonjour à tous.") == 3
