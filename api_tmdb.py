import requests


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