# Script d'initialisation pour l'utilisateur niveau1

import os
import CTF_lib as CTF_lib
import niveau2 as niveau2

def main():
    NIVEAU = 1

    # Génère le mot de passe et crée l'utilisateur niveau1
    mdp = CTF_lib.ajout_utilisateur(NIVEAU)

    # Création d'un fichier readme contenant le mot de passe pour le niveau 1
    os.system(f"touch /home/niveau{NIVEAU}/readme")
    os.system(f"echo '{mdp}' >> /home/niveau{NIVEAU - 1}/readme")
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} /home/niveau{NIVEAU}/readme")
    os.system(f"chmod 640 /home/niveau{NIVEAU}/readme")

    # Restreint les permissions du répertoire personnel
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Passe à la configuration du niveau suivant
    niveau2.main()

if __name__ == '__main__':
    main()