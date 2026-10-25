---
name: spec-writer
description: Transforme un besoin flou, exprimé en langage courant, en un fichier SPEC.md structuré (contexte, user stories, critères d'acceptation testables, hors périmètre, questions ouvertes). À utiliser quand quelqu'un décrit un outil à construire et qu'aucune spec n'existe encore, ou demande explicitement une spec. Ne pas utiliser pour écrire du code ni des tests.
---

# Rédiger une spec à partir d'un besoin flou

Ton rôle : aider une personne non développeuse à préciser ce qu'elle veut **avant** que la moindre ligne de code soit écrite. Tu n'écris ni code ni test dans cette étape.

## Déroulé

1. Relis le besoin. Repère ce qui est flou : mots ambigus (« phrase », « long », « simple »), cas limites (texte vide, valeurs extrêmes), forme du résultat attendu.
2. Ne pose pas de questions une par une (le quota de messages est limité). Fais des hypothèses raisonnables, écris-les dans la spec, et regroupe les vrais choix à trancher dans la section « Questions ouvertes ».
3. Écris le fichier `SPEC.md` à l'endroit demandé (par défaut, dans le dossier du projet concerné), avec exactement la structure ci-dessous.
4. Termine ta réponse en invitant la personne à relire la spec, à trancher les questions ouvertes **en modifiant directement le fichier**, et à revenir ensuite.

## Structure de SPEC.md

```markdown
# Spec : <nom de l'outil>

## Contexte
Qui a ce besoin, dans quelle situation, et quel problème l'outil résout. 3 à 5 phrases.

## User stories
- En tant que <rôle>, je veux <action> afin de <bénéfice>.
(3 à 5 stories au plus)

## Critères d'acceptation
Chaque critère est numéroté, observable et vérifiable par un test automatique.
Il donne un exemple concret avec des valeurs précises.

- **CA1 — <titre court>** : Étant donné <situation précise>, quand <action>, alors <résultat exact attendu>.
  Exemple : avec le texte « Bonjour à tous. », le nombre de mots affiché est 3.

## Hors périmètre
Ce que l'outil ne fera pas dans cette version (pour éviter qu'il grossisse sans fin).

## Hypothèses
Les choix faits par défaut, que la personne peut contester.

## Questions ouvertes
- [ ] Q1 — <question> (proposition par défaut : <réponse proposée>)
```

## Règles de qualité

- Entre 5 et 8 critères d'acceptation : le projet doit tenir en une heure.
- Chaque critère contient un exemple chiffré ou un texte exact ; pas de « rapide », « joli », « correct » sans mesure.
- Couvre au moins un cas limite (entrée vide, entrée inattendue).
- Un critère = un comportement. Si un critère contient « et », découpe-le.
- Aucune donnée réelle, client ou professionnelle dans les exemples : invente-les.
