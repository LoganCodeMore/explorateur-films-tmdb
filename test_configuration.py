import os

from dotenv import load_dotenv


load_dotenv()

jeton = os.getenv("TMDB_TOKEN")

if jeton:
    print("Le jeton TMDB a été chargé avec succès.")

else:
    print("Le jeton TMDB est introuvable.")