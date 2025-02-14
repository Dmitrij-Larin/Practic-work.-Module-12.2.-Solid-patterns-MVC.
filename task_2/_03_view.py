class ArticleView:
    @staticmethod
    def display_article(article):
        print(article)

    @staticmethod
    def display_all_articles(articles):
        if not articles:
            print("Нет доступных статей.")
        for article in articles:
            ArticleView.display_article(article)