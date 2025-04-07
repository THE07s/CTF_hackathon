# Script d'initialisation pour l'utilisateur niveau13

import os
import CTF_lib
import niveau14
# import niveau15
import subprocess

def main():
    NIVEAU = 13
    SUIVANT = 14

    # Mot de passe niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Génération d'une paire de clés SSH
    key_dir = f"/tmp/sshkey_niveau{NIVEAU}"
    os.makedirs(key_dir, exist_ok=True)
    priv_path = f"{key_dir}/id_rsa"
    pub_path = f"{key_dir}/id_rsa.pub"

    subprocess.run(["ssh-keygen", "-t", "rsa", "-b", "2048", "-f", priv_path, "-N", ""])

    # Copie de la clé privée dans le home de niveau13
    chemin_priv = f"/home/niveau{NIVEAU}/sshkey.private"
    os.rename(priv_path, chemin_priv)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_priv}'")
    os.system(f"chmod 600 '{chemin_priv}'")

    # Ajout de la clé publique dans authorized_keys de niveau14
    ssh_dir = f"/home/niveau{SUIVANT}/.ssh"
    os.makedirs(ssh_dir, exist_ok=True)
    os.system(f"touch {ssh_dir}/authorized_keys")
    with open(pub_path, "r") as pub_file, open(f"{ssh_dir}/authorized_keys", "w") as auth_file:
        auth_file.write(pub_file.read())

    os.system(f"chown -R niveau{SUIVANT}:niveau{SUIVANT} {ssh_dir}")
    os.system(f"chmod 700 {ssh_dir}")
    os.system(f"chmod 600 {ssh_dir}/authorized_keys")

    # Nettoyage des clés temporaires
    os.remove(pub_path)
    os.rmdir(key_dir)

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Utiliser une clé SSH privée pour te connecter au niveau suivant.

Pour t'aider :
Un fichier contient une clé d'identification valide.

ℹ️ :
Utilise la commande : ssh <à compléter> niveau14@localhost

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau14.main()
    # niveau15.main()

if __name__ == '__main__':
    main()
