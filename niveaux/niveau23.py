# Script d'initialisation pour l'utilisateur niveau27

import os
import base64
import gzip
import CTF_lib
import niveau24

def main():
    NIVEAU = 23
    SUIVANT = 24

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
    contenu_readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Le mot de passe est là, caché… mais pas accessible immédiatement.\
Il est enfoui sous deux couches : une première d’encodage, puis une compression classique.\
À toi de démêler les protections, pour extraire le mot brut, celui qui t’ouvrira la porte du niveau suivant.

Pour t'aider :
Tu disposes d’un fichier nommé donnees.mystere.\
Il ne contient pas directement le mot de passe, mais une version encodée en base64, puis compressée via un algorithme bien connu.\
Ta mission est simple : décoder, décompresser, révéler.

ℹ️ :
Commence par décoder le fichier base64 : tu obtiendras un contenu compressé.\
Ensuite, décompresse ce fichier en mémoire, sans l’écrire sur le disque.\
Tu verras alors le mot de passe apparaître en clair dans ton terminal.

Bonne chance, et n’oublie pas : Tu n’as pas besoin de forcer. Il suffit de décoder… et de libérer.\
Les données sont mystères, mais toi… tu es lucide. Ouvre simplement les 👀
"""
    chemin_readme = os.path.join(dossier, "readme")
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau24.main()

if __name__ == '__main__':
    main()
