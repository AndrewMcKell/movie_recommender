import os
import requests
from dotenv import load_dotenv

def main():
    load_dotenv()
    url = "https://api.themoviedb.org/3/search/movie"
    token = os.getenv("TMDB_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
        }
    movie_title = "City of God"
    params = {
        "query": movie_title
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.text)
    

if __name__ == "__main__":
    main()