# Script d'initialisation globale de tous les utilisateurs de niveau de CTF Hackaton
import CTF_lib
import niveau0

def main():
    print("Initialisation des utilisateurs de niveau de CTF Hackaton…")
    
    for niveau in range(0, 25):
        print(f" → Création de l'utilisateur niveau{niveau}")
        CTF_lib.ajout_utilisateur(niveau)

    print("\n✅ Tous les utilisateurs ont été créés avec succès.\nTu peux maintenant lancer le script niveau0.py pour démarrer le jeu.")

    # Lancement du niveau 0
    print("Génération du niveau 0...")
    niveau0.main()

if __name__ == "__main__":
    main()
