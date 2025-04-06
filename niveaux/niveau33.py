# Script d'initialisation pour l'utilisateur niveau33

import os
import CTF_lib

def main():
    NIVEAU = 33
    SUIVANT = 34

    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    dossier = f"/home/niveau{NIVEAU}"
    fichier_pass = os.path.join(dossier, "fichier.txt")
    binaire = os.path.join(dossier, "vuln33.c")
    binaire_exec = os.path.join(dossier, "vuln33")

    # Créer un fichier contenant un leurre
    with open(fichier_pass, "w") as f:
        f.write("Pas ici 😉\n")

    # Code C vulnérable (appel à 'cat' sans chemin)
    with open(binaire, "w") as f:
        f.write("""#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
    printf("Bienvenue dans vuln33 !\\n");
    system("cat fichier.txt");
    return 0;
}
""")

    os.system(f"chown niveau{SUIVANT}:niveau{SUIVANT} {fichier_pass}")
    os.system(f"chmod 600 {fichier_pass}")

    os.system(f"gcc {binaire} -o {binaire_exec}")
    os.system(f"chown niveau{SUIVANT}:niveau{SUIVANT} {binaire_exec}")
    os.system(f"chmod 4755 {binaire_exec}")  # SUID binaire

    # Readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Exploiter un binaire SUID vulnérable pour obtenir le mot de passe du niveau suivant.

Pour t'aider :
Le programme vuln33 exécute une commande système sans sécurité. À toi de la détourner…

ℹ️ :
Regarde ce que fait le binaire.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    readme_path = f"/home/niveau{NIVEAU}/readme"
    with open(readme_path, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {readme_path}")
    os.system(f"chmod 640 {readme_path}")

    CTF_lib.dossier_home_lecture(NIVEAU)

if __name__ == '__main__':
    main()
