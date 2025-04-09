# Script d'initialisation pour l'utilisateur niveau15

import os
import ssl
import socket
import threading
import multiprocessing
import CTF_lib
import niveau16

def main():
    NIVEAU = 15
    SUIVANT = 16
    PORT = 30001

    # Mots de passe
    mdp_actuel = CTF_lib.get_mdp_hash(NIVEAU)
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Création d’un contexte SSL auto-signé
    certfile = f"/tmp/cert{NIVEAU}.pem"
    keyfile = f"/tmp/key{NIVEAU}.pem"

    # Génère un certificat auto-signé avec OpenSSL (si pas déjà existant)
    if not os.path.exists(certfile) or not os.path.exists(keyfile):
        os.system(f"openssl req -x509 -nodes -newkey rsa:2048 -keyout {keyfile} -out {certfile} -days 1 -subj '/CN=localhost'")

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
                            ssl_conn.sendall((mdp_suivant + "\n").encode())
                            ssl_conn.shutdown(socket.SHUT_WR)  # Forcer l'envoi complet
                        else:
                            ssl_conn.sendall(b"Wrong password\n")
                            ssl_conn.shutdown(socket.SHUT_WR)
                    except Exception:
                        pass

    # Lancer le serveur SSL dans un processus séparé
    processus_ssl = multiprocessing.Process(target=ssl_server)
    processus_ssl.start()

    # Fichier readme
    contenu_readme = f"""\
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Communiquer avec un serveur local sécurisé via SSL pour obtenir le mot de passe du niveau suivant.

Pour t'aider :
Le serveur écoute sur le port {PORT} et attend que tu lui envoies ton mot de passe actuel.

ℹ️ :
Utilise la commande : <à trouver> localhost:{PORT}

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)
    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreint le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer le niveau suivant
    niveau16.main()

if __name__ == '__main__':
    main()
