"""
Модуль Library содержит основную логику приложения: позволяет добавлять, удалять, отображать книги,
искать по автору, названию и году, а также изменять статус книги.
"""
from Book import Book
from ConsoleManager import ConsoleManager
from DataManager import DataManager


class Library(DataManager):
    """Класс отвечает за основные действия в приложении"""
    def __init__(self, filename: str):
        self.console = ConsoleManager()
        DataManager.__init__(self, filename)
        self.lib_dict = {}

    def add_book(self) -> str:
        """Метод добавляет книгу в бибилиотеку"""
        self.fill_dict()
        new_book = Book(self.new_id(), *self.console.add_book())
        id = new_book.id
        self.add_line(f'\n{id} {repr(new_book)}' if id != 1 else f'{id} {repr(new_book)}')
        return f'Книга добавлена в библиотеку'

    def del_book(self) -> str:
        """Метод удаляет книгу из библиотеки"""
        self.fill_dict()
        id = self.console.del_book(self.lib_dict.keys())
        if self.lib_dict.get(id, None):
            del self.lib_dict[id]
            if self.lib_dict:
                first_id = min(self.lib_dict)
                data = [f'\n{k} {repr(v)}' if k != first_id else f'{k} {repr(v)}' for k, v in self.lib_dict.items()]
            else:
                data = ''
            self.rewrite(data)
            return f'Книга с {id = } удалена'

    def search_book(self) -> str:
        """Метод осуществляет поиск книги по заданному критерию"""
        self.fill_dict()
        search_in, value = self.console.search_book()
        search_list = []
        for id, book in self.lib_dict.items():
            if value in getattr(book, search_in):
                search_list.append(book)
        if search_list:
            self.console.print_list(search_list)
        else:
            return f'Не найдено совпадений'

    def display_books(self):
        """Метод выводит на экран все книги из библиотеки"""
        self.console.print_list(self.read())

    def change_status(self):
        """Метод изменяет статус книги"""
        self.fill_dict()
        id, status = self.console.change_status(self.lib_dict.keys())
        if id:
            self.lib_dict[id].status = status
            first_id = min(self.lib_dict)
            data = [f'\n{k} {repr(val)}' if k != first_id else f'{k} {repr(val)}' for k, val in self.lib_dict.items()]
            self.rewrite(data)

    def new_id(self) -> int:
        """Метод выполняет функцию автоинкремента id"""
        if self.lib_dict:
            return max(self.lib_dict) + 1
        else:
            return 1

    def fill_dict(self):
        """Метод заполняет словарь key = id книги, value = класс Book"""
        for line in self.read():
            key, sep, value = line.partition(' ')
            self.lib_dict[int(key)] = Book(*value.strip('Book()').split(','))
