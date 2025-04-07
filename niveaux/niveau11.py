# Script d'initialisation pour l'utilisateur niveau11

import os
import codecs
import CTF_lib
import niveau12

def main():
    NIVEAU = 11
    SUIVANT = 12

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Chiffrement ROT13
    mdp_rot13 = codecs.encode(mdp_suivant, 'rot_13')

    # Écriture dans data.txt
    chemin_fichier = f"/home/niveau{NIVEAU}/data.txt"
    with open(chemin_fichier, "w") as f:
        f.write(mdp_rot13 + "\n")

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_fichier}'")
    os.system(f"chmod 640 '{chemin_fichier}'")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Retrouver le mot de passe à partir d’une version chiffrée présente dans un fichier.

Pour t'aider :
Le chiffrement utilisé est un simple décalage de 13 lettres dans l’alphabet : le ROT13.

ℹ️ :
Trouve la commande 😈.

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
    niveau12.main()

if __name__ == '__main__':
    main()
