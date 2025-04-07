# Script d'initialisation pour l'utilisateur niveau25

import os
import socket
import threading
import random
import CTF_lib
import niveau26

def main():
    NIVEAU = 25
    PORT = 31001
    mdp_attendu = CTF_lib.get_mdp_hash(NIVEAU)

    # Génération du mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(26)
    CTF_lib.ecrire_fichier_mdp(26, mdp_suivant)

    # Lancer le serveur UDP
    def serveur_udp():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(('0.0.0.0', PORT))
            while True:
                data, addr = s.recvfrom(1024)
                if data.decode().strip() == mdp_attendu:
                    s.sendto(mdp_suivant.encode(), addr)
                else:
                    s.sendto(b"Nope\n", addr)

    threading.Thread(target=serveur_udp, daemon=True).start()

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Communiquer avec un service UDP local pour obtenir le mot de passe du niveau suivant.

Pour t'aider :
Le serveur écoute sur le port {PORT} et attend que tu lui envoies le bon mot de passe en UDP.

ℹ️ :
Trouve la bonne commande

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau26.main()

if __name__ == '__main__':
    main()
