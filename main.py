import os
import json
import requests
from dotenv import load_dotenv

from search_movies import search_movie_by_title


def main():
    movie_data = search_movie_by_title("City of God")
    with open("result.json", "w") as file:
        json.dump(movie_data, file, indent=4)
    

if __name__ == "__main__":
    main()