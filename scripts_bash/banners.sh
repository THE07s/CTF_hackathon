#!/bin/bash

sleep 1

echo -e "\033[40m\033[31m
 ▄████▄  ██░ ██ ▄▄▄      ██▓    ██▓   ▓█████ ███▄    █  ▄████▓█████     ▄████▄ ████████▓ █████▒
▒██▀ ▀█ ▓██░ ██▒████▄   ▓██▒   ▓██▒   ▓█   ▀ ██ ▀█   █ ██▒ ▀█▓█   ▀    ▒██▀ ▀█ ▓  ██  ▓  █   ▒ 
▒▓█    ▄▒██▀▀██▒██  ▀█▄ ▒██░   ▒██░   ▒███  ▓██  ▀█ ██▒██░▄▄▄▒███      ▒▓█    ▄▒  █░  ▒  ███ ░ 
▒▓▓▄ ▄██░▓█ ░██░██▄▄▄▄██▒██░   ▒██░   ▒▓█  ▄▓██▒  ▐▌██░▓█  ██▒▓█  ▄    ▒▓▓▄ ▄██░  ██  ░░ █▒  ░ 
▒ ▓███▀ ░▓█▒░██▓▓█   ▓██░██████░██████░▒████▒██░   ▓██░▒▓███▀░▒████▒   ▒ ▓███▀ ░ ▒▒█  ░░ █░    
░ ░▒ ▒  ░▒ ░░▒░▒▒▒   ▓▒█░ ▒░▓  ░ ▒░▓  ░░ ▒░ ░ ▒░   ▒ ▒ ░▒   ▒░░ ▒░ ░   ░ ░▒ ▒  ░ ▒ ░░   ▒ ░    
  ░  ▒   ▒ ░▒░ ░ ▒   ▒▒ ░ ░ ▒  ░ ░ ▒  ░░ ░  ░ ░░   ░ ▒░ ░   ░ ░ ░  ░     ░  ▒      ░    ░      
░        ░  ░░ ░ ░   ▒    ░ ░    ░ ░     ░     ░   ░ ░░ ░   ░   ░      ░         ░      ░ ░    
░ ░      ░  ░  ░     ░  ░   ░  ░   ░  ░  ░  ░        ░      ░   ░  ░   ░ ░                     ░
░                                                                      ░                       \033[0m
Fait partie du projet Portable Wargame NUC (PWN) — série de challenges CTF"

echo "--[ Jouer au jeu ]--

Cette machine peut contenir plusieurs wargames.
Si vous jouez à \"somegame\", alors:

    * Les noms d'utilisateur sont somegame0, somegame1, ...
    * La plupart des niveaux se trouvent dans /somegame/.
    * Les mots de passe pour chaque niveau sont stockés dans /etc/somegame_pass/.

L'accès en écriture aux répertoires personnels étant désactivé, il est conseillé de créer un répertoire de travail avec un nom difficile à deviner dans /tmp/. Vous pouvez utiliser la commande \"mktemp -d\" afin de générer un répertoire aléatoire et difficile à deviner dans /tmp/. L'accès en lecture à /tmp/ est désactivé et l'accès à /proc est restreint pour empêcher les utilisateurs de se surveiller mutuellement. Les fichiers et répertoires aux noms facilement devinables ou trop courts seront supprimés périodiquement ! Le répertoire /tmp est régulièrement effacé.
S'il vous plaît, soyez respectueux :

    * Ne laissez pas de processus orphelins en cours d'exécution
    * Ne laissez pas traîner de fichiers d'exploit
    * N'embêtez pas les autres joueurs

--[ Plus d'informations ]--

Pour plus d'informations concernant les wargames individuelles, visitez
https://github.com/THE07s/CTF_hackaton

Si vous trouvez un bug, n'hésitez pas à signaler un problème sur le Github ci-dessus.

Profitez de votre séjour!"