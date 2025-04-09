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
Un serveur sécurisé t’attend, dissimulé derrière une connexion SSL. Il est silencieux, vigilant… mais prêt à s’ouvrir à celui qui saura lui parler dans le bon langage.\
Ton mot de passe actuel est la clé. \
Ta mission : le transmettre à ce serveur, et en retour, recevoir celui du niveau suivant.

Pour t'aider :
Le serveur est bien en place, à l’écoute sur le port {PORT}, ici même, sur localhost.\
Mais il ne s’agit pas d’une simple communication texte : tu dois établir une vraie connexion SSL, puis lui envoyer exactement ton mot de passe, sans retour à la ligne ni espace inutile.

ℹ️ :
Commence par récupérer ton mot de passe actuel.\
Prépare-le pour l’envoyer tel quel, sans saut de ligne parasite.\
Puis établis une connexion SSL silencieuse avec le serveur.\
Une fois connecté, envoie directement ton mot de passe, d’un seul bloc, pour qu’il soit bien compris

Bonne chance, et n’oublie pas : Ce niveau ne teste pas ta force brute, mais ta précision.\
Lis. Formate. Transmets. Et le serveur, s’il reconnaît ta sincérité… t’ouvrira le chemin.\
Ouvre bien les 👀. Et entre discrètement. 👁️‍🗨️🔓
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
