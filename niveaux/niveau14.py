# Script d'initialisation pour l'utilisateur niveau14

import os
import socket
import threading
import CTF_lib
import niveau15

def main():
    NIVEAU = 14
    SUIVANT = 15
    PORT = 30000

    # Mots de passe
    mdp_actuel = CTF_lib.get_mdp_hash(NIVEAU)
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    # Serveur qui attend le mot de passe et répond
    def listener():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("0.0.0.0", PORT))
            s.listen(1)
            while True:
                conn, _ = s.accept()
                with conn:
                    data = conn.recv(1024).decode().strip()
                    if data == mdp_actuel:
                        conn.sendall((mdp_suivant + "\n").encode())
                    else:
                        conn.sendall(b"Wrong password\n")

    thread = threading.Thread(target=listener, daemon=True)
    thread.start()

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Envoyer ton mot de passe actuel à un serveur local qui écoute sur un port spécifique. Si c'est le bon, il te donnera le mot de passe suivant.

Pour t'aider :
Le serveur écoute sur le port {PORT} de localhost. Il attend que tu lui envoies le bon mot de passe.

ℹ️ :
Utilise une commande comme : <...> localhost <numéro de port> ou echo 'motdepasse' | <...><numéro de port>

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
    niveau15.main()

if __name__ == '__main__':
    main()
