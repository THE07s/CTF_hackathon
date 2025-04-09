# Script d'initialisation pour l'utilisateur niveau22

import os
import CTF_lib
import niveau21
import hashlib

def main():
    NIVEAU = 20
    SUIVANT = 21

    MYTARGET = f"$(echo I am user niveau{SUIVANT} | md5sum | cut -d ' ' -f 1)"

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
echo "Copying passwordfile /etc/niveau_mdps/niveau{SUIVANT} to /tmp/{MYTARGET}"
cat /etc/niveau_mdps/niveau{SUIVANT} > /tmp/{MYTARGET}
chmod 644 /tmp/{MYTARGET}
""")
    os.system(f"chmod 755 {script_path}")
    os.system(f"chown root:root {script_path}")

    # Cron
    cron_path = f"/etc/cron.d/cronjob_niveau{SUIVANT}"
    with open(cron_path, "w") as f:
        f.write(f"""* * * * * root {script_path} &> /dev/null
""")
    os.system(f"chmod 644 {cron_path}")
    os.system(f"chown root:root {cron_path}")

    # Fichier readme
    contenu_readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Le mot de passe que tu cherches est bien là… mais son fichier est masqué. Il ne porte pas un nom classique : il est généré à partir d’un hash.\
Ton rôle ici? C'est de retrouver ce fichier temporaire.\
Ce niveau te met face à une énigme logique. Pas de hasard. Juste de la précision, et une touche de cryptographie.

Pour t'aider :
Le script planifié que tu as analysé précédemment crée un fichier dans /tmp.\
Mais pas avec un nom simple : il utilise une fonction de hachage, à partir d’une chaîne de texte construite dynamiquement, et qui inclut une commande système bien connue…

ℹ️ :
Le nom du fichier est le résultat d’un hash md5\
La phrase hashée inclut le nom de l’utilisateur cible, inséré dynamiquement via une commande (whoami)\
Reproduis exactement la chaîne utilisée dans le script, applique le bon hachage, puis cherche le fichier dans /tmp/

Bonne chance, et n’oublie pas : Ce n’est pas un fichier caché. C’est un fichier chiffré… dans son nom.\
Reconstitue la formule. Dévoile le nom. Ouvre les 👀. 
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
