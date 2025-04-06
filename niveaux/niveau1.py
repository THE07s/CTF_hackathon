# Script d'initialisation pour l'utilisateur niveau1

import os
import CTF_lib
import niveau2

def main():
    NIVEAU = 1
    SUIVANT = 2

    # Crée l'utilisateur niveau1
    CTF_lib.ajout_utilisateur(NIVEAU)

    # Génère le mot de passe du niveau suivant et l'enregistre
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Fichier piège nommé "-"
    chemin_fichier = f"/home/niveau{NIVEAU}/-"
    with open(chemin_fichier, "w") as f:
        f.write(mdp_suivant + "\n")
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_fichier}'")
    os.system(f"chmod 640 '{chemin_fichier}'")

    # Fichier readme explicatif
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Dans ce niveau, tu dois trouver le mot de passe caché dans un fichier au nom un peu particulier.

Pour t'aider :
Un seul fichier est présent dans ton répertoire personnel… mais son nom peut causer des surprises.

ℹ️ :
Essaie d'accéder au fichier en le ciblant avec un chemin explicite.
Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Passe au niveau suivant
    niveau2.main()

if __name__ == '__main__':
    main()
