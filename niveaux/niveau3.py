# Script d'initialisation pour l'utilisateur niveau3

import os
import CTF_lib
import niveau4

def main():
    NIVEAU = 3
    SUIVANT = 4

    # Crée l'utilisateur niveau3
    CTF_lib.ajout_utilisateur(NIVEAU)

    # Génère et enregistre le mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Création du sous-dossier jeSuisLa et du fichier ...tuNeMeVoisPaaaas
    dossier_jeSuisLa = f"/home/niveau{NIVEAU}/jeSuisLa"
    os.makedirs(dossier_jeSuisLa, exist_ok=True)

    chemin_fichier = f"{dossier_jeSuisLa}/...tuNeMeVoisPaaaas"
    with open(chemin_fichier, "w") as f:
        f.write(mdp_suivant + "\n")
    os.system(f"chown -R niveau{NIVEAU}:niveau{NIVEAU} {dossier_jeSuisLa}")
    os.system(f"chmod 640 '{chemin_fichier}'")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Trouver un fichier caché. Ce fichier contient le mot de passe du niveau suivant.

Pour t'aider :
Ce fichier n’apparaît bizarrement pas. Il est discret, mais bien là.

ℹ️ :
Utilise une commande spéciale pour le faire apparaître.

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
    niveau4.main()

if __name__ == '__main__':
    main()
