# Script d'initialisation pour l'utilisateur niveau10

import os
import base64
import CTF_lib
import niveau11

def main():
    NIVEAU = 10
    SUIVANT = 11

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Encodage en base64
    encoded = base64.b64encode(mdp_suivant.encode()).decode()

    # Écriture du fichier
    chemin_fichier = f"/home/niveau{NIVEAU}/data.txt"
    with open(chemin_fichier, "w") as f:
        f.write(encoded + "\n")

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_fichier}'")
    os.system(f"chmod 640 '{chemin_fichier}'")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Décoder le contenu d’un fichier contenant le mot de passe du niveau suivant.

Pour t'aider :
Le mot de passe est encodé, un format courant de transmission de données.

ℹ️ :
Trouver l'encodage et la commande pour convertir le fichier en texte clair.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau11.main()

if __name__ == '__main__':
    main()
