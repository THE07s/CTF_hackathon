# Script d'initialisation pour l'utilisateur niveau3 et configuration de l'environnement du niveau3

import os
import CTF_lib as CTF_lib
import niveau4 as niveau4

def main():
    NIVEAU = 3

    # Crée et configure l'utilisateur "niveau3", récupère son mot de passe
    mdp = CTF_lib.ajout_utilisateur(NIVEAU)

    # Création d'un fichier spécial (nom commençant par "-") dans le répertoire personnel de niveau3 contenant le mot de passe
    os.system(f"touch /home/niveau{NIVEAU}/-")
    os.system(f"echo '{mdp}' >> /home/{NIVEAU - 1}/-")
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} /home/niveau{NIVEAU}/-")
    os.system(f"chmod 640 /home/niveau{NIVEAU}/-")
    
    # Restreint l'accès du répertoire personnel de l'utilisateur niveau3
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Passe à la configuration du niveau suivant
    niveau4.main()

if __name__ == '__main__':
    main()