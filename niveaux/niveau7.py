# Script d'initialisation pour l'utilisateur niveau7

import os
import random
import CTF_lib
import niveau8

def main():
    NIVEAU = 7
    SUIVANT = 8

    # Le mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Création d'un gros fichier texte avec du bruit
    chemin_fichier = f"/home/niveau{NIVEAU}/data.txt"
    lignes = []

    # Génère 10 000 lignes de bruit
    for _ in range(10000):
        bruit = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=32))
        lignes.append(bruit)

    # Insertion du mot de passe dans une ligne contenant le mot "millionth"
    index = random.randint(100, 9900)
    lignes[index] = f"millionth        {mdp_suivant}"

    with open(chemin_fichier, "w") as f:
        f.write("\n".join(lignes) + "\n")

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_fichier}'")
    os.system(f"chmod 640 '{chemin_fichier}'")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Trouver le mot de passe caché quelque part dans les différents fichiers.

Pour t'aider :
Ce fichier contient une ligne unique avec le mot 'millionth' suivi du mot de passe.

ℹ️ :
Utilise une commande pour trouver rapidement la bonne ligne.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lance le niveau suivant
    niveau8.main()

if __name__ == '__main__':
    main()
