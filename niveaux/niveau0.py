# Script d'initialisation pour l'utilisateur niveau0

import os
import CTF_lib
import niveau1

def main():
    NIVEAU = 0
    SUIVANT = 1

    # Génère le mot de passe du niveau suivant et l'enregistre
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Création du fichier readme avec instructions
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Comme tu l'as fais, tu dois lire le contenu de différents fichiers pour découvrir le mot de passe du niveau suivant.

Pour t'aider :
Tu es dans ton répertoire personnel. Un ou plusieurs fichiers s'y trouveront, et ils contiendront ce dont tu as besoin...

ℹ️ :
Utilise des commandes "simples" pour afficher le contenu d’un fichier texte.

Bonne chance, et n’oublie pas : ouvre les 👀

À chaque niveau, vous trouverez un fichier readme pour vous aider

Mot de passe : {mdp_suivant}
"""
    chemin_fichier = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_fichier, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_fichier}")
    os.system(f"chmod 640 {chemin_fichier}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Passe au niveau suivant
    niveau1.main()

if __name__ == '__main__':
    main()
