# Script d'initialisation pour l'utilisateur niveau23

import os
import CTF_lib
import niveau24

def main():
    NIVEAU = 23
    SUIVANT = 24

    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Dossier surveillé
    spool_path = f"/var/spool/niveau{SUIVANT}"
    os.makedirs(spool_path, exist_ok=True)
    os.system(f"chown niveau{SUIVANT}:niveau{SUIVANT} {spool_path}")
    os.system(f"chmod 733 {spool_path}")  # accès pour déposer des fichiers

    # Script cron à exécuter
    cron_script = "/usr/bin/cronjob_bandit24.sh"
    with open(cron_script, "w") as f:
        f.write(f"""#!/bin/bash
myname=$(whoami)
cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        timeout -s 9 60 ./$i
        rm -f ./$i
    fi
done
""")
    os.system(f"chmod 755 {cron_script}")
    os.system(f"chown root:root {cron_script}")

    # Cron config
    cron_path = "/etc/cron.d/cronjob_bandit24"
    with open(cron_path, "w") as f:
        f.write(f"""* * * * * niveau{SUIVANT} {cron_script} &> /dev/null
""")
    os.system(f"chmod 644 {cron_path}")
    os.system(f"chown root:root {cron_path}")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Placer un script dans un dossier spécial, pour qu’un cron l’exécute automatiquement et copie un mot de passe ailleurs.

Pour t'aider :
Tous les fichiers dans /var/... sont exécutés une fois par minute, puis supprimés.

ℹ️ :
Crée un script comme celui-ci.

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
    niveau24.main()

if __name__ == '__main__':
    main()
