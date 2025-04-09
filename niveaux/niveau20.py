# Script d'initialisation pour l'utilisateur niveau22

import os
import CTF_lib
import niveau21
import hashlib

def main():
    NIVEAU = 20
    SUIVANT = 21

    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Hash md5 de la string "I am user niveau21"
    phrase = f"I am user niveau{SUIVANT}"
    hash_target = hashlib.md5(phrase.encode()).hexdigest()
    chemin_tmp = f"/tmp/{hash_target}"

    # Script cron
    script_path = f"/usr/bin/cronjob_niveau{SUIVANT}.sh"
    with open(script_path, "w") as f:
        f.write(f"""#!/bin/bash

mytarget=$(echo I am user niveau{SUIVANT} | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/niveau_mdps/niveau{SUIVANT} to /tmp/$mytarget"
cat /etc/niveau_mdps/niveau{SUIVANT} > /tmp/$mytarget
chmod 644 /tmp/$mytarget
""")
    os.system(f"chmod 755 {script_path}")
    os.system(f"chown root:root {script_path}")

    # Cron
    cron_path = f"/etc/cron.d/cronjob_niveau{SUIVANT}"
    with open(cron_path, "w") as f:
        f.write(f"""* * * * * niveau{SUIVANT} {script_path} &> /dev/null
""")
    os.system(f"chmod 644 {cron_path}")
    os.system(f"chown root:root {cron_path}")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Retrouver un fichier temporaire généré par un cron job à partir d’un hash md5.

Pour t'aider :
Le script cron utilise 'whoami' 

ℹ️ :
Trouve la bonne commande

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
    niveau21.main()

if __name__ == '__main__':
    main()
