from Library import Library

main_text = '''\nadd_book - добавить книгу в библиотеку,
del_book - удалить книгу из библиотеки,
search_book - поиск книги в библиотеке,
display_books - вывести весь список книг в библиотеке,
change_status - указать статус книги(в наличии/выдана),
exit - для выхода из программы
Введите действие: '''

if __name__ == '__main__':
    lib = Library('library.txt')
    print('Вас приветствует система управления библиотекой.')

    while (text := input(main_text)) != 'exit':
        if hasattr(lib, text):
            msg = getattr(lib, text)()
            if msg:
                print(msg)
        else:
            print('Неправильная команда. Повторите ввод!')