# Bandito – Portable Wargame NUC

Bandito est un clone conteneurisé, léger et portable du wargame Bandit d'OverTheWire. Conçu pour fonctionner sur des systèmes Raspberry Pi (basé sur Raspbian Lite), ce projet fait partie de l'initiative PWN (Portable Wargame NUC) et permet de déployer et jouer à divers wargames, challenges CTF et machines virtuelles vulnérables dans un environnement isolé et reproductible, sans nécessiter d'accès Internet.

---

## Présentation du Projet

**Qu'est-ce que Bandito ?**

- **Clone de Bandit :** Inspiré du wargame Bandit d'OverTheWire, Bandito offre une série de niveaux de défis permettant de s'exercer aux compétences Linux, à l'administration système et aux bonnes pratiques en cybersécurité.
- **Environnement Conteneurisé :** Le projet exploite Docker pour déployer une instance fraîche de Raspbian Lite sur laquelle sont configurés SSH, Python et divers outils essentiels. Les niveaux sont configurés automatiquement via des scripts Python et des playbooks Ansible.
- **Objectif Pédagogique :** Bandito vise à renforcer l'apprentissage en combinant des compétences techniques variées : gestion de conteneurs, scripting, configuration SSH, et notions de sécurité.

---

## Fonctionnement et Utilisation

**Déploiement**

1. **Construction de l'image Docker :**  
   Utilisez le Dockerfile adapté à votre architecture (amd64, arm, arm64v8) pour construire l'image. Par exemple, pour ARM64 (sur Raspberry Pi) :  
   ```bash
   docker build -t bandito:arm64v8 -f Dockerfile-arm64v8 .
   ```
2. **Exécution du Conteneur :**  
   Une fois l'image construite, lancez le conteneur :
   ```bash
   docker run -d -p 22:22 -p 2222:2222 bandito:arm64v8
   ```
   Vos ports SSH 22 et 2222 seront exposés pour gérer l'administration et l'accès aux différents niveaux du wargame.

**Accès et Interaction**

- **Bannière de Connexion :**  
  Lors de la connexion SSH, une bannière statique est affichée (contenue dans `/etc/issue`), suivie d’une bannière dynamique qui s’exécute depuis `/etc/profile.d/banners.sh` après login. Ces bannières fournissent des informations sur le projet, quelques règles d'utilisation et des instructions utiles.
- **Utilisateurs et Niveaux de Jeu :**  
  Les noms d'utilisateurs des différents niveaux suivent un schéma (par exemple, `somegame0`, `somegame1`, etc.) et les mots de passe correspondants sont stockés dans des fichiers spécifiques (ex. `/etc/somegame_pass/`).  
  Pour jouer, connectez-vous via SSH à l'adresse de votre conteneur et suivez les instructions affichées.

**Conseils aux Joueurs**

- **Création d'un Répertoire de Travail :**  
  L'accès en écriture aux répertoires personnels est désactivé. Il est fortement recommandé de créer un répertoire de travail dans `/tmp/` avec un nom difficile à deviner via la commande :
  ```bash
  mktemp -d
  ```
- **Respect et Convivialité :**  
  - Ne laissez pas de processus orphelins.
  - Ne traînez pas de fichiers d'exploit.
  - Respectez les autres joueurs et évitez de publier des mots de passe ou spoilers.

---

## Conseils et Explications pour les Curieux

Bandito n'est pas qu'un simple challenge. Il s'agit d'une plateforme d'apprentissage et de perfectionnement :
- **Administration Système et Docker :**  
  - Comprenez comment Docker isole l'environnement et comment l'image est créée via le Dockerfile.
  - Explorez la configuration de SSH et l'utilisation de scripts pour la gestion des niveaux.
- **Scripting et Automatisation :**  
  - Les scripts Bash et Python utilisés dans ce projet automatisent plusieurs tâches (génération de clés SSH, configuration des environnements de jeu, etc.).
- **Cybersécurité :**  
  - En pratiquant sur Bandito, vous allez explorer des concepts de sécurité tels que l'escalade de privilèges et la gestion des permissions.
- **Personnalisation :**  
  - N'hésitez pas à explorer le code du projet et à le modifier pour ajouter de nouveaux niveaux ou adapter l'environnement à vos besoins spécifiques.

---

## Dépendances

- [Docker](https://www.docker.com/) – Pour la construction et le déploiement des conteneurs.
- [Raspbian Lite](https://www.raspberrypi.com/software/operating-systems/) – Distribution Linux légère pour Raspberry Pi.

---

## Remerciements

- [OverTheWire](https://overthewire.org/) – Pour la création du Bandit original.
- [rmcmillan34](https://github.com/rmcmillan34/bandito/commits?author=rmcmillan34) – Pour son projet Bandito, dont ce fork a servi de base pour continuer le développement de Bandito.
- [Deselikem](https://dev.to/github/publishing-a-docker-image-to-githubs-container-repository-4n50) – Pour ses ressources et conseils sur la publication d'images Docker.

Profitez de votre séjour sur Bandito et bonne chance dans vos challenges !
