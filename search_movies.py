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

def search_movie_by_title(title: str):
    url = "https://api.themoviedb.org/3/search/movie"
    headers = prepare_search()
    params = {
        "query": title
    }
    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()
    top_result_data = response_data["results"][0]
    return top_result_data

def get_movie_details(id: int):
    url = f"https://api.themoviedb.org/3/movie/{id}"
    headers = prepare_search()
    response = requests.get(url, headers=headers)
    result_data = response.json()
    return result_data

def get_movie_keywords(id: int):
    url = f"https://api.themoviedb.org/3/movie/{id}/keywords"
    headers = prepare_search()
    response = requests.get(url, headers=headers)
    keyword_data = response.json()
    return keyword_data

def get_movie_credits(id: int):
    url = f"https://api.themoviedb.org/3/movie/{id}/credits"
    headers = prepare_search()
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
        keywords = keywords["keywords"],
        director = get_director(credits),
        cast = get_main_cast(credits)
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
