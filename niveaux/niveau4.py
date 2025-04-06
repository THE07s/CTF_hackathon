# Script d'initialisation pour l'utilisateur niveau4

import os
import random
import CTF_lib
import niveau5

def main():
    NIVEAU = 4
    SUIVANT = 5

    # Crée l'utilisateur niveau4
    CTF_lib.ajout_utilisateur(NIVEAU)

    # Génère et enregistre le mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Création du dossier jeSuisLa
    dossier_jeSuisLa = f"/home/niveau{NIVEAU}/jeSuisLa"
    os.makedirs(dossier_jeSuisLa, exist_ok=True)

    # Fichier contenant le bon mot de passe (randomisé)
    index_correct = random.randint(0, 9)

    for i in range(10):
        nom_fichier = f"{dossier_jeSuisLa}/-fichier0{i}"
        if i == index_correct:
            with open(nom_fichier, "w") as f:
                f.write(mdp_suivant + "\n")
        else:
            with open(nom_fichier, "wb") as f:
                f.write(os.urandom(32))  # Données binaires
        os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{nom_fichier}'")
        os.system(f"chmod 640 '{nom_fichier}'")

    os.system(f"chown -R niveau{NIVEAU}:niveau{NIVEAU} {dossier_jeSuisLa}")
    os.system(f"chmod 700 {dossier_jeSuisLa}")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Retrouver le bon fichier parmi dix, dans un dossier appelé 'jeSuisLa'. Un seul contient un mot de passe lisible.

Pour t'aider :
Certains fichiers ne sont pas lisibles directement, ou contiennent du contenu illisible.

ℹ️ :
Essaie la commande 'file' pour détecter le type de contenu d’un fichier. Les fichiers texte sont en ASCII.

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
    niveau5.main()

if __name__ == '__main__':
    main()
