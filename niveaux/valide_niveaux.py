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



# #!/usr/bin/env python3
# import os
# import subprocess

# NIVEAUX = 34

# def test_read_password(niveau):
#     user = f"niveau{niveau}"
#     next_user = f"niveau{niveau+1}" if niveau < NIVEAUX - 1 else None
#     print(f"🧪 Test niveau {niveau} ({user})")

#     if not next_user:
#         print("✅ Dernier niveau, rien à tester")
#         return True

#     # Chemin du mot de passe
#     mdp_path = f"/etc/bandit_pass/{next_user}"
#     if not os.path.exists(mdp_path):
#         print(f"❌ Mot de passe {next_user} manquant")
#         return False

#     # Lire via su -c
#     try:
#         result = subprocess.run(
#             ["su", "-c", f"cat {mdp_path}", user],
#             capture_output=True, text=True, timeout=5
#         )
#         if result.returncode != 0:
#             print(f"❌ Accès refusé au mot de passe de {next_user}")
#             return False
#         output = result.stdout.strip()
#         if len(output) < 6:
#             print(f"❌ Mot de passe trop court ou vide pour {next_user}")
#             return False
#         print(f"✅ {user} peut accéder au mot de passe de {next_user} : {output}")
#         return True
#     except Exception as e:
#         print(f"❌ Erreur sur niveau {niveau} : {e}")
#         return False

# def main():
#     erreurs = 0
#     for i in range(NIVEAUX):
#         if not test_read_password(i):
#             erreurs += 1

#     if erreurs == 0:
#         print("\n🎉 Tous les niveaux sont valides !")
#     else:
#         print(f"\n⚠️ {erreurs} niveau(x) en erreur")

# if __name__ == "__main__":
#     main()
