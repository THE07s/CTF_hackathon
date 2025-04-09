# Script d'initialisation pour l'utilisateur niveau26

import os
import random
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
import CTF_lib
import niveau23

def main():
    NIVEAU = 22
    SUIVANT = 23
    PORT = 8080
    mdp_suivant = CTF_lib.get_mdp_hash(SUIVANT)
    CTF_lib.ecrire_fichier_mdp(SUIVANT, mdp_suivant)

    dossier_http = f"/tmp/http_niveau{NIVEAU}"
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
    contenu_readme = f"""
Bienvenue dans le niveau {NIVEAU} du CTF hackathon.

Objectif:
Un serveur HTTP local tourne en secret, sur le port {PORT}. \
Il contient un fichier caché, bien protégé… mais à celui ou celle qui saura deviner son nom, il offrira le mot de passe du niveau suivant.\
Pourras-tu le trouver? 

Pour t'aider :
Le serveur est actif, et tu peux t’y connecter avec un navigateur ou en ligne de commande.\
Mais il ne liste pas ses fichiers, même si tu visites la racine.\
Pour progresser, tu vas devoir deviner le nom exact du fichier qui contient le mot de passe, puis l’interroger directement.

ℹ️ :
Pense à des noms de fichiers souvent oubliés ou sauvegardés par erreur…(par exemple : hidden.txt, motdepasse.html, index.html.bak, etc.)\
Une commande te permet d’envoyer une requête HTTP silencieuse, et de vérifier si le fichier existe ou non\
Teste plusieurs noms jusqu’à tomber sur le bon : quand le bon fichier sera trouvé, le serveur te répondra.

Bonne chance, et n’oublie pas : c’est un test de flair.\
Devine juste, vise bien, et le serveur t’ouvrira la porte.\
Tape à la bonne adresse… et n’oublie pas d’ouvrir les 👀
"""
    chemin_readme = f"/home/niveau{NIVEAU}/readme"
    with open(chemin_readme, "w") as f:
        f.write(contenu_readme)

    os.system(f"chown niveau{NIVEAU}:niveau{NIVEAU} '{chemin_readme}'")
    os.system(f"chmod 640 '{chemin_readme}'")

    # Restreindre le home
    CTF_lib.dossier_home_lecture(NIVEAU)

    # Lancer niveau suivant
    niveau23.main()

if __name__ == '__main__':
    main()
