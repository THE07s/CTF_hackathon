# Script d'initialisation pour l'utilisateur niveau3

import os
import CTF_lib
import niveau4

def main():
    NIVEAU = 3
    SUIVANT = 4

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
    contenu_readme = f"""\
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
 Il te faut trouver un fichier bien caché...\
 C'est lui qui referme le mot de passe pour accéder au niveau suivant. 

Pour t'aider :
Etrangement, tu ne le vois pas...Et pourtant, il est présent. \
Il est simplement discret, mais bien là.

ℹ️ :
Parmi les commandes: ls , cd , cat , file , du , find...seule une t'aidera à le faire apparaître

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
    niveau4.main()

if __name__ == '__main__':
    main()
