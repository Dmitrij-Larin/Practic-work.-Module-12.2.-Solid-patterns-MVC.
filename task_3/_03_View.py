class MovieView:
    @staticmethod
    def display_movie(movie):
        print(movie)

    @staticmethod
    def display_all_movies(movies):
        if not movies:
            print("Нет доступных фильмов.")
        else:
            for movie in movies:
                MovieView.display_movie(movie)