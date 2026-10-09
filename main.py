from search_movies import search_movie_by_title, get_movie_data
from recommender import recommend_movies

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

        search_result = search_movie_by_title(title)
        search_result_id = search_result["id"]
        movie = get_movie_data(search_result_id)

        print(f"\nSelected: {movie.title} ({movie.release_year})")
        print("Finding recommendations...")

        recommendations = recommend_movies(movie)

        print("\nRecommendations:")
        for rank, (score, recommendation) in enumerate(recommendations, start=1):
            print(f"{rank}. {recommendation.title} ({recommendation.release_year}) - similarity score: {score}")

if __name__ == "__main__":
    main()