import os
import requests
from dotenv import load_dotenv

from movie import Movie

def prepare_search():
    load_dotenv()
    token = os.getenv("TMDB_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return headers

def search_movies_by_title(title: str):
    url = "https://api.themoviedb.org/3/search/movie"
    headers = prepare_search()
    params = {
        "query": title
    }
    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()
    top_results_data = response_data["results"]
    return top_results_data

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
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = prepare_search()
    params = {
        "append_to_response": "keywords,credits"
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return Movie(
        movie_id = data["id"],
        title = data["title"],
        release_year = data["release_date"][:4],
        overview = data["overview"],
        genres = data["genres"],
        keywords = data["keywords"]["keywords"],
        director = get_director(data["credits"]),
        cast = get_main_cast(data["credits"])
    )

def find_candidate_movies(
        *,
        genres: list[int] | None = None,
        keywords: list[int] | None = None,
        cast: list[int] | None = None,
        director: list[int] | None = None,
        page: int = 1,
    ) -> list[dict]:
    url = "https://api.themoviedb.org/3/discover/movie"
    headers = prepare_search()
    params = {
        "page": page,
        "sort_by": "popularity.desc"
    }
    if genres:
        genre_list = []
        for genre_id in genres:
            genre_list.append(str(genre_id))
        params["with_genres"] = "|".join(genre_list)
    if keywords:
        keyword_list = []
        for keyword_id in keywords:
            keyword_list.append(str(keyword_id))
        params["with_keywords"] = "|".join(keyword_list)
    if cast:
        cast_list = []
        for actor_id in cast:
            cast_list.append(str(actor_id))
        params["with_cast"] = "|".join(cast_list)
    if director:
        director_list = []
        for director_id in director:
            director_list.append(str(director_id))
        params["with_crew"] = "|".join(director_list)
    response = requests.get(url, headers=headers, params=params)
    return response.json()
