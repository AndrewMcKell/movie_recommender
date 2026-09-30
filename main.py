import os
import json
import requests
from dotenv import load_dotenv

from search_movies import (
    search_movie_by_title,
    get_movie_details,
    get_movie_keywords,
    get_movie_credits,
    get_director,
    get_main_cast,
    get_movie_data,
    find_candidate_movies
)
from recommender import movie_similarity, get_candidate_movie_ids

def main():
    movie_search = search_movie_by_title("City of God")
    movie_id = movie_search["id"]
    movie_data = get_movie_details(movie_id)
    keyword_data = get_movie_keywords(movie_id)
    credit_data = get_movie_credits(movie_id)
    result = {}
    result["details"] = movie_data
    result["keywords"] = keyword_data
    result["cast"] = get_main_cast(credit_data)
    director_data = get_director(credit_data)
    result["director"] = director_data
    with open("result.json", "w") as input_movie:
        json.dump(result, input_movie, indent=4)

    movie1_search = search_movie_by_title("Goodfellas")
    movie1_id = movie1_search["id"]
    movie1 = get_movie_data(movie1_id)
    movie2_search = search_movie_by_title("City of God")
    movie2_id = movie2_search["id"]
    movie2 = get_movie_data(movie2_id)
    movie3_search = search_movie_by_title("Raging Bull")
    movie3_id = movie3_search["id"]
    movie3 = get_movie_data(movie3_id)

    similarity_1_2 = movie_similarity(movie1, movie2)
    similarity_1_3 = movie_similarity(movie1, movie3)
    similarity_2_3 = movie_similarity(movie2, movie3)
    same = movie_similarity(movie1, movie1)

    print(similarity_1_2)
    print(similarity_1_3)
    print(similarity_2_3)
    print(same)

    movie_to_search = "Casino Royale"
    movie_input_search = search_movie_by_title(movie_to_search)
    movie_input_id = movie_input_search["id"]
    movie_input = get_movie_data(movie_input_id)
    candidate_ids = get_candidate_movie_ids(movie_input)
    movie_list = []
    for movie_id in candidate_ids:
        candidate_movie = get_movie_data(movie_id)
        movie_list.append(candidate_movie)
    top_candidates = []
    for candidate in movie_list:
        similarity_score = movie_similarity(movie_input, candidate)
        top_candidates.append((similarity_score, candidate))
    top_candidates.sort(key=lambda item: item[0], reverse=True)
    for (score, recommendation) in top_candidates[:10]:
        print(f"title: {recommendation.title}, score: {score}")


if __name__ == "__main__":
    main()