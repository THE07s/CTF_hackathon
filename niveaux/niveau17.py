# Script d'initialisation pour l'utilisateur niveau19

import os
import CTF_lib
import niveau18
import textwrap

def main():
    NIVEAU = 17
    SUIVANT = 18

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    dossier = f"/home/niveau{NIVEAU}"
    chemin_script = os.path.join(dossier, f"niveau{SUIVANT}-do")
    
    # Création du wrapper en C pour directement changer d'UID vers niveau18
    chemin_c_source = os.path.join(os.path.dirname(chemin_script), f"niveau{SUIVANT}-do-wrapper.c")
    code_c = textwrap.dedent(f"""\
        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>
        #include <unistd.h>
        #include <pwd.h>

        int main(int argc, char *argv[]) {{
            if (argc < 2) {{
                fprintf(stderr, "Usage: %s <commande>\\n", argv[0]);
                return 1;
            }}

            // Concatène tous les arguments en une seule commande
            int total_length = 0;
            for (int i = 1; i < argc; i++) {{
                total_length += strlen(argv[i]) + 1;
            }}
            char *cmd = malloc(total_length);
            if (!cmd) {{
                perror("malloc");
                return 1;
            }}
            cmd[0] = '\\0';
            for (int i = 1; i < argc; i++) {{
                strcat(cmd, argv[i]);
                if (i < argc - 1)
                    strcat(cmd, " ");
            }}

            struct passwd *pw = getpwnam("niveau{SUIVANT}");
            if (!pw) {{
                perror("getpwnam");
                free(cmd);
                return 1;
            }}

            if (setuid(pw->pw_uid) != 0) {{
                perror("setuid");
                free(cmd);
                return 1;
            }}

            execl("/bin/sh", "sh", "-c", cmd, (char *)NULL);
            perror("execl");
            free(cmd);
            return 1;
        }}
    """)
    with open(chemin_c_source, "w") as f:
        f.write(code_c)

    # Compilation du code C pour générer le binaire niveau18-do
    os.system(f"gcc '{chemin_c_source}' -o '{chemin_script}'")
    # Suppression du fichier source après compilation
    os.remove(chemin_c_source)

    # Attribution des permissions SUID sur le binaire compilé
    os.system(f"chown root:niveau{NIVEAU} '{chemin_script}'")
    os.system(f"chmod 4750 '{chemin_script}'")  # SUID sur le binaire

    # Fichier readme
    contenu_readme = f"""\
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Un outil spécial t’a été confié. Il ne ressemble à rien de ce que tu as vu jusqu’ici. \
Et pourtant… c’est lui qui te permettra d’atteindre le niveau supérieur.\
Avec lui, tu vas pouvoir exécuter une commande comme si tu étais déjà dans la peau du prochain utilisateur.

Pour t'aider :
Dans ton dossier personnel se trouve un exécutable mystérieux. C’est la clé. \
Si tu l’utilises correctement, il exécutera la commande que tu lui donnes, avec les privilèges du niveau suivant.

ℹ️ :
Repère ce fichier dans ton répertoire personnel.\
Lance-le en lui passant une commande claire, simple, directe.\
Ton objectif ? Lire un fichier contenant le mot de passe… et tu sais où ils se trouvent tous, n’est-ce pas ? 😉

Bonne chance, et n’oublie pas : Ce niveau ne demande pas d’exploiter une faille… il te demande d’utiliser un privilège.\
Tu as le droit d’entrer… mais encore faut-il que tu saches comment frapper.\
Regarde bien dans ton environnement. Et surtout… ouvre les 👀. 
"""
    chemin_readme = os.path.join(dossier, "readme")
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_readme}'")
    os.system(f"chmod 640 '{chemin_readme}'")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer le niveau suivant
    niveau18.main()

if __name__ == '__main__':
    main()
