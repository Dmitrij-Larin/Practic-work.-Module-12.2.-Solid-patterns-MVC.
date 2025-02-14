from _01_Model import Movie


class MovieController:
    def __init__(self):
        self.movies = []

    def create_movie(self, title, genre, director, year, duration, studio):
        movie = Movie(title, genre, director, year, duration, studio)
        self.movies.append(movie)
        return movie

    def add_actor_to_movie(self, movie, name, role):
        movie.add_actor(name, role)

    def get_movies(self):
        return self.movies
