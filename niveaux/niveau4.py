# Script d'initialisation pour l'utilisateur niveau4

import os
import random
import CTF_lib
import niveau5

def main():
    NIVEAU = 4
    SUIVANT = 5

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
    contenu_readme = f"""\
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Retrouve le bon fichier dans le bon dossier. Un seul contient un mot de passe lisible.

Pour t'aider :
Certains fichiers semblent illisibles ou contiennent des données étranges… \
Ne te laisse pas piéger. Le mot de passe est caché dans le seul fichier lisible du dossier inhere. \

ℹ️ :
Essaie d’identifier le type de contenu de chaque fichier.\
Mais attention...Les fichiers texte ont quelque chose d'assez inabituel…\
Si ton terminal fait des siennes, pense à utiliser la commande magique : reset.

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
    niveau5.main()

if __name__ == '__main__':
    main()
