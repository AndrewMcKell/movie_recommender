class Movie:
    def __init__(
        self,
        movie_id: int,
        title: str,
        release_year: int,
        overview: str,
        genres: list[dict],
        keywords: list[dict],
        director: list[dict],
        cast: list[dict],
    ):
        self.movie_id = movie_id
        self.title = title
        self.release_year = release_year
        self.overview = overview
        self.genres = genres
        self.keywords = keywords
        self.director = director
        self.cast = cast

    def get_genre_ids(self):
        genre_ids = []
        for genre in self.genres:
            genre_ids.append(genre["id"])
        return genre_ids

    def get_keyword_ids(self):
        keyword_ids = []
        for keyword in self.keywords:
            keyword_ids.append(keyword["id"])
        return keyword_ids

    def get_cast_ids(self):
        cast_ids = []
        for actor in self.cast:
            cast_ids.append(actor["id"])
        return cast_ids

    def get_director_ids(self):
        director_ids = []
        for director in self.director:
            director_ids.append(director["id"])
        return director_ids