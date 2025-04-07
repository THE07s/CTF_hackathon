# Script d'initialisation pour l'utilisateur niveau27

import os
import base64
import gzip
import CTF_lib
import niveau28

def main():
    NIVEAU = 27
    SUIVANT = 28

    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    dossier = f"/home/niveau{NIVEAU}"
    chemin_final = os.path.join(dossier, "donnees.mystere")

    # Étape 1 : écrire le mot de passe dans un fichier .gz
    gzip_path = "/tmp/temp.gz"
    with gzip.open(gzip_path, "wb") as f:
        f.write(mdp_suivant.encode())

    # Étape 2 : encoder en base64
    with open(gzip_path, "rb") as f:
        contenu_binaire = f.read()
    encodage = base64.b64encode(contenu_binaire)

    # Étape 3 : écrire le fichier final
    with open(chemin_final, "wb") as f:
        f.write(encodage)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_final}")
    os.system(f"chmod 640 {chemin_final}")

    # Nettoyage
    os.remove(gzip_path)

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Décoder un fichier compressé et encodé en base64 pour obtenir le mot de passe du niveau suivant.

Pour t'aider :
Un fichier contient le mot de passe, mais il est encodé et compressé.

ℹ️ :
trouve une commande pour décompresser.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = os.path.join(dossier, "readme")
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau28.main()

if __name__ == '__main__':
    main()
