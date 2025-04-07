# Script d'initialisation pour l'utilisateur niveau30

import os
import CTF_lib
import niveau31
import tempfile
import time
import threading

def main():
    NIVEAU = 30
    SUIVANT = 31

    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)

    def daemon_fichier():
        while True:
            with tempfile.NamedTemporaryFile(prefix="secret_", dir="/tmp", delete=False) as f:
                f.write(mdp_suivant.encode())
                f.flush()
                time.sleep(60)  # laisse le fichier ouvert
                os.unlink(f.name)

    # Lancer le script en tâche de fond
    threading.Thread(target=daemon_fichier, daemon=True).start()

    # Readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Repérer un processus qui garde un fichier temporaire ouvert contenant le mot de passe du niveau suivant.

Pour t'aider :
Le fichier est stocké temporairement et reste ouvert par un processus.

ℹ️ :
Explore les fichiers.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau31.main()

if __name__ == '__main__':
    main()
