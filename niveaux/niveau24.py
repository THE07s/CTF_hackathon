# Script d'initialisation pour l'utilisateur niveau24

import os
import socket
import threading
import random
import CTF_lib

def main():
    NIVEAU = 24
    SUIVANT = 25
    PORT = 30002
    mdp_attendu = CTF_lib.get_mdp_hash(NIVEAU)

    # Génération du bon code PIN
    code_correct = f"{random.randint(0, 9999):04d}"

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    chemin_pass_suivant = f"/etc/bandit_pass/niveau25"
    with open(chemin_pass_suivant, "w") as f:
        f.write(mdp_suivant + "\n")
    os.system(f"chmod 640 '{chemin_pass_suivant}'")

    # Serveur bruteforce
    def server():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', PORT))
            s.listen()
            while True:
                conn, _ = s.accept()
                with conn:
                    try:
                        data = conn.recv(1024).decode().strip()
                        if not data:
                            continue
                        parts = data.split(" ")
                        if len(parts) != 2:
                            conn.sendall(b"Invalid format\n")
                            continue
                        motdepasse, code = parts
                        if motdepasse == mdp_attendu and code == code_correct:
                            conn.sendall(mdp_suivant.encode() + b"\n")
                        else:
                            conn.sendall(b"Wrong\n")
                    except Exception:
                        continue

    threading.Thread(target=server, daemon=True).start()

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Contacter un serveur TCP local, lui envoyer le bon mot de passe et un code PIN à 4 chiffres.

Pour t'aider :
Le serveur écoute sur le port {PORT} et attend une ligne contenant :
<mot_de_passe> <PIN>

ℹ️ :
Essaie d’écrire un script bash ou python.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

if __name__ == '__main__':
    main()
