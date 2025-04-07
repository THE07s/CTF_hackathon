# Script d'initialisation pour l'utilisateur niveau31

import os
import CTF_lib
import niveau32

def main():
    NIVEAU = 31
    SUIVANT = 32

    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    script_path = "/usr/bin/niv32backup.sh"
    output_path = f"/home/niveau{NIVEAU}/leak.txt"

    # Script vulnérable simulant une race condition
    with open(script_path, "w") as f:
        f.write(f"""#!/bin/bash
if [ -f /tmp/backup ]; then
    cat /tmp/backup > {output_path}
fi
""")
    os.system(f"chmod 755 {script_path}")
    os.system(f"chown root:root {script_path}")

    # Cron : exécute toutes les minutes
    cron_path = "/etc/cron.d/cronjob_niv32backup"
    with open(cron_path, "w") as f:
        f.write(f"""* * * * * root {script_path} &> /dev/null
""")
    os.system(f"chmod 644 {cron_path}")
    os.system(f"chown root:root {cron_path}")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Profiter d’une race condition pour faire lire au système un fichier auquel tu n’as pas accès.

Pour t'aider :
Un script vérifie que /tmp/backup est un fichier normal, puis le copie dans ton home.

ℹ️ :
Sans commentaire...

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    readme_path = f"/home/niveau{NIVEAU}/readme"
    with open(readme_path, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {readme_path}")
    os.system(f"chmod 640 {readme_path}")

    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau32.main()

if __name__ == '__main__':
    main()
