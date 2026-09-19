import os
import requests
from dotenv import load_dotenv

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
    for person in credits["crew"]:
        if person["job"] == "Director":
            director_details = person
    return director_details