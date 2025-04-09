# Script d'initialisation pour l'utilisateur niveau21

import os
import CTF_lib
import niveau20
import string
import random
import hashlib

def main():
    NIVEAU = 19
    SUIVANT = 20

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Chemins utiles
    script_path = f"/usr/bin/cronjob_niveau{SUIVANT}.sh"
    cron_path = f"/etc/cron.d/cronjob_niveau{SUIVANT}"
    tmp_file = f"/tmp/{generer_nom_temp()}"

    # Script bash exécuté par le cron
    with open(script_path, "w") as f:
        f.write(f"""#!/bin/bash
echo '{mdp_suivant}' > {tmp_file}
chmod 644 {tmp_file}
""")
    os.system(f"chown root:root {script_path}")
    os.system("chmod 755 " + script_path)

    # Fichier de cron (exécution chaque minute)
    with open(cron_path, "w") as f:
        f.write(f"""* * * * * niveau{SUIVANT} {script_path} &> /dev/null
""")
    os.system(f"chown root:root {cron_path}")
    os.system("chmod 644 " + cron_path)

    # Fichier readme
    contenu_readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Un mot de passe est généré automatiquement par un processus planifié.\
Il est stocké temporairement, puis écrasé. \
Ton but, cette fois, n’est pas encore de le lire… mais de remonter à la source : le script responsable de sa création.

Pour t'aider :
Un cron job s’exécute chaque minute pour l’utilisateur du niveau suivant.\
Il lance un script précis, placé dans un coin stratégique du système.\
Si tu veux retrouver le mot de passe plus tard, tu dois d’abord comprendre exactement ce que ce script fait.

ℹ️ :
Localise le script lancé par le cron job.\
Ouvre-le et analyse son contenu.\
Repère les chemins, les commandes, les noms de fichiers générés…\
Tu es ici pour observer, pas encore pour agir.

Bonne chance, et n’oublie pas : Le vrai hacker ne fonce pas tête baissée. Il lit. Il comprend. Il anticipe.\
Le fichier temporaire viendra après… mais pour l’instant, ouvre les yeux… et le script. 👀📜
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau20.main()

def generer_nom_temp():
    return hashlib.md5("I am user niveau20".encode()).hexdigest()

if __name__ == '__main__':
    main()
