# Script d'initialisation pour l'utilisateur niveau2 et configuration de l'environnement du niveau 2

import os
import niveaux.CTF_lib as CTF_lib
import niveaux.niveau3 as niveau3

def main():
    NIVEAU = 2

    # Crée et configure l'utilisateur niveau2 et récupère son mot de passe
    mdp = CTF_lib.ajout_utilisateur(NIVEAU)

    # Création d'un fichier spécial dans le répertoire personnel de niveau2 contenant le mot de passe
    os.system("touch /home/niveau2/-")
    os.system(f"echo '{mdp}' >> /home/niveau2/-")
    os.system("chown niveau2:niveau2 /home/niveau2/-")
    os.system("chmod 640 /home/niveau2/-")

    # Restreint l'accès du répertoire personnel de l'utilisateur niveau2
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Passe à la configuration du niveau suivant
    niveau3.main()

if __name__ == '__main__':
    main()