# Script d'initialisation pour l'utilisateur niveau28

import os
import CTF_lib
import niveau25

def main():
    NIVEAU = 24
    SUIVANT = 25

    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    dossier = f"/home/niveau{NIVEAU}"

    # Groupe spécial
    groupe = f"mdplevel{NIVEAU}"
    os.system(f"groupadd -f {groupe}")
    os.system(f"usermod -a -G {groupe} niveau{NIVEAU}")

    # Fichier avec droits de groupe uniquement
    chemin_fichier = os.path.join(dossier, "acces_groupe.txt")
    with open(chemin_fichier, "w") as f:
        f.write(mdp_suivant + "\n")

    os.system(f"chown root:{groupe} {chemin_fichier}")
    os.system(f"chmod 640 {chemin_fichier}")  # -rw-r-----

    # Readme
    contenu_readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Un fichier t’attend… mais à première vue, il n’est pas à toi. Pas de panique : ici, ce n’est pas une question de propriété, mais d’appartenance.\
Tu n’es pas le propriétaire du fichier, mais tu fais partie d’un groupe bien précis… et ce groupe a les clés.\
Ton but? Lire ce fichier.

Pour t'aider :
Le fichier acces_groupe.txt est protégé par les droits UNIX classiques : propriétaire, groupe, autres.\
Tu ne peux pas l’ouvrir comme ça, sauf que… tu fais partie du groupe qui a le droit de le lire.\
Il te suffit de le comprendre, et de l’assumer.

ℹ️ :
Observe bien les droits du fichier.\
Regarde à qui il appartient, et surtout quel groupe a les droits de lecture.\
Vérifie que tu appartiens à ce groupe, et tu pourras lire le fichier en toute légitimité.

Bonne chance, et n’oublie pas : Tu n’as pas besoin d’être le propriétaire.\
Tu fais partie de la famille.\
Regarde les droits. Regarde ton groupe. Et ouvre les 👀
"""
    chemin_readme = os.path.join(dossier, "readme")
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau25.main()

if __name__ == '__main__':
    main()
