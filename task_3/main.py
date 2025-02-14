from _02_Controller import MovieController
from _03_View import MovieView


if __name__ == '__main__':
    controller = MovieController()

    movie1 = controller.create_movie(
        title="Остров проклятых",
        genre="Триллер",
        director="Мартин Скорсезе",
        year=2009,
        duration=138,
        studio="Paramount"
    )

    controller.add_actor_to_movie(movie1, "Леонардо ДиКаприо", "Тедди Дэниелс")
    controller.add_actor_to_movie(movie1, "Марк Руфффало", "Чак Ауль")
    controller.add_actor_to_movie(movie1, "Бен Кингсли", "Доктор Коули")
    controller.add_actor_to_movie(movie1, "Макс фон Сюдов", "Доктор Нейринг\n")

    movie2 = controller.create_movie(
        title="Драйв",
        genre="Криминал",
        director="Николас Виндинг Рефн",
        year=2011,
        duration=100,
        studio="Bold Films"
    )

    controller.add_actor_to_movie(movie2, "Райан Гослинг", "Драйвер")
    controller.add_actor_to_movie(movie2, "Кэри Маллиган", "Ирэн")
    controller.add_actor_to_movie(movie2, "Брайан Крэнстон", "Шеннон")
    controller.add_actor_to_movie(movie2, "Альберт Брукс", "Барни Рос")

    movies = controller.get_movies()
    MovieView.display_all_movies(movies)
