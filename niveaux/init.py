# Script d'initialisation globale de tous les utilisateurs de niveau de CTF hackathon
import CTF_lib
import niveau0
import time

def main():
    print("Initialisation des utilisateurs de niveau de CTF hackathon…")

    for niveau in range(0, 27):
        print(f" → Création de l'utilisateur niveau{niveau}")
        CTF_lib.ajout_utilisateur(niveau)
    
    # Lancement du niveau 0
    print("Génération du niveau 0...")
    niveau0.main()

if __name__ == "__main__":
    main()
