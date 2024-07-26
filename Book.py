"""
Модуль Book отвечает за создание класса книги.
Поля: id книги, название книги, автор, год выпуска и статус книги: выдана/в наличии
"""


class Book:
    """Класс отвечает за хранение данных о книге"""
    def __init__(self, id: int, title: str, author: str, year: str, status: str = 'в наличии'):
        self._id = int(id)
        self._title = title
        self._author = author
        self._year = year
        self.status = status

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id},{self.title},{self.author},{self.year},{self.status})'

    def __str__(self):
        return f'Book: id - {self._id}, title - {self.title}, author - {self.author}, year - {self.year}'
