import os
import json
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