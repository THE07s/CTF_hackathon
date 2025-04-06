# Script d'initialisation pour l'utilisateur niveau6

import os
import random
import CTF_lib
import niveau7

def main():
    NIVEAU = 6
    SUIVANT = 7

    # Crée l'utilisateur niveau6
    CTF_lib.ajout_utilisateur(NIVEAU)

    # Génère et enregistre le mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Dossier système "random" pour planquer le fichier
    dossier_secret = "/var/lib/ctf"
    os.makedirs(dossier_secret, exist_ok=True)

    # Fichier caché système
    chemin_fichier = f"{dossier_secret}/niveau7.password"
    with open(chemin_fichier, "w") as f:
        f.write(mdp_suivant[:32] + "\n")  # 33 caractères = 32 + newline
    os.system(f"chown niveau{SUIVANT}:niveau{NIVEAU} {chemin_fichier}")
    os.system(f"chmod 640 {chemin_fichier}")

    # Fichier readme explicatif
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Retrouver un fichier contenant le mot de passe du niveau suivant. Ce fichier est bien caché quelque part dans le système.

Pour t'aider :
Ce fichier t'appartient partiellement : il est accessible grâce aux permissions de groupe.

ℹ️ :
Utilise la commande 'find' avec les options -user niveau7 -group niveau6 -size 33c pour le dénicher. Et redirige les erreurs si besoin avec '2>/dev/null'.

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
    niveau7.main()

if __name__ == '__main__':
    main()
