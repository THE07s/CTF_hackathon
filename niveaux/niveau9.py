# Script d'initialisation pour l'utilisateur niveau9

import os
import random
import CTF_lib
import niveau10

def main():
    NIVEAU = 9
    SUIVANT = 10

    # Le mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    chemin_fichier = f"/home/niveau{NIVEAU}/data.txt"
    with open(chemin_fichier, "wb") as f:
        f.write(os.urandom(1024))                          # Données binaires avant
        f.write(b"\n" + mdp_suivant.encode() + b"\n")      # Chaîne ASCII (le mot de passe)
        f.write(os.urandom(1024))                          # Données binaires après

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_fichier}'")
    os.system(f"chmod 640 '{chemin_fichier}'")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Trouver une chaîne de texte lisible cachée dans un fichier qui contient principalement des données binaires.

Pour t'aider :
Le mot de passe est présent en clair (ASCII) quelque part au milieu du fichier.

ℹ️ :
Trouve la commande pour extraire uniquement les séquences lisibles.

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
    niveau10.main()

if __name__ == '__main__':
    main()
