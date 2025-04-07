# Script d'initialisation pour l'utilisateur niveau16

import os
import ssl
import socket
import threading
import random
import subprocess
import CTF_lib
import niveau17

def main():
    NIVEAU = 16
    SUIVANT = 17
    PORT = random.randint(31000, 32000)

    # Mots de passe
    mdp_actuel = CTF_lib.get_mdp_hash(NIVEAU)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, CTF_lib.get_mdp_hash(SUIVANT))  # Pour cohérence

    # Génération clé SSH pour niveau17
    key_dir = f"/tmp/sshkey_lvl{SUIVANT}"
    os.makedirs(key_dir, exist_ok=True)
    priv_path = f"{key_dir}/id_rsa"
    pub_path = f"{key_dir}/id_rsa.pub"
    subprocess.run(["ssh-keygen", "-t", "rsa", "-b", "2048", "-f", priv_path, "-N", ""])

    # Mise en place du .ssh de niveau17
    ssh_dir = f"/home/niveau{SUIVANT}/.ssh"
    os.makedirs(ssh_dir, exist_ok=True)
    with open(pub_path, "r") as pub_file:
        with open(f"{ssh_dir}/authorized_keys", "w") as auth_file:
            auth_file.write(pub_file.read())
    os.system(f"chown -R niveau{SUIVANT}:niveau{SUIVANT} {ssh_dir}")
    os.system(f"chmod 700 {ssh_dir}")
    os.system(f"chmod 600 {ssh_dir}/authorized_keys")

    # Préparer certificat SSL temporaire
    certfile = f"/tmp/cert{NIVEAU}.pem"
    keyfile = f"/tmp/key{NIVEAU}.pem"
    os.system(f"openssl req -x509 -nodes -newkey rsa:2048 -keyout {keyfile} -out {certfile} -days 1 -subj '/CN=localhost'")

    # Contenu à renvoyer : clé privée
    with open(priv_path, "r") as f:
        key_content = f.read()

    def ssl_server():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('0.0.0.0', PORT))
            sock.listen(5)
            while True:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssl_conn:
                    try:
                        data = ssl_conn.recv(1024).decode().strip()
                        if data == mdp_actuel:
                            ssl_conn.sendall(key_content.encode())
                        else:
                            ssl_conn.sendall(b"Wrong password\n")
                    except Exception:
                        pass

    threading.Thread(target=ssl_server, daemon=True).start()

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

L'objectif de ce niveau :
Explorer les ports ouverts et détecter un service sécurisé. Envoie ton mot de passe au bon port, et tu obtiendras une clé SSH.

Pour t'aider :
Le serveur SSL est actif sur un port aléatoire entre 31000 et 32000.

ℹ️ :
Trouver les ports ouverts, puis <à trouver> localhost:<PORT à trouver>'

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Nettoyage temporaire
    os.remove(pub_path)
    os.remove(priv_path)
    os.rmdir(key_dir)

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau17.main()

if __name__ == '__main__':
    main()
