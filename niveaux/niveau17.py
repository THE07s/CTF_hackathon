# Script d'initialisation pour l'utilisateur niveau17

import os
import random
import CTF_lib
import niveau18
import string


def main():
    NIVEAU = 17
    SUIVANT = 18

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    dossier = f"/home/niveau{NIVEAU}"
    lignes = []

    # Générer 50 lignes factices
    for _ in range(50):
        lignes.append(generer_ligne())

    # On choisit une ligne à remplacer
    index_modif = random.randint(5, 45)
    old_lines = lignes.copy()
    new_lines = lignes.copy()
    new_lines[index_modif] = mdp_suivant

    # Écriture des fichiers
    with open(os.path.join(dossier, "passwords.old"), "w") as f:
        f.write("\n".join(old_lines) + "\n")

    with open(os.path.join(dossier, "passwords.new"), "w") as f:
        f.write("\n".join(new_lines) + "\n")

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {dossier}/passwords.*")
    os.system(f"chmod 640 {dossier}/passwords.*")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Identifier une modification entre deux fichiers pour récupérer le mot de passe du niveau suivant.

Pour t'aider :
2 fichiers sont presque identiques, à une chose prêt.

ℹ️ :
Utilise une commande pour repérer la différence.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = os.path.join(dossier, "readme")
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer le niveau suivant
    niveau18.main()

def generer_ligne():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

if __name__ == '__main__':
    main()
