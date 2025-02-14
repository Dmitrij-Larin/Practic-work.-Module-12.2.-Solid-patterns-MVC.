class Actor:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"Актёр - {self.name}. Роль - {self.role}"


class Movie:
    def __init__(self, title, genre, director, year, duration, studio):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = []

    def add_actor(self, name, role):
        actor = Actor(name, role)
        self.actors.append(actor)

    def __str__(self):
        actors_str = "\n".join(str(actor) for actor in self.actors)
        return (f"Фильм: {self.title}\n"
                f"Жанр: {self.genre}\n"
                f"Режиссер: {self.director}\n"
                f"Год выпуска: {self.year}\n"
                f"Длительность: {self.duration} минут\n"
                f"Студия: {self.studio}\n"
                f"Актеры: \n{actors_str}")
