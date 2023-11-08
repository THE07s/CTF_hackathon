#!/bin/bash

echo "\033[40m\033[31m ▄▄▄▄    ▄▄▄       ███▄    █ ▓█████▄  ██▓▄▄▄█████▓ ▒█████
▓█████▄ ▒████▄     ██ ▀█   █ ▒██▀ ██▌▓██▒▓  ██▒ ▓▒▒██▒  ██▒
▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██▒▒ ▓██░ ▒░▒██░  ██▒
▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌░██░░ ▓██▓ ░ ▒██   ██░
░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░██░  ▒██▒ ░ ░ ████▓▒░
░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░▓    ▒ ░░   ░ ▒░▒░▒░
▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ▒ ░    ░      ░ ▒ ▒░
 ░    ░   ░   ▒      ░   ░ ░  ░ ░  ░  ▒ ░  ░      ░ ░ ░ ▒
 ░            ░  ░         ░    ░     ░               ░ ░
      ░                       ░                             \033[39m
  This is an OverTheWire Bandit clone made in Alpine Linux
     More info: https://github.com/rmcmillan34/bandito"

sleep 1

echo "\033[32m     ██▓███        █     █░      ███▄    █
    ▓██░  ██▒     ▓█░ █ ░█░      ██ ▀█   █
    ▓██░ ██▓▒     ▒█░ █ ░█      ▓██  ▀█ ██▒
    ▒██▄█▓▒ ▒     ░█░ █ ░█      ▓██▒  ▐▌██▒
    ▒██▒ ░  ░ ██▓ ░░██▒██▓  ██▓ ▒██░   ▓██░ ██▓
    ▒▓▒░ ░  ░ ▒▓▒ ░ ▓░▒ ▒   ▒▓▒ ░ ▒░   ▒ ▒  ▒▓▒
    ░▒ ░      ░▒    ▒ ░ ░   ░▒  ░ ░░   ░ ▒░ ░▒
    ░░        ░     ░   ░   ░      ░   ░ ░  ░
               ░      ░      ░           ░   ░
               ░             ░               ░\033[39m
Part of the project Portable Wargame NUC (PWN) series of CTF challenges"

sleep 0.5

echo "--[ Playing the game ]--

  This machine might hold several wargames.
  If you are playing "somegame", then:

    * USERNAMES are somegame0, somegame1, ...
    * Most LEVELS are stored in /somegame/.
    * PASSWORDS for each level are stored in /etc/somegame_pass/.

  Write-access to homedirectories is disabled. It is advised to create a
  working directory with a hard-to-guess name in /tmp/.  You can use the
  command \"mktemp -d\" in order to generate a random and hard to guess
  directory in /tmp/.  Read-access to both /tmp/ is disabled and to /proc
  restricted so that users cannot snoop on eachother. Files and directories
  with easily guessable or short names will be periodically deleted! The /tmp
  directory is regularly wiped.
  Please play nice:

    * don't leave orphan processes running
    * dont' leave exploit-files laying around
    * don't annoy other players

--[ More information ]--

  For more information regarding individual wargames, visit
  https://github.com/rmcmillan34/bandito

  If you find a bug please feel free to raise an issue on the github above.

  Enjoy your stay!"
