# Movie Recommender

This is a Python command-line tool that recommends movies similar to a movie you choose, using data from The Movie Database (TMDB). Recommendations are ranked by similarities in genres, keywords, cast, and directors. 

## Setup
1. Clone this repository and create and activate a virtual environment.
2. Install the dependencies in requirements.txt.
3. Get a read access token for the TMDB API from the TMDB website:
https://www.themoviedb.org/settings/api
4. Create a .env file with:
```
TMDB_TOKEN=your_token_here
```

## Usage
With the virtual environment activated, run:
```
python -m main.py
```
Follow the prompts to input a movie and get related recommendations.