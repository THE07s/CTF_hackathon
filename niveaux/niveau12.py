# Script d'initialisation pour l'utilisateur niveau12

import os
import subprocess
import CTF_lib
import niveau13

def main():
    NIVEAU = 12
    SUIVANT = 13

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    dossier_tmp = f"/tmp/bandito_lvl12"
    os.makedirs(dossier_tmp, exist_ok=True)

    current_file = os.path.join(dossier_tmp, "data.txt")
    with open(current_file, "w") as f:
        f.write(mdp_suivant)

    extensions = [".gz", ".bz2", ".tar", ".gz", ".tar", ".bz2", ".tar", ".gz"]
    for i, ext in enumerate(extensions):
        prev_file = current_file
        base = os.path.join(dossier_tmp, f"data{i}")
        current_file = base + ext

        if ext == ".gz":
            subprocess.run(["gzip", "-c", prev_file], stdout=open(current_file, "wb"))
        elif ext == ".bz2":
            subprocess.run(["bzip2", "-c", prev_file], stdout=open(current_file, "wb"))
        elif ext == ".tar":
            # On met le fichier dans une archive tar
            subprocess.run(["tar", "-cf", current_file, "-C", os.path.dirname(prev_file), os.path.basename(prev_file)])

        os.remove(prev_file)

    # Finalement : hexdump du fichier obtenu
    final_hex_path = f"/home/niveau{NIVEAU}/data.txt"
    with open(final_hex_path, "w") as out:
        subprocess.run(["xxd", current_file], stdout=out)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{final_hex_path}'")
    os.system(f"chmod 640 '{final_hex_path}'")

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Décoder et décompresser plusieurs couches de données cachées dans un fichier.

Pour t'aider :
Commence par convertir le fichier depuis l’hexadécimal vers un format binaire exploitable.

ℹ️ :
Une superbe commande te sera utile pour détecter les formats successifs (gzip, bzip2, tar…). Décompresse-les un à un.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Nettoyage temporaire
    os.system(f"rm -rf {dossier_tmp}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau13.main()

if __name__ == '__main__':
    main()
