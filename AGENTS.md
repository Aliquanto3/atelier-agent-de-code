# Consignes pour l'agent de code

Ce dépôt sert à un atelier de découverte. Les personnes qui te parlent sont des consultants **non développeurs**.

## Communication
- Réponds toujours en français, avec des phrases simples. Explique un terme technique la première fois que tu l'emploies.
- Termine chaque réponse par un court résumé : ce que tu as fait, et ce que la personne peut vérifier elle-même.
- Le quota de messages est limité : fais le maximum dans chaque réponse. Ne pose une question que si tu es vraiment bloqué ; sinon, fais une hypothèse raisonnable et signale-la.

## Méthode
- **Petits pas** : une modification à la fois, vérifiée avant de passer à la suivante.
- **Spec avant code** : si une demande est floue et qu'il n'existe pas de `SPEC.md`, propose d'en écrire une avant de coder (skill `spec-writer`).
- **Tests avant implémentation** : écris d'abord un test qui échoue pour chaque critère d'acceptation, puis le code qui le fait passer. Ne modifie jamais un test pour le faire passer sans le dire explicitement.
- Lance `pytest -q` après chaque modification du code Python et montre le résultat.
- **Commit par étape** : un commit par étape logique (spec, tests, code, correctif), avec un message en français qui dit ce qui change et pourquoi.

## Sécurité
- Jamais de secret (mot de passe, jeton, clé d'API) dans le code, les tests ou les commits.
- Aucune donnée client ni professionnelle : utilise uniquement des exemples fictifs.
- Pas de dépendance externe ni d'appel réseau dans le code : bibliothèque standard Python, et HTML/CSS/JavaScript sans bibliothèque externe.
- Ne lance pas de serveur qui tourne en continu : indique plutôt à la personne la commande à lancer elle-même dans un autre terminal.

## Repères
- `partie1-tirage/` : page web de tirage au sort de binômes (partie 1 de l'atelier).
- `partie2-relecteur/` : outil en ligne de commande qui relit un texte (partie 2) ; code dans `relecteur/`, tests dans `tests/`.
- `docs/deroule-atelier.md` : déroulé de l'atelier et prompts.
