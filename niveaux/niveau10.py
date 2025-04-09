# Script d'initialisation pour l'utilisateur niveau10

import os
import base64
import CTF_lib
import niveau11

def main():
    NIVEAU = 10
    SUIVANT = 11

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Encodage en base64
    encoded = base64.b64encode(mdp_suivant.encode()).decode()

    # Écriture du fichier
    chemin_fichier = f"/home/niveau{NIVEAU}/data.txt"
    with open(chemin_fichier, "w") as f:
        f.write(encoded + "\n")

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_fichier}'")
    os.system(f"chmod 640 '{chemin_fichier}'")

    # Fichier readme
    contenu_readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Un fichier codé t’attend. Il contient le mot de passe du prochain niveau, soigneusement dissimulé dans le fichier data.txt et sous une forme que seuls les initiés sauront déchiffrer…\
À toi de percer ce voile et de révéler le message caché.\
Prêt pour une nouvelle aventure ? Alors, en avant !


Pour t'aider :
Ce n’est pas du charabia au hasard : le mot de passe est encodé dans un format très utilisé pour transmettre des données. \
Autrement dit : il y a une logique, une structure… et une faille.\
Comment la trouver ? C’est simple : il suffit de se pencher sur le fichier et de l’examiner de plus près.\
Commence par identifier le type d’encodage. Puis, avec la bonne commande, transforme ces symboles en texte clair. \
Le mot de passe apparaîtra alors sous tes yeux comme une révélation.

ℹ️ :
Le fichier data.txt contient des données encodées en base64.\
À toi de les décoder pour libérer le mot magique.\
Les commandes utiles pour ce niveau sont: grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

Bonne chance, et n’oublie pas : tu n’as qu’un obstacle entre toi et la suite de ton aventure : une énigme chiffrée. \
Sois précis·e, rapide, et surtout…garde les yeux grands ouverts 👀.
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau11.main()

if __name__ == '__main__':
    main()
