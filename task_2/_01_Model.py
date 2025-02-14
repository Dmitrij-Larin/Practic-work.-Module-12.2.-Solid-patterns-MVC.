class Article:
    def __init__(self, title, author, content, publication, description):
        self.title = title
        self.author = author
        self.content = content
        self.publication = publication
        self.description = description

    def get_character_count(self):
        return len(self.content)

    def __str__(self):
        return (f"Статья: {self.title}\n"
                f"Автор: {self.author}\n"
                f"Контент: {self.content}\n"
                f"Количество знаков: {self.get_character_count()}\n"
                f"Публикация: {self.publication}\n"
                f"Описание: {self.description}")

