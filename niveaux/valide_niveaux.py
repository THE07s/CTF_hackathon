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

# Fonctions mises à jour pour correspondre aux scripts modifiés
def jouer_niveau0():
    return run_as("niveau0", "cat readme")

def jouer_niveau1():
    return run_as("niveau1", "cat ./-")

def jouer_niveau2():
    return run_as("niveau2", "cat 'mon nom contient des espaces'")

def jouer_niveau3():
    return run_as("niveau3", "cat jeSuisLa/...tuNeMeVoisPaaaas")

def jouer_niveau4():
    cmd = "file jeSuisLa/* | grep ASCII | cut -d':' -f1 | xargs cat"
    return run_as("niveau4", cmd)

def jouer_niveau5():
    cmd = "find jeSuisLa -type f -size 1033c ! -executable -exec cat {} \;"
    return run_as("niveau5", cmd)

def jouer_niveau6():
    cmd = "find / -type f -size 33c -user niveau7 -group niveau6 2>/dev/null -exec cat {} \;"
    return run_as("niveau6", cmd)

def jouer_niveau7():
    cmd = "grep millionth data.txt | cut -d' ' -f2"
    return run_as("niveau7", cmd)

def jouer_niveau8():
    cmd = "sort data.txt | uniq -u"
    return run_as("niveau8", cmd)

def jouer_niveau9():
    cmd = "strings data.txt | grep ="
    return run_as("niveau9", cmd)

joueurs = [
    jouer_niveau0,
    jouer_niveau1,
    jouer_niveau2,
    jouer_niveau3,
    jouer_niveau4,
    jouer_niveau5,
    jouer_niveau6,
    jouer_niveau7,
    jouer_niveau8,
    jouer_niveau9,
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
    tools.display_dataframe_to_user(name="Validation finale niveaux 0 à 9", dataframe=df)

main()
