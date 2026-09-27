from movie import Movie

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

def movie_similarity(movie1: Movie, movie2: Movie):
    genre_score = genre_similarity(movie1, movie2)
    keyword_score = keyword_similarity(movie1, movie2)
    cast_score = cast_similarity(movie1, movie2)
    director_score = director_similarity(movie1, movie2)
    overall_score = (
        0.25 * genre_score
        + 0.25 * keyword_score
        + 0.25 * cast_score
        + 0.25 * director_score
    )
    return overall_score