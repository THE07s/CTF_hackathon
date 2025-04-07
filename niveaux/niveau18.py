# Script d'initialisation pour l'utilisateur niveau18

import os
import CTF_lib
import niveau19

def main():
    NIVEAU = 18
    SUIVANT = 19

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)

    dossier_home = f"/home/niveau{NIVEAU}"
    chemin_readme = os.path.join(dossier_home, "readme")
    with open(chemin_readme, "w") as f:
        f.write(mdp_suivant + "\n")

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_readme}'")
    os.system(f"chmod 640 '{chemin_readme}'")

    # Forcer un exit uniquement si aucune commande n'est fournie via SSH
    chemin_bashrc = os.path.join(dossier_home, ".bashrc")
    with open(chemin_bashrc, "w") as f:
        f.write('''if [ -z "$SSH_ORIGINAL_COMMAND" ]; then
    exit
fi
''')
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_bashrc}'")
    os.system(f"chmod 644 '{chemin_bashrc}'")

    # Fichier explicatif
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Exécuter une commande sur une session SSH même si le shell se ferme immédiatement.

Pour t'aider :
Le fichier contient le mot de passe du niveau suivant, mais tu ne peux pas interagir normalement avec le shell.

ℹ️ :
Essaie d'exécuter une commande avec SSH.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_explication = os.path.join(dossier_home, "instructions")
    with open(chemin_explication, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_explication}'")
    os.system(f"chmod 640 '{chemin_explication}'")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau19.main()

if __name__ == '__main__':
    main()
