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
    readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Le mot de passe du niveau suivant n’a pas été protégé…
Il a été inscrit par erreur dans un fichier de log système, comme une trace oubliée d’un passage furtif. \
À toi de la retrouver.\
Tu vas devoir jouer le rôle du cyber-enquêteur : fouiller les journaux, analyser, extraire… et révéler ce qui aurait dû rester caché.

Pour t'aider :
Un script de journalisation (log) enregistre chaque connexion utilisateur. \
Quelqu’un a laissé échapper un mot de passe.\
Ce mot figure dans une ligne liée à l’utilisateur niveau26.\
Mais le log ne se lit pas comme un livre : tu devras filtrer, découper, nettoyer pour extraire le mot exact.

ℹ️ :
Regarde dans le bon fichier de logs système.\
Cherche les lignes associées à niveau26.\
Une fois la ligne trouvée, extrais précisément la partie contenant le mot de passe.\
Il peut être caché derrière un délimiteur, ou entouré d’espaces : fais le ménage.

Bonne chance, et n’oublie pas : Les logs ne mentent jamais… mais ils ne crient pas non plus.\
Écoute bien, lis entre les lignes, et ouvre les 👀
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
