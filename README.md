# Bandito
Tout comme Bandit... mais petit, et portable.

## Introduction
Un clone conteneurisé léger du wargame Bandit d'OverTheWire (https://overthewire.org/wargames/bandit/). Ce projet est né dans le cadre du projet PWN (Portable Wargame NUC) afin de pouvoir déployer et jouer à des wargames, des CTF et à des machines virtuelles vulnérables sans accès Internet.

## Méthodologie
Je pense pouvoir créer un environnement reproductible pour pratiquer les compétences Linux en utilisant Docker, Ansible, Bash et du script Python. Recréer chaque niveau de Bandit au fur et à mesure sera similaire à la réalisation d'une writeup, tout en intégrant des compétences en administration système et DevOps pour renforcer l'apprentissage.

Docker sera utilisé pour déployer une instance fraîche de Raspbian Lite et des playbooks Ansible serviront à construire l'environnement Bandito niveau par niveau. Des langages de script comme Bash et Python seront utilisés pour automatiser des tâches au niveau du système d'exploitation, telles que la création de fichiers/dossiers, la génération de chaînes aléatoires, la création d'utilisateurs, la configuration des permissions, etc.

Entreprendre un projet pour créer un wargame dockerisé, comme Bandit, implique diverses compétences sur plusieurs domaines :

## Dépendances
- [Docker](https://www.docker.com/)

## Remerciements
- [OverTheWire](https://overthewire.org/) - Pour la création du Bandit original.
- [rmcmillan34](https://github.com/rmcmillan34/bandito/commits?author=rmcmillan34) - Pour son projet Bandito, dont ce fork a servi de base pour ce projet.
- [Raspbian Lite](https://www.raspberrypi.com/software/operating-systems/) - Pour la mise à disposition d'une distribution Linux légère pour Raspberry Pi. 
- [Deselikem](https://dev.to/github/publishing-a-docker-image-to-githubs-container-repository-4n50) - Pour
