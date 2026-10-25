# Atelier : découvrir un agent de code

En deux heures, vous allez construire deux petits outils **sans écrire vous-même de code**, en confiant le travail à un agent de code (Codex) et en apprenant à l'encadrer : spec, tests, revue.

- **Partie 1 : une page web de tirage au sort.** Résultat très visuel en quelques minutes, vérifié « à l'œil ».
- **Partie 2 : un relecteur de livrable.** Un vrai petit outil, construit avec méthode : spec, puis tests, puis code, puis revue.

Tout se passe dans votre navigateur, avec des comptes personnels gratuits. Rien à installer sur votre PC, aucun droit administrateur nécessaire.

> **Rappel important : aucune donnée client ni professionnelle.** Utilisez des comptes personnels et uniquement des textes fictifs ou publics.

---

## Avant l'atelier : préparation (20 minutes, à faire chez vous)

### 1. Créer vos deux comptes personnels gratuits
- **GitHub** : [github.com/signup](https://github.com/signup), offre Free. Confirmez votre adresse e-mail (lien reçu par mail).
- **ChatGPT** : [chatgpt.com](https://chatgpt.com), offre Free. Une vérification par téléphone peut être demandée.

Utilisez une adresse personnelle, pas votre adresse professionnelle.

### 2. Autoriser la connexion par code d'appareil dans ChatGPT
Le Codespace n'a pas de navigateur à lui : Codex s'y connecte grâce à un code que vous saisissez dans votre propre navigateur. Il faut l'autoriser une fois :

1. Sur [chatgpt.com](https://chatgpt.com), cliquez sur votre profil (en bas à gauche), puis **Settings** (Paramètres).
2. Ouvrez l'onglet **Security** (Sécurité).
3. Activez l'option de **connexion par code d'appareil pour Codex** (*device code authorization*).

### 3. Créer votre copie du dépôt et ouvrir un Codespace
1. En haut de cette page, cliquez sur **Use this template**, puis **Create a new repository**.
2. Propriétaire : votre compte. Nom : `atelier-agent-de-code`. Visibilité : **Private** conseillé. Cliquez sur **Create repository**.
3. Dans votre nouveau dépôt, cliquez sur le bouton vert **Code**, onglet **Codespaces**, puis **Create codespace on main**.
4. Patientez 2 à 5 minutes : un éditeur (VS Code) s'ouvre dans le navigateur, avec un terminal en bas. Codex s'installe automatiquement.

### 4. Connecter Codex à votre compte ChatGPT
Dans le terminal en bas de l'écran, tapez :

```bash
codex login --device-auth
```

Codex affiche un lien et un code à usage unique. Ouvrez le lien dans un nouvel onglet, connectez-vous à ChatGPT si besoin, saisissez le code. Le terminal confirme la connexion.

### 5. Lancer Codex et faire l'auto-test
```bash
codex
```

Tapez : `Dis bonjour en une phrase.` Codex doit vous répondre en français.
Tapez ensuite `/status` pour voir votre quota restant, puis `/quit` pour sortir.

**Auto-test réussi ?** Vous êtes prêt. Arrêtez votre Codespace pour économiser votre quota gratuit : [github.com/codespaces](https://github.com/codespaces), menu « … » à côté du Codespace, **Stop codespace**.

**Bloqué ?** Consultez le dépannage plus bas, ou venez au quart d'heure d'accueil-dépannage avant l'atelier.

---

## Partie 1 : page web de tirage au sort

**Énoncé.** Une page web qui forme des binômes au hasard à partir d'une liste de prénoms, pour animer un atelier.

**Terminé quand :**
- le fichier `partie1-tirage/index.html` existe et s'ouvre dans le navigateur ;
- coller une liste de prénoms (un par ligne) puis cliquer sur un bouton affiche des binômes ;
- avec un nombre impair de prénoms, personne n'est oublié.

**Pour voir la page :** clic droit sur `index.html` dans l'explorateur de fichiers, puis **Show Preview**.

## Partie 2 : relecteur de livrable

**Énoncé.** Un outil en ligne de commande qui analyse un texte en français et signale ce qui nuit à sa lisibilité : longueur, temps de lecture, phrases trop longues, mots creux du jargon de conseil (« synergie », « holistique »…).

Point de départ : `partie2-relecteur/`, avec un test qui **échoue volontairement**. Lancez `pytest -q` pour le voir échouer.

**Terminé quand :**
- `partie2-relecteur/SPEC.md` existe, relue par vous, avec 5 à 8 critères d'acceptation testables ;
- chaque critère d'acceptation a au moins un test ;
- `pytest -q` affiche que tous les tests passent ;
- depuis le dossier `partie2-relecteur`, la commande `python -m relecteur exemples/texte-exemple.txt` affiche l'analyse du texte d'exemple ;
- le travail est sur une branche, avec une pull request ouverte.

Le pas-à-pas et les prompts sont dans [docs/deroule-atelier.md](docs/deroule-atelier.md).

---

## Dépannage

| Symptôme | Cause probable | Solution |
|---|---|---|
| `codex login --device-auth` ouvre une page de connexion classique, ou rien ne se passe après la saisie du code | La connexion par code d'appareil n'est pas activée | Refaites l'étape 2, puis relancez `codex login --device-auth` |
| « Code expiré » ou « code invalide » | Le code n'est valable que quelques minutes | Relancez `codex login --device-auth` et saisissez le nouveau code tout de suite |
| `codex: command not found` | L'installation automatique a échoué | Tapez `npm install -g @openai/codex@0.164.0`, puis réessayez |
| Message de limite d'usage (*usage limit*, *rate limit*) | Quota gratuit épuisé | `/status` indique l'heure de remise à zéro. En attendant : travaillez sur l'écran de votre binôme, ou utilisez le plan B ci-dessous |
| Codex signale une erreur de *sandbox* ou de *landlock* quand il lance une commande | Le bac à sable de Codex n'est pas pris en charge par ce conteneur | Quittez Codex et relancez-le avec `codex --sandbox danger-full-access`. Acceptable ici car le Codespace est une machine jetable, isolée de votre PC |
| L'écran affiche « Codespace arrêté » ou reste gris | Arrêt automatique après 30 minutes d'inactivité | Rechargez la page, ou allez sur [github.com/codespaces](https://github.com/codespaces) et rouvrez-le. Vos fichiers et votre connexion Codex sont conservés |
| `pytest: command not found` | Commande absente du chemin | Utilisez `python -m pytest -q` |
| La page web ne s'affiche pas | Aperçu non lancé | Clic droit sur `index.html`, **Show Preview**. Sinon, dans un terminal : `python -m http.server 8000 --directory partie1-tirage`, puis cliquez sur **Open in Browser** |

**Plan B si le quota Codex est épuisé :** GitHub Copilot est intégré au Codespace. Activez l'offre gratuite sur [github.com/settings/copilot](https://github.com/settings/copilot), ouvrez la fenêtre de discussion Copilot (icône en haut de l'éditeur), choisissez le mode **Agent** et utilisez les mêmes prompts.

---

## Après l'atelier
- **Désactivez la connexion par code d'appareil** dans ChatGPT (Settings > Security). Elle n'est utile que pour l'atelier, et ce type de connexion peut être détourné par hameçonnage.
- Supprimez votre Codespace si vous ne vous en servez plus : [github.com/codespaces](https://github.com/codespaces).
- Votre dépôt reste à vous : continuez à l'enrichir.
