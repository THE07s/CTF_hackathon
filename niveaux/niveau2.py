# Script d'initialisation pour l'utilisateur niveau2

import os
import CTF_lib
import niveau3

def main():
    NIVEAU = 2
    SUIVANT = 3
    
    # Génère et enregistre le mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Fichier avec des espaces dans le nom
    nom_fichier = "mon nom contient des espaces"
    chemin_fichier = f"/home/niveau{NIVEAU}/{nom_fichier}"
    with open(chemin_fichier, "w") as f:
        f.write(mdp_suivant + "\n")
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_fichier}'")
    os.system(f"chmod 640 '{chemin_fichier}'")

    # Fichier readme
    contenu_readme = f"""\
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Trouve un fichier contenant le mot de passe du niveau suivant…\
Mais fais gaffe car ce fichier est assez délicat à manipuler.

Pour t'aider :
Le nom du fichier est quelque peu atypique. \
Il te faudra alors être très précis pour le débusquer.

ℹ️ :
Sers-toi de ces commandes pour t'aider à avancer: ls , cd , cat , file , du , find

Bonne chance, et n’oublie pas : ouvre grands les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Passe au niveau suivant
    niveau3.main()

if __name__ == '__main__':
    main()
