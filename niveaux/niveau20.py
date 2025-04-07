# Script d'initialisation pour l'utilisateur niveau20

import os
import socket
import textwrap
import CTF_lib
import niveau21

def main():
    NIVEAU = 20
    SUIVANT = 21
    SCRIPT = "/home/niveau20/suconnect"

    # Mots de passe
    mdp_actuel = CTF_lib.get_mdp_hash(NIVEAU)
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Script suconnect simulant une connexion à un port local en TCP
    contenu_script = textwrap.dedent(f"""\
        #!/usr/bin/env python3
        import socket
        import sys

        if len(sys.argv) != 2:
            print("Usage: ./suconnect <portnumber>")
            sys.exit(1)

        port = int(sys.argv[1])
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("localhost", port))
            s.sendall(b"{mdp_actuel}\\n")
            print(s.recv(1024).decode())
    """)

    with open(SCRIPT, "w") as f:
        f.write(contenu_script)

    os.system(f"chown root:niveau{NIVEAU} '{SCRIPT}'")
    os.system(f"chmod 4750 '{SCRIPT}'")  # SUID script

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Utiliser un binaire spécial pour communiquer avec un port local via TCP.

Pour t'aider :
Tu peux écouter un port avec : nc -lvp <numéro du port>

ℹ️ :
Le mot de passe est automatiquement envoyé par le programme, et le serveur répond s’il est correct.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = "/home/niveau20/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_readme}'")
    os.system(f"chmod 640 '{chemin_readme}'")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer le niveau suivant
    niveau21.main()

if __name__ == '__main__':
    main()
