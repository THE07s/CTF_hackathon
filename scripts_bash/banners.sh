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
"

echo "--[ Jouer au jeu ]--

Si vous jouez à \"somegame\", alors:

    * Les noms d'utilisateur sont niveau0, niveau1, ...
    * La plupart des niveaux se trouvent dans le /home de chaque niveau.
    * Les mots de passe pour chaque niveau sont stockés dans /etc/niveau_mdps/.

L'accès en écriture aux répertoires personnels étant désactivé, il est conseillé de créer un répertoire de travail avec un nom difficile à deviner dans /tmp/. Vous pouvez utiliser la commande \"mktemp -d\" afin de générer un répertoire aléatoire et difficile à deviner dans /tmp/. L'accès à /proc est restreint pour empêcher les utilisateurs de se surveiller mutuellement. Les fichiers et répertoires aux noms facilement devinables ou trop courts seront supprimés périodiquement ! Le répertoire /tmp est régulièrement effacé.

S'il vous plaît, soyez respectueux :

    * Ne laissez pas de processus orphelins en cours d'exécution
    * Ne laissez pas traîner de fichiers d'exploit
    * N'embêtez pas les autres joueurs

--[ Plus d'informations ]--

Pour plus d'informations, visitez
https://github.com/THE07s/CTF_hackathon

Si vous trouvez un bug, n'hésitez pas à signaler un problème sur le Github ci-dessus.

Bonne chance!"