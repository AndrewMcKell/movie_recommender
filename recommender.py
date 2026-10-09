from movie import Movie
from search_movies import find_candidate_movies, get_movie_data

def set_similarity(ids1: list[int], ids2: list[int]):
    set_a = set(ids1)
    intersection = set_a.intersection(ids2)
    union = set_a.union(ids2)
    return len(intersection) / len(union)

def genre_similarity(movie1: Movie, movie2: Movie):
    return set_similarity(movie1.get_genre_ids(), movie2.get_genre_ids())

def keyword_similarity(movie1: Movie, movie2: Movie):
    return set_similarity(movie1.get_keyword_ids(), movie2.get_keyword_ids())

def cast_similarity(movie1: Movie, movie2: Movie):
    return set_similarity(movie1.get_cast_ids(), movie2.get_cast_ids())

def director_similarity(movie1: Movie, movie2: Movie):
    return set_similarity(movie1.get_director_ids(), movie2.get_director_ids())

def movie_similarity(
    movie1: Movie, movie2: Movie, genre_weight: float=0.25, keyword_weight: float=0.25, cast_weight: float=0.25, director_weight: float=0.25
):
    genre_score = genre_similarity(movie1, movie2)
    keyword_score = keyword_similarity(movie1, movie2)
    cast_score = cast_similarity(movie1, movie2)
    director_score = director_similarity(movie1, movie2)
    overall_score = (
        genre_weight * genre_score
        + keyword_weight * keyword_score
        + cast_weight * cast_score
        + director_weight * director_score
    )
    return overall_score

def get_candidate_movie_ids(movie: Movie):
    candidate_ids = set()
    for page in range(1, 6):
        genre_results = find_candidate_movies(genres=movie.get_genre_ids(), page=page)
        keyword_results = find_candidate_movies(keywords=movie.get_keyword_ids(), page=page)
        cast_results = find_candidate_movies(cast=movie.get_cast_ids(), page = page)
        director_results = find_candidate_movies(director=movie.get_director_ids(), page=page)
        for genre_result in genre_results["results"]:
            candidate_ids.add(genre_result["id"])
        for keyword_result in keyword_results["results"]:
            candidate_ids.add(keyword_result["id"])
        for cast_result in cast_results["results"]:
            candidate_ids.add(cast_result["id"])
        for director_result in director_results["results"]:
            candidate_ids.add(director_result["id"])
    candidate_ids.discard(movie.movie_id)
    return list(candidate_ids)

def recommend_movies(movie: Movie, n: int=10):
    candidate_ids = get_candidate_movie_ids(movie)
    scored_candidates = []
    for movie_id in candidate_ids:
        candidate = get_movie_data(movie_id)
        score = movie_similarity(movie, candidate)
        scored_candidates.append((score, candidate))
    scored_candidates.sort(key=lambda item: item[0], reverse=True)
    return scored_candidates[:n]