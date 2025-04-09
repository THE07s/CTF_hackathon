# Script d'initialisation pour l'utilisateur niveau32

import os
import CTF_lib
import niveau26

def main():
    NIVEAU = 25
    SUIVANT = 26

    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)

    # Fichier de log global
    log_path = "/var/log/hackathon.log"
    os.makedirs("/var/log", exist_ok=True)

    # Fichier log avec mot de passe enregistré dedans
    with open(log_path, "a") as f:
        f.write(f"[INFO] Tentative de connexion utilisateur: niveau{SUIVANT}, mot de passe essayé: {mdp_suivant}\n")

    os.system(f"chown root:niveau{NIVEAU} {log_path}")
    os.system(f"chmod 640 {log_path}")

    # Fichier readme
    readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Analyser les logs système pour retrouver un mot de passe écrit accidentellement.

Pour t'aider :
Un script de journalisation loggue toutes les connexions utilisateur quelque-part.

ℹ️ :
Regarde dans ce fichier pour y trouver une ligne suspecte…

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    readme_path = f"/home/niveau{NIVEAU}/readme"
    with open(readme_path, "w") as f:
        f.write(readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {readme_path}")
    os.system(f"chmod 640 {readme_path}")

    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau26.main()

if __name__ == '__main__':
    main()
