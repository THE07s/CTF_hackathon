# Script d'initialisation pour l'utilisateur niveau26

import os
import random
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
import CTF_lib
import niveau27

def main():
    NIVEAU = 26
    PORT = 8080
    mdp_suivant = CTF_lib.get_mdp_hash(27)
    CTF_lib.ecrire_fichier_mdp(27, mdp_suivant)

    dossier_http = f"/tmp/http_lvl{NIVEAU}"
    os.makedirs(dossier_http, exist_ok=True)

    # Nom du fichier caché
    nom_fichier = random.choice(["hidden.txt", "motdepasse.html", "index.html.bak"])
    chemin_fichier = os.path.join(dossier_http, nom_fichier)

    with open(chemin_fichier, "w") as f:
        f.write(mdp_suivant + "\n")

    class CustomHandler(SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass  # silence logs

    def lancer_http():
        os.chdir(dossier_http)
        httpd = HTTPServer(('0.0.0.0', PORT), CustomHandler)
        httpd.serve_forever()

    threading.Thread(target=lancer_http, daemon=True).start()

    # Fichier readme
    contenu_readme = f"""Bienvenue dans le niveau {NIVEAU} du CTF Hackaton.

L'objectif de ce niveau :
Trouver un fichier caché sur un serveur HTTP local pour obtenir le mot de passe du niveau suivant.

Pour t'aider :
Un serveur HTTP est actif sur le port {PORT}, mais ne liste pas ses fichiers. Tu dois deviner l’URL correcte.

ℹ️ :
Trouve la bonne commande.

Bonne chance, et n’oublie pas : ouvre les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_readme}'")
    os.system(f"chmod 640 '{chemin_readme}'")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau27.main()

if __name__ == '__main__':
    main()
