# Script d'initialisation pour l'utilisateur niveau24

import os
import socket
import threading
import random
import CTF_lib
import niveau22

def main():
    NIVEAU = 21
    SUIVANT = 22
    PORT = 30002
    mdp_attendu = CTF_lib.get_mdp_hash(NIVEAU)

    # Génération du bon code PIN
    code_correct = f"{random.randint(0, 9999):04d}"

    # Mot de passe du niveau suivant
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    chemin_pass_suivant = f"/etc/niveau_mdps/niveau{SUIVANT}"
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
    contenu_readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Un serveur TCP local se tient prêt à te donner le mot de passe du niveau suivant…\
Contacte le.\
Mais attention... il ne se contente pas de ton mot de passe : il veut une preuve supplémentaire.\
Un code PIN à 4 chiffres, et pas un de plus.

Pour t'aider :
LLe serveur écoute sur le port {PORT}, ici même sur localhost. \
Il attend une seule ligne, au format suivant : <mot_de_passe> <PIN>\
Tu dois lui envoyer cette ligne, et trouver le bon code PIN. \
Si tu te trompes, il répond « Wrong »… mais si tu vises juste, il te livrera le mot de passe du niveau suivant.

ℹ️ :
Prépare une boucle qui teste chaque PIN possible de 0000 à 9999\
Envoie à chaque fois le mot de passe actuel suivi du code PIN testé\
Interprète la réponse du serveur : dès qu’elle change, tu tiens le bon\
Tu peux écrire un petit script en bash ou en python pour automatiser l’envoi

Bonne chance, et n’oublie pas :Chaque tentative te rapproche de la vérité. Sois patient·e. Sois méthodique. \
Et surtout… ouvre grand les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} {chemin_readme}")
    os.system(f"chmod 640 {chemin_readme}")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau22.main()

if __name__ == '__main__':
    main()
