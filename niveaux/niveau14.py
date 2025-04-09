# Script d'initialisation pour l'utilisateur niveau14

import os
import socket
import threading
import multiprocessing
import CTF_lib
import niveau15

def main():
    NIVEAU = 14
    SUIVANT = 15
    PORT = 30000

    # Mots de passe
    mdp_actuel = CTF_lib.get_mdp_hash(NIVEAU)
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Serveur qui attend le mot de passe et répond
    def listener():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("0.0.0.0", PORT))
            s.listen(1)
            while True:
                conn, _ = s.accept()
                with conn:
                    data = conn.recv(1024).decode().strip()
                    if data == mdp_actuel:
                        conn.sendall((mdp_suivant + "\n").encode())
                    else:
                        conn.sendall(b"Wrong password\n")

    # Lancer le serveur dans un processus séparé
    processus_listener = multiprocessing.Process(target=listener)
    processus_listener.start()

    # Fichier readme
    contenu_readme = f"""\
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Un serveur local t’attend… mais il n’accepte de parler qu’à ceux qui connaissent le bon mot de passe. \
Ton rôle ? \
Lui envoyer ton mot de passe actuel, et s’il est correct, il te remettra le précieux sésame pour le niveau suivant.

Pour t'aider :
Le serveur écoute sur le port {PORT} de localhost. \
Il est là, silencieux, prêt à recevoir une seule ligne de texte : ton mot de passe actuel.
Envoie-lui ce qu’il attend, et il t’ouvrira la voie.

ℹ️ :
Tu peux préparer ton mot de passe dans une commande, puis le rediriger vers le bon port. \
Le but est de lui envoyer le mot juste, au bon endroit, d’un seul coup.
Pas besoin de taper à la main : une commande peut faire tout le travail pour toi, du moment qu’elle combine lecture du mot de passe et envoi au bon port.

Bonne chance, et n’oublie pas : Le serveur est muet... mais il écoute.\
Envoie le bon mot, et tu entendras sa réponse
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer le niveau suivant
    niveau15.main()

if __name__ == '__main__':
    main()
