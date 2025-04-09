# Script d'initialisation pour l'utilisateur niveau20

import os
import socket
import textwrap
import CTF_lib
import niveau19

def main():
    NIVEAU = 18
    SUIVANT = 19
    SCRIPT = f"/home/niveau{NIVEAU}/suconnect"

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
            s.sendall(b"{mdp_suivant}\\n")
            print(s.recv(1024).decode())
    """)

    with open(SCRIPT, "w") as f:
        f.write(contenu_script)

    os.system(f"chown root:niveau{NIVEAU} '{SCRIPT}'")
    os.system(f"chmod 4750 '{SCRIPT}'")  # SUID script

    # Fichier readme
    contenu_readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Un binaire spécial est entre tes mains. Il ne prend pas de mot de passe en argument. \
Il le connaît déjà. Et il est prêt à le transmettre... mais à une seule condition :\
Tu dois être prêt à l’écouter. Littéralement.\
Il te faufra l'utiliser pour communiquer avec un port local via TCP.

Pour t'aider :
Tu dois ouvrir un port sur ta machine. Le programme va s’y connecter, envoyer automatiquement le mot de passe, et attendre une réponse.\
Si tu captes bien ce qu’il envoie, tu auras le mot de passe du niveau suivant.

ℹ️ :
Ouvre un port en écoute sur localhost.\
Lance ensuite le programme, en lui indiquant le port à utiliser.\
Tu devrais voir apparaître quelque chose… peut-être le mot de passe lui-même, ou une réponse du serveur si le mot est correct.\
Une fois la communication terminée, pense à fermer proprement ton écouteur.

Bonne chance, et n’oublie pas : Tu ne cherches pas un mot de passe. Il vient à toi.\
Mais à toi de tendre l’oreille.\
Sois le serveur. Sois prêt. Et surtout… ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_readme}'")
    os.system(f"chmod 640 '{chemin_readme}'")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer le niveau suivant
    niveau19.main()

if __name__ == '__main__':
    main()
