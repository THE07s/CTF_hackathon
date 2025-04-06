# 🧩 CTF Hackaton — Défi Linux Conteneurisé

CTF Hackaton est un clone francisé et conteneurisé du wargame **Bandit** d'OverTheWire.  
Conçu pour fonctionner sur **Raspberry Pi** (et tout environnement Docker ARM64v8 ou x86_64), il permet d'apprendre la ligne de commande, les droits Unix, le réseau, et la cybersécurité à travers **34 niveaux progressifs**.

---

## 🎯 Objectif pédagogique

- 👨‍💻 Apprendre les commandes système de base (`cat`, `find`, `grep`, `ssh`, etc.)
- 🔐 Comprendre les droits Unix, les UID/GID, les scripts shell, la compression, l'encodage
- 🧠 Résoudre des énigmes Linux pour progresser
- 📦 Travailler dans un environnement conteneurisé, propre et reproductible

---

## 🐧 Caractéristiques

- 🐳 Docker léger basé sur `debian:bullseye-slim`
- 🔧 Compatible Raspberry Pi (ARMv8)
- 🇫🇷 Fichiers `readme` explicatifs pour chaque niveau
- 🚀 Génération automatisée via `Makefile`
- 🧪 Validation automatique via `valide_niveaux.py`
- 🔁 Ports exposés pour niveaux réseau (30000, 30001, 31000-32000…)

---

## ⚙️ Installation et lancement

### 1. Cloner le dépôt

```bash
git clone https://github.com/THE07s/CTF_hackaton.git
cd CTF_hackaton
```

### 2. Builder l’image Docker

```bash
docker build -t ctf-hackaton .
```

### 3. Lancer le conteneur avec les bons ports

```bash
docker run -it \
  -p 2222:2222 \
  -p 30000:30000 -p 30001:30001 \
  -p 31000-32000:31000-32000 \
  ctf-hackaton
```

---

## 🔐 Se connecter

```bash
ssh niveau0@localhost -p 2222
mot de passe : bandit0
```

> Un fichier `readme` est présent dans le répertoire de chaque joueur (`/home/niveauX/`) pour expliquer l’objectif du niveau en cours.  
> Les mots de passe suivants sont stockés dans `/etc/niveau_mdps/niveauX`.

---

## 🗂️ Structure du projet

```
.
├── Dockerfile              # Image Docker ARM compatible
├── README.md               # Ce fichier
├── descriptions/           # Pistes et aides en Markdown pour chaque niveau
├── niveaux/                # Scripts Python pour chaque niveau + init
├── scripts_bash/           # Bannière et autres scripts shell utiles
```

---

## 🧪 Tester les niveaux automatiquement

```bash
sudo python3 niveaux/valide_niveaux.py
```

Ce script simule un joueur qui résout les niveaux un par un avec les bonnes commandes.

---

## 📦 Déploiement GitHub

Un **workflow GitHub Actions** permet de :

- Builder automatiquement l’image Docker
- La publier dans la section **Packages** du dépôt GitHub

Tu trouveras ce workflow dans `.github/workflows/docker.yml`

---

## 🙏 Remerciements

- [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/)
- [rmcmillan34/bandito](https://github.com/rmcmillan34/bandito)
- Projet forké, traduit, amélioré et adapté à Raspberry Pi par [THE07s](https://github.com/THE07s)

---

## 🧠 Note aux joueurs

- Les répertoires personnels ne sont pas modifiables, utilise `/tmp/` :
  ```bash
  cd $(mktemp -d)
  ```
- Ne publie pas les mots de passe.
- Ne laisse pas traîner de fichiers suspects.
- Respecte les autres joueurs 🫶

Bonne chance, et ouvre bien les 👀
