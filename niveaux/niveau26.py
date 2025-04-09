# Script d'initialisation pour l'utilisateur niveau33

import os
import CTF_lib

def main():
    NIVEAU = 26
    dossier = f"/home/niveau{NIVEAU}"

    # Message de fin uniquement
    contenu_readme = f"""🎉 Bienvenue dans le niveau {NIVEAU} du CTF hackathon 🎉

🥳 Bravo ! Tu es arrivé au bout du CTF hackathon, en complétant les {NIVEAU + 1} niveaux.
Tu as démontré des compétences solides, de la curiosité et une belle persévérance.

🎓 Tu repars avec :
- Une meilleure maîtrise de Linux
- Une meilleure compréhension des failles courantes
- Une belle satisfaction personnelle 😎

Merci d’avoir joué ❤️

🐧 À bientôt pour de nouveaux défis !
"""
    readme_path = os.path.join(dossier, "readme")
    with open(readme_path, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {readme_path}")
    os.system(f"chmod 640 {readme_path}")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Afficher dans le terminal les mots de passe de tous les niveaux 0 à 33
    print(f"\n=== Liste des mots de passe (niveau 0 à {NIVEAU + 1}) ===")
    for niv in range(0, NIVEAU + 1):
        chemin_mdp = f"/etc/niveau_mdps/niveau{niv}"
        try:
            with open(chemin_mdp, "r") as f:
                mdp = f.read().strip()
            print(f"Niveau {niv} : {mdp}")
        except Exception as e:
            print(f"Erreur lors de la lecture du niveau {niv} : {e}")

if __name__ == '__main__':
    main()
