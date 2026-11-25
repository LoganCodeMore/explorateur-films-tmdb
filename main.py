import os

from dotenv import load_dotenv
from films import effectuer_recherche_complete


def afficher_menu():

    print("=== RECHERCHE DE FILMS TMDB ===")
    print()
    print("1 - Rechercher un film")
    print("0 - Quitter")
    print()



load_dotenv()

jeton = os.getenv("TMDB_TOKEN")

if not jeton:
    print("Le jeton TMDB est introuvable. Vérifiez le fichier .env.")
else:
    while True:

        afficher_menu()

        choix = input("Entrez une commande du menu : ")
        print()

        if choix == "1":
            effectuer_recherche_complete(jeton)
        elif choix == "0":
            print("Au revoir.")
            break
        else:
            print("Commande invalide.")

        print()