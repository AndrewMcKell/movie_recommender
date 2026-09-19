import os
import json
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
    response_data = response.json()
    top_result_data = response_data["results"][0]
    with open("result.json", "w") as file:
        json.dump(top_result_data, file, indent=4)
    

if __name__ == "__main__":
    main()