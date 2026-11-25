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


def afficher_details_film_selectionne(details_film):

    date_sortie = details_film.get("release_date") or "Date de sortie inconnue"
    resume = details_film.get("overview") or "Résumé indisponible"

    noms_genres = []
    
    for genre in details_film['genres']:
        noms_genres.append(genre['name'])

    genres_formates = ", ".join(noms_genres)

    duree = details_film['runtime']
    heures = duree // 60
    minutes = duree % 60

    print("=== INFORMATIONS DU FILM ===")
    print()
    print(f"Identifiant TMDB : {details_film['id']}")
    print(f"Titre : {details_film['title']}")
    print(f"Titre original : {details_film['original_title']}")
    print(f"Genres : {genres_formates}")
    print(f"Date de sortie : {date_sortie}")
    print(f"Durée : {heures} h {minutes} min")
    print(f"Note moyenne : {details_film['vote_average']}/10")
    print(f"Résumé : {resume}")