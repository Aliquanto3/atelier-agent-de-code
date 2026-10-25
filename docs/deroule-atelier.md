# Déroulé de l'atelier (2 h)

**Objectif pédagogique :** savoir se bricoler un petit outil avec un agent de code, et savoir l'encadrer avec une spec, des tests et une revue.

**Format :** hybride, environ 30 participants, 2 animateurs.
- **Animateur A** : sur scène. Il projette son écran et fait chaque étape en direct, juste avant les participants.
- **Animateur B** : dépannage, priorité aux participants à distance, et surveillance de la discussion en ligne.
- **En salle** : en binômes, sur deux PC, chacun avec son compte. Si l'un épuise son quota, on continue sur l'autre.
- **À distance** : chacun seul. Le plan B Copilot est indiqué dans le README.

**Budget de prompts :** environ 10 par personne sur l'ensemble de l'atelier. Les prompts ci-dessous sont complets et font beaucoup en une fois. Copiez-les tels quels et adaptez-les ensuite.

**Prérequis :** l'auto-test de préparation du README est réussi. Un quart d'heure d'accueil-dépannage est ouvert avant le début.

| Horaire | Séquence | Prompts |
|---|---|---|
| 0:00 – 0:10 | Accueil, objectifs, Codespace ouvert et Codex lancé | 0 |
| 0:10 – 0:35 | Partie 1 : page web de tirage au sort, vérifiée « à l'œil » | 2 à 3 |
| 0:35 – 0:40 | Débrief : « Comment savez-vous que ça marche ? » | 0 |
| 0:40 – 1:00 | Partie 2, étape 1 : du besoin à la spec | 1 à 2 |
| 1:00 – 1:15 | Partie 2, étape 2 : les tests avant le code | 1 |
| 1:15 – 1:35 | Partie 2, étape 3 : le code, puis l'essai | 1 |
| 1:35 – 1:45 | Partie 2, étape 4 : la revue | 1 à 2 |
| 1:45 – 1:52 | Partie 2, étape 5 : branche, commits, pull request | 1 |
| 1:52 – 2:00 | Débrief final et suites | 0 |

---

## 0:00 – 0:10 · Accueil

- Message clé : *l'agent fait le geste technique, vous gardez les décisions.*
- Chacun ouvre son Codespace ([github.com/codespaces](https://github.com/codespaces)) puis lance `codex` dans le terminal.
- Démonstration rapide de l'écran : explorateur de fichiers à gauche, éditeur au centre, terminal en bas.
- Rappel : aucune donnée client ni professionnelle.

## 0:10 – 0:35 · Partie 1 : page web de tirage au sort

Mode « vibe coding » : on demande, on regarde, on ajuste. Aucune spec, aucun test.

**Prompt 1 :**
```text
Crée une page web dans le fichier partie1-tirage/index.html, avec le HTML, le CSS et le JavaScript dans ce seul fichier, sans aucune bibliothèque externe.
La page sert à animer un atelier :
- une grande zone de texte où je colle une liste de prénoms, un par ligne ;
- un bouton « Former des binômes » qui mélange la liste au hasard et affiche les binômes sous forme de cartes colorées ;
- si le nombre de prénoms est impair, le dernier groupe est un trinôme.
Style moderne, coloré et lisible, textes en français.
À la fin, explique-moi en deux lignes comment ouvrir la page dans le Codespace.
```

**Pour voir le résultat :** clic droit sur `partie1-tirage/index.html`, puis **Show Preview**. Collez une dizaine de prénoms inventés.

**Prompt 2 (embellir) :**
```text
Améliore la page partie1-tirage/index.html :
- une petite animation de mélange quand je clique sur le bouton ;
- un bouton « Copier le résultat » qui copie la liste des binômes dans le presse-papiers ;
- un compteur qui affiche le nombre de prénoms saisis.
Ne change rien d'autre.
```

**Prompt 3 (libre) :** chacun demande une amélioration de son choix (thème sombre, nommer les groupes, etc.).

## 0:35 – 0:40 · Débrief de la partie 1

Faites tester les cas limites, sans nouveau prompt :
- une liste vide ;
- un seul prénom ;
- des lignes vides au milieu de la liste ;
- deux fois le même prénom.

Questions à poser à la salle :
- Est-ce que ça marche ? **Comment le savez-vous ?**
- Qu'est-ce qui était attendu pour une liste vide ? Personne ne l'avait dit.
- Si vous changez la page demain, comment savoir que vous n'avez rien cassé ?

Transition : *pour une page jetable, vérifier à l'œil suffit. Pour un outil dont on va se servir, on écrit d'abord ce qu'on attend, puis on le fait vérifier automatiquement.* C'est la partie 2.

## 0:40 – 1:00 · Partie 2, étape 1 : du besoin à la spec

Montrez d'abord le point de départ. Dans un second terminal (icône **+** du terminal), tapez `pytest -q` : un test échoue volontairement. C'est normal, rien n'est encore codé.

**Prompt 4 :**
```text
Crée d'abord une branche git nommée relecteur et place-toi dessus.
Ensuite, utilise le skill $spec-writer pour ce besoin :
« Je suis consultant et je relis souvent des livrables. Je voudrais un petit outil en ligne de commande qui analyse un texte en français et me signale ce qui nuit à sa lisibilité : sa longueur, son temps de lecture, les phrases trop longues et les mots creux du jargon de conseil. »
Écris la spec dans partie2-relecteur/SPEC.md. Le point de départ du code est partie2-relecteur/relecteur/analyse.py, et il existe déjà un test dans partie2-relecteur/tests/. Ne code rien.
Fais un commit de la spec.
```

**Travail humain, le plus important de l'atelier (10 min) :**
- Ouvrez `partie2-relecteur/SPEC.md` et lisez les critères d'acceptation.
- Tranchez chaque question ouverte **en modifiant directement le fichier** : seuil d'une phrase trop longue, liste des mots creux, traitement d'un texte vide…
- Supprimez ce qui ne vous sert pas et ajoutez ce qui manque.

**Prompt 5 (facultatif, si vous avez beaucoup modifié la spec) :**
```text
J'ai relu et modifié partie2-relecteur/SPEC.md et tranché les questions ouvertes.
Vérifie que chaque critère d'acceptation est testable, précis et cohérent avec les autres. Corrige uniquement ce qui pose problème, montre-moi les changements, puis fais un commit.
```

## 1:00 – 1:15 · Partie 2, étape 2 : les tests avant le code

**Prompt 6 :**
```text
Lis partie2-relecteur/SPEC.md.
Dans partie2-relecteur/tests/, écris au moins un test pytest par critère d'acceptation, en nommant chaque test d'après son critère (par exemple test_ca3_phrase_trop_longue). Garde le test existant s'il est cohérent avec la spec, sinon adapte-le et dis-le.
N'écris pas encore le code de l'outil.
Lance pytest -q et explique-moi pourquoi les tests échouent. Ils doivent échouer parce que le code n'existe pas, pas à cause d'une erreur dans les tests.
Fais un commit des tests.
```

À faire vérifier par les participants : ouvrir un test et le relire. Le test dit-il bien ce que dit le critère ? Message clé : *les tests sont la spec rendue exécutable.*

## 1:15 – 1:35 · Partie 2, étape 3 : le code

**Prompt 7 :**
```text
Implémente l'outil dans partie2-relecteur/relecteur/ pour faire passer tous les tests, sans modifier les tests.
Avance par petits pas : un critère d'acceptation à la fois, en relançant pytest -q après chacun.
Ajoute aussi la commande python -m relecteur <fichier>, qui affiche l'analyse de façon lisible en français.
Fais un commit du code quand tous les tests passent, puis résume-moi ce que tu as fait.
```

**Essai par les participants :**
```bash
cd partie2-relecteur
python -m relecteur exemples/texte-exemple.txt
```

Ensuite, chacun écrit son propre texte fictif dans un nouveau fichier et le fait analyser.

Vous pouvez aussi ouvrir le panneau **Testing** (icône en forme de fiole à gauche) : les tests passent au vert.

## 1:35 – 1:45 · Partie 2, étape 4 : la revue

**Prompt 8 :**
```text
Relis ton propre code comme un relecteur exigeant qui ne l'a pas écrit.
Cherche les écarts avec partie2-relecteur/SPEC.md, les cas oubliés, et les textes qui feraient planter l'outil ou donneraient un résultat faux : texte vide, texte sans ponctuation, abréviations comme « M. » ou « etc. », points de suspension, nombres décimaux comme « 3,5 ».
Liste les problèmes par ordre d'importance, sans rien corriger.
```

**Décision humaine :** choisissez les problèmes à corriger. Tout n'est pas à corriger.

**Prompt 9 :**
```text
Corrige les problèmes n° X et n° Y. Pour chacun, ajoute d'abord un test qui reproduit le problème et vérifie qu'il échoue, puis corrige le code et relance pytest -q.
Fais un commit par correctif.
```

## 1:45 – 1:52 · Partie 2, étape 5 : branche, commits, pull request

**Prompt 10 :**
```text
Pousse la branche relecteur sur GitHub, puis ouvre une pull request vers main avec gh pr create.
La description de la pull request doit reprendre, en français, les critères d'acceptation de la spec, le résultat de pytest et les limites connues.
Donne-moi le lien de la pull request.
```

Codex peut demander l'autorisation d'accéder au réseau pour pousser la branche. **Lisez la commande, puis acceptez.** C'est le bon réflexe : on valide ce qu'on comprend.

Ouvrez le lien. Sur GitHub, l'onglet **Commits** montre l'histoire du travail (spec, tests, code, correctifs) et l'onglet **Files changed** montre ce qui a été produit.

## 1:52 – 2:00 · Débrief final

Les trois réflexes pour encadrer une IA :
1. **Spec** : écrire ce qu'on attend, avec des exemples précis, et trancher soi-même les choix.
2. **Tests** : rendre la spec vérifiable automatiquement, avant le code.
3. **Revue** : faire relire, décider de ce qu'on corrige, et garder une trace (commits, pull request).

Suites possibles :
- reprendre la partie 1 avec la méthode de la partie 2 ;
- ajouter une fonctionnalité au relecteur, en commençant par la spec.

Rappels :
- désactiver la connexion par code d'appareil dans ChatGPT ;
- arrêter son Codespace ;
- toujours aucune donnée client ni professionnelle.

---

## Notes pour les animateurs

- **La veille :** refaire tout le parcours avec un compte de démo, relever le quota avec `/status` après les 10 prompts, et vérifier le libellé exact de l'option de sécurité dans ChatGPT.
- **Si la salle est en retard :** sauter le prompt 3, le prompt 5 et le prompt 9. Le prompt 10 peut être fait en démonstration seulement.
- **Si un participant n'a plus de quota :** il continue sur le PC de son binôme, ou passe au plan B Copilot (voir le README).
