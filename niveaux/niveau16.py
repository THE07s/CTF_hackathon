# Script d'initialisation pour l'utilisateur niveau17

import os
import random
import CTF_lib
import niveau17
import string


def main():
    NIVEAU = 16
    SUIVANT = 17

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
    contenu_readme = f"""\
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Deux fichiers. Deux listes. Deux versions d’un même secret… mais quelque chose a changé.\
Ton rôle ? Trouver l’intrus. L’élément nouveau. Le mot interdit qui s’est glissé dans la liste.\
Ce mot unique, c’est le mot de passe du prochain niveau.

Pour t'aider :
Tu disposes de deux fichiers : l’un est l’ancienne version, l’autre la nouvelle.\
Ils se ressemblent presque à la perfection. Mais une seule ligne a été ajoutée.\
Une seule différence. C’est elle que tu dois repérer. Elle seule t’ouvrira la voie.

ℹ️ :
Oublie la recherche visuelle. Ce serait trop long, trop risqué.\
Tu dois comparer les deux fichiers, ligne par ligne, avec précision chirurgicale. \
Cherche ce qui existe dans le nouveau fichier mais pas dans l’ancien.\
Tu verras : la différence est là, tapie dans l’ombre… mais visible à celui ou celle qui sait observer avec méthode.

Bonne chance, et n’oublie pas : Une seule ligne. Un seul mot. Et un nouveau niveau s’ouvre.\
Garde ton sang-froid, et ouvre grand les 👀🧠🕶️📜
"""
    chemin_readme = os.path.join(dossier, "readme")
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer le niveau suivant
    niveau17.main()

def generer_ligne():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

if __name__ == '__main__':
    main()
