# Script d'initialisation globale de tous les utilisateurs de niveau de CTF Hackaton
import CTF_lib
import niveau0
import time

def main():
    print("Initialisation des utilisateurs de niveau de CTF Hackaton…")

    for niveau in range(0, 25):
        print(f" → Création de l'utilisateur niveau{niveau}")
        CTF_lib.ajout_utilisateur(niveau)

    # Attente pour éviter les erreurs de chown/open trop précoces
    print("⏳ Attente que les utilisateurs et répertoires soient bien enregistrés...")
    time.sleep(2)

    print("\n✅ Tous les utilisateurs ont été créés avec succès.\nTu peux maintenant lancer le script niveau 0.")
    
    # Lancement du niveau 0
    print("Génération du niveau 0...")
    niveau0.main()

if __name__ == "__main__":
    main()
