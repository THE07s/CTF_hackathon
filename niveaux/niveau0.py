# Script d'initialisation pour l'utilisateur niveau0

import niveaux.CTF_lib as CTF_lib
import niveaux.niveau1 as niveau1

def main():
    NIVEAU = 0

    # Crée et configure l'utilisateur bandito0 (ajoute l'utilisateur, écrit le mot de passe, configure SSH et Bash)
    CTF_lib.ajout_utilisateur(NIVEAU)

    # Restreint les permissions du répertoire personnel
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Passe à la configuration du niveau suivant
    niveau1.main()

if __name__ == '__main__':
    main()
