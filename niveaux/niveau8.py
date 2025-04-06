# Script d'initialisation pour l'utilisateur niveau8

import os
import random
import CTF_lib
import niveau9

def main():
    NIVEAU = 8
    SUIVANT = 9

    # Le mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Générer un fichier avec plein de mots, tous en double sauf un (le mot de passe)
    chemin_fichier = f"/home/niveau{NIVEAU}/data.txt"
    mots = []

    # Ajout de 1000 mots en double
    for _ in range(1000):
        mot = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8))
        mots.extend([mot, mot])

    # Ajout du mot de passe une seule fois
    mots.append(mdp_suivant)
    random.shuffle(mots)

    with open(chemin_fichier, "w") as f:
        f.write("\n".join(mots) + "\n")

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_fichier}'")
    os.system(f"chmod 640 '{chemin_fichier}'")

    # Fichier readme explicatif
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Retrouver un mot unique dans une grande liste de mots contenus dans un fichier.

Pour t'aider :
Un seul mot est présent une seule fois dans tout le fichier. Tous les autres sont en double.

ℹ️ :
Trie le fichier puis filtre pour repérer la ligne unique.

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
    niveau9.main()

if __name__ == '__main__':
    main()
