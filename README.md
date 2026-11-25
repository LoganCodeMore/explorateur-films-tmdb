# Explorateur de films TMDB

Application Python en ligne de commande permettant de rechercher des films avec l’API TMDB, de consulter leurs informations détaillées et d’ouvrir leur affiche dans le navigateur.

Ce projet a été réalisé dans le cadre de mon apprentissage de l’utilisation des API avec Python.

## Fonctionnalités

- Recherche d’un film par titre
- Affichage des cinq premiers résultats
- Sélection d’un film
- Récupération de sa fiche détaillée
- Affichage du titre original, des genres, de la durée, de la date de sortie, de la note et du résumé
- Ouverture automatique de l’affiche dans le navigateur
- Gestion des recherches sans résultat
- Gestion des erreurs de connexion, de délai, HTTP et JSON
- Possibilité d’effectuer plusieurs recherches grâce à un menu

## Technologies utilisées

- Python
- API TMDB
- Requests
- Python-dotenv
- Git et GitHub

## Organisation du projet

```text
apprentissage-api-cinema/
├── main.py
├── films.py
├── api_tmdb.py
├── affichage.py
├── utilitaires.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

- `main.py` : lancement de l’application et menu principal
- `films.py` : déroulement complet d’une recherche
- `api_tmdb.py` : communication avec l’API TMDB
- `affichage.py` : présentation des résultats et des détails
- `utilitaires.py` : contrôle des saisies utilisateur

## Installation

### 1. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 2. Activer l’environnement virtuel

Sous PowerShell :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

Sous l’invite de commandes Windows :

```cmd
.venv\Scripts\activate.bat
```

### 3. Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

### 4. Configurer le jeton TMDB

Créer un compte TMDB et demander un jeton d’accès à l’API.

Copier `.env.example` vers un nouveau fichier nommé `.env` :

```text
TMDB_TOKEN=votre_jeton_tmdb
```

Remplacer la valeur d’exemple par votre véritable jeton.

Le fichier `.env` ne doit jamais être publié sur GitHub.

## Lancement

```bash
python main.py
```

## Notions travaillées

- Envoi de requêtes HTTP
- Utilisation d’un jeton d’authentification
- Lecture de données JSON
- Manipulation de listes et de dictionnaires
- Gestion des erreurs réseau
- Variables d’environnement
- Découpage d’un programme en modules
- Utilisation de Git

## Attribution TMDB

This product uses the TMDB API but is not endorsed or certified by TMDB.