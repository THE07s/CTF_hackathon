# Script d'initialisation pour l'utilisateur niveau21

import os
import CTF_lib
import niveau22
import string
import random

def main():
    NIVEAU = 21
    SUIVANT = 22

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Chemins utiles
    script_path = "/usr/bin/cronjob_bandit22.sh"
    cron_path = "/etc/cron.d/cronjob_bandit22"
    tmp_file = f"/tmp/{generer_nom_temp()}"

    # Script bash exécuté par le cron
    with open(script_path, "w") as f:
        f.write(f"""#!/bin/bash
chmod 644 {tmp_file}
echo '{mdp_suivant}' > {tmp_file}
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
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Trouver un mot de passe laissé temporairement dans un fichier, généré automatiquement par une tâche planifiée.

Pour t'aider :
Un cron job s'exécute toutes les minutes pour l’utilisateur niveau{SUIVANT}.

ℹ️ :
Cherche dans le bon dossier et vois ce que contient le script lancé

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau22.main()

def generer_nom_temp():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

if __name__ == '__main__':
    main()
