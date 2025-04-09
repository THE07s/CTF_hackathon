# Script d'initialisation pour l'utilisateur niveau6

import os
import random
import CTF_lib
import niveau7

def main():
    NIVEAU = 6
    SUIVANT = 7

    # Génère et enregistre le mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Dossier système "random" pour planquer le fichier
    dossier_secret = "/var/lib/ctf"
    os.makedirs(dossier_secret, exist_ok=True)

    # Fichier caché système
    chemin_fichier = f"{dossier_secret}/niveau{SUIVANT}.password"
    with open(chemin_fichier, "w") as f:
        f.write(mdp_suivant[:32] + "\n")  # 33 caractères = 32 + newline
    os.system(f"chown niveau{SUIVANT}:niveau{NIVEAU} {chemin_fichier}")
    os.system(f"chmod 640 {chemin_fichier}")

    # Fichier readme explicatif
    contenu_readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Un fichier mystère contenant le mot de passe du prochain niveau est caché quelque part dans les méandres du système… \
À toi de le retrouver.\
Et rappelle toi...Ce n’est pas qu’un simple fichier — c’est la clé vers la suite de ton aventure !

Pour t'aider :
Ce que tu cherches a toutes ces caractéristiques :\
Il est possédé par l’utilisateur bandit7\
Il appartient au groupe bandit6\
Il fait exactement 33 octets\
Mais ce fichier...est-ce qu'il t'appartient🤔?? Peut-être pas😱...\
Essaie de démêler le vrai du faux et tu découvriras ce qui est à toi et ce qui ne l'est pas.

ℹ️ :
Il existe une commande précise entre ls, cd, cat, file, du, find, grep, pour t'aider à traquer ce genre de fichier.\
Il faut vite la trouver parce qu'elle sera ton alliée...


Bonne chance, et n’oublie pas : ce qui est caché ne veut pas toujours être retrouvé alors ouvre grands les 👀
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
