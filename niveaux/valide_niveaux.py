#!/usr/bin/env python3
import os
import subprocess
import hashlib
import time

LOG_FILE = "/tmp/validation.log"

def log_message(message):
    """Écrit le message dans le fichier de log en mode append."""
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")

def get_expected_passwords():
    """
    Retourne un dictionnaire des mots de passe attendus pour chaque niveau.
    Pour le niveau 0, le mot de passe est "niveau0".
    Pour les niveaux > 0, le mot de passe est le MD5 de "Je suis le meilleur admin de CTF !{niveau}".
    """
    seed = "Je suis le meilleur admin de CTF !"
    d = {}
    for level in range(0, 26):
        if level == 0:
            d[level] = "niveau0"
        else:
            d[level] = hashlib.md5(f"{seed}{level}".encode()).hexdigest()
    return d

def run_cmd(cmd, input_text=None):
    """
    Exécute une commande shell, capture stdout et stderr, les logge, et retourne stdout.
    """
    try:
        result = subprocess.run(cmd, shell=True, input=input_text, capture_output=True, text=True, timeout=30)
        log_message(f"Commande exécutée : {cmd}")
        log_message("STDOUT :\n" + result.stdout)
        log_message("STDERR :\n" + result.stderr)
        return result.stdout.strip()
    except Exception as e:
        log_message(f"Erreur lors de l'exécution de '{cmd}' : {e}")
        return f"Erreur : {e}"

def run_cmd_as_user(level, cmd, input_text=None):
    """
    Exécute la commande cmd depuis le home de l'utilisateur niveau{level} en utilisant su.
    On s'assure que le shell démarre dans le répertoire personnel.
    """
    # Échappe les éventuelles doubles quotes dans la commande
    safe_cmd = cmd.replace('"', '\\"')
    new_cmd = f"su - niveau{level} -c \"cd ~ && {safe_cmd}\""
    return run_cmd(new_cmd, input_text)

# Définition des commandes de validation pour chaque niveau (0 à 25)
validation_steps = {
    0: "cat readme",
    1: "cat ./-",
    2: "cat mon\\ nom\\ contient\\ des\\ espaces",
    3: "ls -la jeSuisLa && cat jeSuisLa/...tuNeMeVoisPaaaas",
    4: "file jeSuisLa/* | grep 'ASCII text' | cut -d: -f1 | xargs cat",
    5: "find jeSuisLa/ -type f -size 1033c -readable ! -executable | xargs cat",
    6: "find / -user niveau7 -group niveau6 -size 33c 2>/dev/null | xargs cat",
    7: "grep millionth data.txt",
    8: "sort data.txt | uniq -u",
    9: "strings data.txt | grep -oE '[0-9a-f]{32}'",
    10: "base64 -d data.txt",
    11: "tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt",
    12: "xxd -r data.txt | gunzip | tar -xf - -O | bunzip2 | tar -xf - -O | gunzip | tar -xf - -O | bunzip2 | gunzip",
    13: "ssh -i sshkey.private -p 2222 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null niveau14@localhost 'cat /etc/niveau_mdps/niveau14'",
    14: "cat /etc/niveau_mdps/niveau14 | xargs -I{} echo {} | nc localhost 30000",
    15: "echo -n \"$(echo -n 'Je suis le meilleur admin de CTF !15' | md5sum | cut -d' ' -f1)\" | openssl s_client -quiet -connect localhost:30001",
    16: "grep -Fxvf passwords.old passwords.new",
    17: "./niveau18-do cat /etc/niveau_mdps/niveau18",
    18: "nc -lvp 12345 & sleep 1 && ./suconnect 12345 && pkill -f \"nc -lvp 12345\"",
    19: "bash -c \"source /usr/bin/cronjob_niveau20.sh; cat /tmp/$(echo I am user niveau20 | md5sum | cut -d ' ' -f 1)\"",
    20: "echo -n 'I am user niveau21' | md5sum | cut -d ' ' -f 1 | xargs -I{} cat /tmp/{}",
    21: "for i in $(seq -w 0000 9999); do out=$(echo 'PLACEHOLDER_PASSWORD' $i | nc -w 1 localhost 30002 2>/dev/null); [[ $out != Wrong ]] && echo $out && break; done",
    22: "for f in hidden.txt motdepasse.html index.html.bak; do curl -fs localhost:8080/$f && break; done",
    23: "base64 -d donnees.mystere | gunzip",
    24: "cat acces_groupe.txt",
    25: "grep niveau26 /var/log/hackathon.log | cut -d ':' -f3 | tr -d ' '"
}

expected_passwords = get_expected_passwords()
results = []

print("Début de la validation des niveaux...\n")
log_message("Début de la validation des niveaux...")

# Itération sur les niveaux de 0 à 25
for level in range(0, 26):
    cmd = validation_steps.get(level)
    if not cmd:
        results.append((f"niveau{level}", "⏭️", "Non testé"))
        continue

    print(f"🧪 Test du niveau {level}…")
    log_message(f"🧪 Test du niveau {level}…")
    
    # Attente de 1:30 minute uniquement pour le premier niveau utilisant un cronjob (niveau 19)
    if level == 19:
        print("Attente de 1:30 minute pour laisser le temps d'exécution du cronjob...")
        log_message("Attente de 1:30 minute pour le cronjob...")
        time.sleep(90)
        
    # Pour le niveau 21, remplacer le placeholder par le mot de passe attendu
    if level == 21:
        cmd = cmd.replace("PLACEHOLDER_PASSWORD", expected_passwords[21])
    
    # Exécute la commande en tant qu'utilisateur "niveauX" depuis son home
    output = run_cmd_as_user(level, cmd)
    
    # Recherche du mot de passe attendu dans la sortie
    found = None
    for key, pw in expected_passwords.items():
        if pw in output:
            found = pw
            break

    if found:
        results.append((f"niveau{level}", "✅", found))
    else:
        results.append((f"niveau{level}", "❌", "Non trouvé"))

# Affichage du tableau récapitulatif
print("\n📋 Résumé de validation des niveaux :")
log_message("📋 Résumé de validation des niveaux :")
summary = f"{'Niveau':<10} {'Statut':<6} Mot de passe"
print(summary)
log_message(summary)
print("=" * 50)
log_message("=" * 50)
for row in results:
    line = f"{row[0]:<10} {row[1]:<6} {row[2]}"
    print(line)
    log_message(line)
