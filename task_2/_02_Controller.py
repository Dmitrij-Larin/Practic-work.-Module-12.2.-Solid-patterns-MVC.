from _01_Model import Article


class ArticleController:
    def __init__(self):
        self.articles = []

    def create_article(self, title, author, content, publication, description):
        article = Article(title, author, content, publication, description)
        self.articles.append(article)
        return article

    def get_articles(self):
        return self.articles
