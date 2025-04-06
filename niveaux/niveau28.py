# Script d'initialisation pour l'utilisateur niveau28

import os
import CTF_lib
import niveau29

def main():
    NIVEAU = 28
    SUIVANT = 29

    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    dossier = f"/home/niveau{NIVEAU}"

    # Groupe spécial
    groupe = f"mdplevel{NIVEAU}"
    os.system(f"groupadd -f {groupe}")
    os.system(f"usermod -a -G {groupe} niveau{NIVEAU}")

    # Fichier avec droits de groupe uniquement
    chemin_fichier = os.path.join(dossier, "acces_groupe.txt")
    with open(chemin_fichier, "w") as f:
        f.write(mdp_suivant + "\n")

    os.system(f"chown root:{groupe} {chemin_fichier}")
    os.system(f"chmod 640 {chemin_fichier}")  # -rw-r-----

    # Readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Lire un fichier dont l’accès est limité à un groupe UNIX spécifique.

Pour t'aider :
Un fichier n’appartient pas à toi, mais tu fais partie du groupe autorisé à le lire.

ℹ️ :
Trouve les commande affectant les groupes : 

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = os.path.join(dossier, "readme")
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau29.main()

if __name__ == '__main__':
    main()
