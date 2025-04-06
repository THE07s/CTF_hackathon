# Script d'initialisation pour l'utilisateur niveau19

import os
import CTF_lib
import niveau20
import textwrap

def main():
    NIVEAU = 19
    SUIVANT = 20

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    dossier = f"/home/niveau{NIVEAU}"
    chemin_script = os.path.join(dossier, "bandit20-do")

    # Simuler un binaire : on fait un script bash avec setuid (chmod 4750)
    with open(chemin_script, "w") as f:
        f.write(textwrap.dedent(f"""\
            #!/bin/bash
            if [ $# -eq 0 ]; then
                echo "Usage: ./bandit20-do <commande>"
                exit 1
            fi
            CMD="$@"
            su -c "$CMD" - niveau{SUIVANT}
        """))

    os.system(f"chown root:niveau{NIVEAU} '{chemin_script}'")
    os.system(f"chmod 4750 '{chemin_script}'")  # SUID sur script bash

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Utiliser un programme spécial pour exécuter une commande en tant que l’utilisateur du niveau suivant.

Pour t'aider :
Trouve le programme et exécute le en tant que l’utilisateur niveau{SUIVANT}.

ℹ️ :
Trouve le mot de passe du niveau suivant, les mot de passe sont stokés dans /etc/...

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = os.path.join(dossier, "readme")
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_readme}'")
    os.system(f"chmod 640 '{chemin_readme}'")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer le niveau suivant
    niveau20.main()

if __name__ == '__main__':
    main()
