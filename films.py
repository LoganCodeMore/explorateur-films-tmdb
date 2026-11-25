import webbrowser

from api_tmdb import rechercher_films, recuperer_details_film
from utilitaires import demander_titre
from affichage import (
    afficher_liste_courte_films,
    afficher_details_film_selectionne
)


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


def ouvrir_affiche_film(details_film):

    chemin_affiche = details_film.get("poster_path")

    if chemin_affiche is None:
        print("Aucune affiche disponible pour ce film.")

    else:
        url_affiche = f"https://image.tmdb.org/t/p/w500{chemin_affiche}"

        webbrowser.open(url_affiche)


def effectuer_recherche_complete(jeton):

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

            id_film = film_selectionne['id']

            details_film = recuperer_details_film(id_film, jeton)

            if details_film is not None:

                afficher_details_film_selectionne(details_film)

                ouvrir_affiche_film(details_film)