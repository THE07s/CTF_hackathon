import os
import subprocess
import pandas as pd
import ace_tools as tools

def run_as(user, cmd):
    try:
        result = subprocess.run(
            ["su", user, "-c", cmd],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout.strip()
    except Exception as e:
        return f"ERREUR: {e}"

def get_mdp_verite(niveau):
    try:
        with open(f"/etc/niveau_mdps/niveau{niveau}") as f:
            return f.read().strip()
    except:
        return None

# Joueurs simulés pour chaque niveau
joueurs = [
    lambda: run_as("niveau0", "cat readme"),
    lambda: run_as("niveau1", "cat ./-"),
    lambda: run_as("niveau2", "cat 'mon nom contient des espaces'"),
    lambda: run_as("niveau3", "cat jeSuisLa/...tuNeMeVoisPaaaas"),
    lambda: run_as("niveau4", "file jeSuisLa/* | grep ASCII | cut -d':' -f1 | xargs cat"),
    lambda: run_as("niveau5", "find jeSuisLa -type f -size 1033c ! -executable -exec cat {} \\;"),
    lambda: run_as("niveau6", "find / -type f -size 33c -user niveau7 -group niveau6 2>/dev/null -exec cat {} \\;"),
    lambda: run_as("niveau7", "grep millionth data.txt | cut -d' ' -f2"),
    lambda: run_as("niveau8", "sort data.txt | uniq -u"),
    lambda: run_as("niveau9", "strings data.txt | grep ="),
    lambda: run_as("niveau10", "base64 -d data.txt"),
    lambda: run_as("niveau11", "tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt"),
    lambda: run_as("niveau12", "xxd -r data.txt"),
    lambda: run_as("niveau13", "ssh -i /tmp/sshkey_niveau13/id_rsa niveau14@localhost -p 2222 'cat readme'"),
    lambda: run_as("niveau14", "openssl rsautl -decrypt -inkey /tmp/key15.pem -in data.txt"),
    lambda: run_as("niveau15", "openssl rsautl -decrypt -inkey /tmp/key16.pem -in data.txt"),
    lambda: run_as("niveau16", "nmap -p- localhost -Pn | grep open | cut -d'/' -f1 | xargs -I{{}} nc localhost {{}} <<< niveau16"),
    lambda: run_as("niveau17", "grep mot_de_passe fichier.txt | cut -d':' -f2 | tr -d ' '"),
    lambda: run_as("niveau18", "ps aux | grep '/le/fichier' | grep -v grep | awk '{print $2}' | xargs cat"),
    lambda: run_as("niveau19", "lsof -p $(pgrep -f /le/fichier) | grep /le/fichier | awk '{print $9}' | xargs cat"),
    lambda: run_as("niveau20", "ls -lR / | grep niveau21 | awk '{print $9}' | xargs cat 2>/dev/null"),
    lambda: run_as("niveau21", "grep -a -oE '[a-f0-9]{32}' /tmp/* | head -n1"),
    lambda: run_as("niveau22", "grep -a -oE '[a-f0-9]{32}' /dev/random | head -n1"),
    lambda: run_as("niveau23", "strings fichier_binaire | grep -oE '[a-f0-9]{32}'"),
    lambda: run_as("niveau24", "for pin in $(seq -w 0000 9999); do echo \"$(cat /etc/niveau_mdps/niveau24) $pin\" | nc localhost 30002; done | grep -v Wrong"),
    lambda: run_as("niveau25", "echo $(cat /etc/niveau_mdps/niveau25) | nc -u localhost 31001"),
    lambda: run_as("niveau26", "nc -v localhost 31002 <<< $(cat /etc/niveau_mdps/niveau26)"),
    lambda: run_as("niveau27", "cat fichier.zip | unzip -p -"),
    lambda: run_as("niveau28", "cat fichier.gz | gzip -d -"),
    lambda: run_as("niveau29", "cat fichier.bz2 | bzip2 -d -"),
    lambda: run_as("niveau30", "cat fichier.xz | xz -d -"),
    lambda: run_as("niveau31", "cat fichier_comprime | tar xOzf -"),
    lambda: run_as("niveau32", "ls -laR / 2>/dev/null | grep niveau33 | awk '{print $9}' | xargs cat 2>/dev/null"),
    lambda: "🎉 BRAVO, vous avez terminé tous les niveaux du CTF Hackaton ! 🎉"
]

def main():
    resultats = []
    for i in range(len(joueurs)):
        mdp_obtenu = joueurs[i]()
        mdp_attendu = get_mdp_verite(i + 1)
        resultats.append({
            "Niveau": f"{i} → {i+1}",
            "Mot de passe attendu": mdp_attendu,
            "Mot de passe obtenu": mdp_obtenu,
            "Résultat": "✅" if mdp_obtenu == mdp_attendu else "❌"
        })

    df = pd.DataFrame(resultats)
    tools.display_dataframe_to_user(name="Validation CTF Hackaton – niveaux 0 à 33", dataframe=df)

main()