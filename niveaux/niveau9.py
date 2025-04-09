# Script d'initialisation pour l'utilisateur niveau9

import os
import random
import CTF_lib
import niveau10

def main():
    NIVEAU = 9
    SUIVANT = 10

    # Le mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    chemin_fichier = f"/home/niveau{NIVEAU}/data.txt"
    with open(chemin_fichier, "wb") as f:
        f.write(os.urandom(1024))                          # Données binaires avant
        f.write(b"\n" + mdp_suivant.encode() + b"\n")      # Chaîne ASCII (le mot de passe)
        f.write(os.urandom(1024))                          # Données binaires après

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_fichier}'")
    os.system(f"chmod 640 '{chemin_fichier}'")

    # Fichier readme
    contenu_readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Plongé·e au cœur d’un fichier bourré de données binaires, tu dois accomplir l’impossible : repérer une minuscule étincelle de clarté dans le chaos.\
Quelque part dans cette masse obscure se cache le mot de passe. Il est là. En clair. Il t’attend.\
Qu'est-ce qu'on sait?\
Une chaîne lisible est tapie dans l’ombre… précédée par plusieurs signes égal (=).\
Elle est unique, précieuse, et surtout : c’est elle qui te propulsera vers le prochain niveau.

Pour t'aider :
Il existe une commande capable de faire parler les fichiers les plus silencieux. \
Une commande qui révèle les morceaux de texte cachés dans les profondeurs binaires.
Utilise-la. Filtre avec précision. Et ouvre l’œil : ta clé est juste là, camouflée dans un océan de bruit.\
Qu'est-ce qui peut t'aider à la débusquer?\
🔸 Le mot de passe est dans le fichier data.txt
🔸 Il est lisible en ASCII, enfoui au milieu des données binaires
🔸 Il est précédé de plusieurs =

ℹ️ :
Les commandes à ta disposition sont: grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

Bonne chance, et n’oublie pas : Fais appel à ton instinct, à ta logique, à ta ruse.\
Ce n’est pas qu’un simple mot… c’est ta prochaine victoire.\
Trouve-le. Gagne. Et surtout… ouvre grand les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau10.main()

if __name__ == '__main__':
    main()
