from search_movies import search_movies_by_title, get_movie_data
from recommender import recommend_movies

def select_movie(results: list[dict]):
    if not results:
        print("No movies found. Try another title.")
        return None
    options = results[:10]
    print("\nMatching movies:")

    for number, movie in enumerate(options, start=1):
        year = movie.get("release_date", "")[:4]
        print(f"{number}. {movie["title"]} ({year})")

    while True:
        answer = input("\nEnter the number of your chosen movie, or press Enter to search again: ")
        if not answer:
            return None
        try:
            selection = int(answer)
        except ValueError:
            print("Please enter the number of your chosen movie")
            continue
        if 1 <= selection <= len(options):
            return options[selection - 1]
        print(f"Please enter a number from 1 to {len(options)}")

def main():
    print("Movie Recommender")
    print("Enter a movie title, or type 'quit' to exit")

    while True:
        title = input("\nMovie title: ")
        if title.lower() == "quit":
            break
        if not title:
            print("Please enter a movie title")
            continue

        search_results = search_movies_by_title(title)
        selected_movie = select_movie(search_results)
        if selected_movie is None:
            continue
        selected_movie_id = selected_movie["id"]
        movie = get_movie_data(selected_movie_id)

        print(f"\nSelected: {movie.title} ({movie.release_year})")
        print("Finding recommendations...")

        recommendations = recommend_movies(movie)

        print("\nRecommendations:")
        for rank, (score, recommendation) in enumerate(recommendations, start=1):
            print(f"{rank}. {recommendation.title} ({recommendation.release_year}) - similarity score: {score:.3f}")

if __name__ == "__main__":
    main()