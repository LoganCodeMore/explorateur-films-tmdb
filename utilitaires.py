def demander_titre(message):

    titre_recherche = input(message).strip()

    while True:

        if len(titre_recherche) <= 0:
            print("Les saisies vides ne sont pas autorisées.")
            titre_recherche = input(message).strip()

        else:
            return titre_recherche