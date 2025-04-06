# Script d'initialisation pour l'utilisateur niveau33

import os
import CTF_lib

def main():
    NIVEAU = 33
    dossier = f"/home/niveau{NIVEAU}"

    # Message de fin uniquement
    contenu_readme = f"""🎉 Bienvenue dans le niveau {NIVEAU} du CTF Hackaton 🎉

🥳 Bravo ! Tu es arrivé au bout du CTF Hackaton, en complétant les 33 niveaux.
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

if __name__ == '__main__':
    main()
