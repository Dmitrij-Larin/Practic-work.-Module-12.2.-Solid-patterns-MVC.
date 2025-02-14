from _02_Controller import ArticleController
from _03_view import ArticleView

if __name__ == '__main__':
    controller = ArticleController()

    controller.create_article(
        title="Исследования Солнечной системы — 2022–2024.",
        author="Лев Каменцев",
        content="Также продолжают исследования Солнца и солнечно-земных связей запущенные в предыдущие годы ACE "
                "(Advanced Composition Explorer), SOHO (Solar and Heliospheric Observatory) и DSCOVR (Deep Space Climate "
                "Observatory) в точке Лагранжа L1 системы Солнце — Земля.",
        publication="Троицкий вариант — Наука» №1(420)",
        description="Успехи в изучении объектов Солнечной системы благодаря космическим аппаратам.\n"
    )

    controller.create_article(
        title="Как доказать, что мы живем не в матрице?",
        author="EDUCON.BY",
        content="После выхода на широкий экран фильма «Матрица» и его продолжений, многие люди задумались: "
                "а действительно, не живем ли мы все в матрице? Как же доказать, что это действительно не так?",
        publication="https://educon.by/index.php/pozn/filosofia/94-kak-dokazat-chto-my-zhivem-ne-v-matritse",
        description="Объяснение доказательства, что мы живём не в матрице."
    )

    articles = controller.get_articles()
    ArticleView.display_all_articles(articles)
