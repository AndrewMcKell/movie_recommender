import os
import requests
from dotenv import load_dotenv

from movie import Movie

def search_movie_by_title(title: str):
    load_dotenv()
    url = "https://api.themoviedb.org/3/search/movie"
    token = os.getenv("TMDB_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
        }
    params = {
        "query": title
    }
    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()
    top_result_data = response_data["results"][0]
    return top_result_data

def get_movie_details(id: int):
    load_dotenv()
    url = f"https://api.themoviedb.org/3/movie/{id}"
    token = os.getenv("TMDB_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
        }
    response = requests.get(url, headers=headers)
    result_data = response.json()
    return result_data

def get_movie_keywords(id: int):
    load_dotenv()
    url = f"https://api.themoviedb.org/3/movie/{id}/keywords"
    token = os.getenv("TMDB_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
        }
    response = requests.get(url, headers=headers)
    keyword_data = response.json()
    return keyword_data

def get_movie_credits(id: int):
    load_dotenv()
    url = f"https://api.themoviedb.org/3/movie/{id}/credits"
    token = os.getenv("TMDB_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
        }
    response = requests.get(url, headers=headers)
    credit_data = response.json()
    return credit_data

def get_director(credits: dict):
    directors = []
    for person in credits["crew"]:
        if person["job"] == "Director":
            director_details = {
                "id": person["id"],
                "name": person["name"]
            }
            directors.append(director_details)
    return directors

def get_main_cast(credits: dict, n: int=10):
    main_cast = []
    for actor in credits["cast"][:n]:
        actor_details = {
            "id": actor["id"],
            "name": actor["name"],
            "character": actor["character"]
        }
        main_cast.append(actor_details)
    return main_cast

def get_movie_data(movie_id: int):
    details = get_movie_details(movie_id)
    keywords = get_movie_keywords(movie_id)
    credits = get_movie_credits(movie_id)
    release_year = details["release_date"][:4]
    return Movie(
        movie_id = details["id"],
        title = details["title"],
        release_year = release_year,
        overview = details["overview"],
        genres = details["genres"],
        keywords = keywords,
        director = get_director(credits),
        cast = get_main_cast(credits)
    )