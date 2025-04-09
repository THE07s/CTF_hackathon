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
    contenu_readme = f"""\
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif: 
Tu dois décrypter et récupérer un message codé.
C'est un mot de passe, prisonnier d’un vieux sortilège numérique : le ROT13 qui transforme les mots…tout en les gardant à portée d’œil.
À toi de briser le charme et de révéler ce qui se cache dessous.\
Dévoile le message et entre dans le niveau suivant en conquérant.

Pour t'aider :
Le fichier data.txt contient le mot de passe, mais il est déguisé.
Chaque lettre, qu’elle soit minuscule ou majuscule, a été décalée de 13 positions dans l’alphabet.
Ce n’est pas complexe. Mais il faut savoir où appuyer pour que tout s’aligne.

ℹ️ :
Une seule commande peut tout faire basculer. Une commande simple… mais puissante.
Trouve-la, et le vrai texte se révélera à toi.\
Aide toi des commandes suivantes: grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

Bonne chance, et n’oublie pas : ouvre les 👀 et retourne les lettres!
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
