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