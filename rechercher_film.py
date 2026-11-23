import os

import requests
from dotenv import load_dotenv


def demander_titre(message):

    titre_recherche = input(message).strip()

    while True:

        if len(titre_recherche) <= 0:
            print("Les saisies vides ne sont pas autorisées.")
            titre_recherche = input(message).strip()

        else:
            return titre_recherche


def afficher_liste_courte_films(resultats_affiches):

    print("=== RESULTATS DE LA RECHERCHE ===")
    print()
    for numero, film in enumerate(resultats_affiches, start=1):

        date_sortie = film.get("release_date") or "Date de sortie inconnue."

        print(f"{numero} - {film['title']}")
        print(f"Date de sortie : {date_sortie}")
        print(f"Note moyenne : {film['vote_average']}/10")
        print("-------------------------")
        print()


def afficher_details_film_selectionne(film_selectionne):

    date_sortie = film_selectionne.get("release_date") or "Date de sortie inconnue"
    resume = film_selectionne.get("overview") or "Résumé indisponible"

    print("=== INFORMATIONS DU FILM ===")
    print()
    print(f"Identifiant TMDB : {film_selectionne['id']}")
    print(f"Titre : {film_selectionne['title']}")
    print(f"Titre original : {film_selectionne['original_title']}")
    print(f"Date de sortie : {date_sortie}")
    print(f"Note moyenne : {film_selectionne['vote_average']}/10")
    print(f"Résumé : {resume}")


def selectionner_film(resultats_affiches):

    try:
        choix_film = int(input("Entrez le numéro du film que vous souhaitez afficher : "))
    
        if 1 <= choix_film <= len(resultats_affiches):

            film_selectionne = resultats_affiches[choix_film - 1]
            return film_selectionne

        else:
            print("Aucun film ne correspond à ce numéro.")
            return None

    except ValueError:
        print("Un nombre est attendu pour sélectionner un film.")
        return None


def rechercher_films(titre_recherche, jeton):

    url = "https://api.themoviedb.org/3/search/movie"

    entetes = {
        "Authorization": f"Bearer {jeton}",
        "accept": "application/json"
    }

    parametres = {
        "query": titre_recherche,
        "language": "fr-FR"
    }

    try:
        reponse = requests.get(
            url,
            headers=entetes,
            params=parametres,
            timeout=10
        )

        reponse.raise_for_status()
        donnees = reponse.json()

    except requests.exceptions.Timeout:
        print("La requête a pris trop de temps.")

    except requests.exceptions.ConnectionError:
        print("Impossible de se connecter à Internet ou à TMDB.")

    except requests.exceptions.HTTPError as erreur:
        print(f"TMDB a renvoyé une erreur HTTP : {erreur}")

    except requests.exceptions.JSONDecodeError:
        print("La réponse reçue n'est pas un JSON valide.")

    else:
        resultats = donnees["results"]
        return resultats


load_dotenv()

jeton = os.getenv("TMDB_TOKEN")

if not jeton:
    print("Le jeton TMDB est introuvable. Vérifiez le fichier .env.")
else:
    titre_recherche = demander_titre("Quel film recherchez-vous ? ")

    resultats = rechercher_films(titre_recherche, jeton)

    if resultats is None:
        pass

    elif not resultats:
        print("Aucun film trouvé.")

    else:
        resultats_affiches = resultats[:5]

        afficher_liste_courte_films(resultats_affiches)

        film_selectionne = selectionner_film(resultats_affiches)

        if film_selectionne is not None:

            afficher_details_film_selectionne(film_selectionne)





