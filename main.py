import os
import json
import requests
from dotenv import load_dotenv

from search_movies import (
    search_movie_by_title,
    get_movie_details,
    get_movie_keywords,
    get_movie_credits,
    get_director
)


def main():
    movie_search = search_movie_by_title("City of God")
    movie_id = movie_search["id"]
    movie_data = get_movie_details(movie_id)
    keyword_data = get_movie_keywords(movie_id)
    credit_data = get_movie_credits(movie_id)
    result = {}
    result["details"] = movie_data
    result["keywords"] = keyword_data
    result["cast"] = credit_data["cast"][:10]
    director_data = get_director(credit_data)
    result["director"] = director_data
    with open("result.json", "w") as input_movie:
        json.dump(result, input_movie, indent=4)


if __name__ == "__main__":
    main()