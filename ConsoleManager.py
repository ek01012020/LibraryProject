"""
Модуль ConsoleManager отвечает за ввод пользователем значений, их проверкой и вывод информации на экран.
"""

search_text = '''\nДля поиска книги укажите критерий поиска:
title - поиск по названию книги,
author - поиск по автору,
year - поиск по году издания книги
exit - для выхода из поиска
Введите действие: '''


class ConsoleManager:
    @staticmethod
    def add_book():
        """Метод запрашивает информацию о книге и проверяет корректность ввода"""
        print('Введите информацию о новой книге:')
        title, author = input('title: '), input('author: ')
        while True:
            if (year := input('year: ')).isdigit():
                return title, author, year
            print('Вы ввели недопустимое значение')

    @staticmethod
    def del_book(keys):
        """Метод запрашивает информацию id книги для удаления и проверяет корректность ввода"""
        while True:
            if (id := input('Введите id книги для удаления: ')).isdigit():
                if int(id) not in keys:
                    print(f'Книга с {id = } отсутствует в библиотеке')
                return int(id)
            else:
                print('Вы ввели недопустимое значение')

    @staticmethod
    def search_book():
        """Метод запрашивает информацию о критериях поиска и проверяет корректность ввода"""
        while (search_in := input(search_text)) != 'exit':
            if search_in in ('title', 'author', 'year'):
                break
        if search_in == 'year':
            while True:
                if (year := input('year: ')).isdigit():
                    return search_in, year
                print('Вы ввели недопустимое значение')
        else:
            return search_in, input('Введите значение - ')

    @staticmethod
    def change_status(keys):
        """Метод запрашивает id книги и новый статус и проверяет корректность ввода"""
        while True:
            if (id := input('Введите id книги для изменения статуса: ')).isdigit():
                id = int(id)
                if id not in keys:
                    print(f'Книга с {id = } отсутствует в библиотеке')
                break
            else:
                print('Вы ввели недопустимое значение')
        while id in keys:
            if (status := input('Введите статус(в наличии/выдана): ')) not in ('в наличии', 'выдана'):
                print('Неизвестный статус книги')
                continue
            else:
                return id, status
        return None, None

    @staticmethod
    def print_list(data: list):
        """Метод распечатывает список объектов на экран"""
        for el in data:
            print(el)
