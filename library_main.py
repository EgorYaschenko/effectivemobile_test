import time

from models import *

print('Добро пожаловать в нашу библиотеку!')

library = load_data('data.json')


seans = True
while seans:

    user_action = input(
        'Выберите операцию:\n\tДобавление книги [введи 1]\n'
        '\tУдаление книги [введи 2]\n'
        '\tПоиск книги [введи 3]'
        '\n\tОтображение всех книг [введи 4]\n'
        '\tИзменение статуса книги [введи 5]\n'
        '\tВыход из библиотеки [введи 0]\nВвод: ')

    if user_action == '1':
        title = input('Введи название книги: ')
        author = input('Введи автора книги: ')
        year = input('Введи год издания книги ')
        id = str(time.time()).split('.')[0]
        library.append(Library(id, title, author, year))

        print_info(library)
        save_data(library)
    elif user_action == '2':
        if not len(library):
            print('В библиотеке не хранится ни одной книги')
        else:
            id_del = input('Введи id книги, которую нужно удалить ')
            dell_book(id_del, library)

            print_info(library)
            save_data(library)
    elif user_action == '3':
        if not len(library):
            print('В библиотеке не хранится ни одной книги')
        else:
            select_search = input('Как ты хочешь найти книгу?\n'
                                  't- по заглавию, a- по автору, y- по году издания')
            message_search = {'t': 'Введи заглавие книги ', 'a': 'Введи автора книги ', 'y': 'Введи год издания книги'}
            search_value = input(message_search[select_search])
            select_books = search_book(search_value, library)
            print_info(select_books)
            # print(
            #     f'id: {select_book.id} {select_book.title}, автор: {select_book.author}, год издания: {select_book.year}. Cтатус - {select_book.status}')
    elif user_action == '4':
        if not len(library):
            print('В библиотеке не хранится ни одной книги')
        else:
            print_info(library)
    elif user_action == '5':
        if not len(library):
            print('В библиотеке не хранится ни одной книги')
        else:
            id_change = input('Введи id книги, чтобы изменить статус ')
            if control_id(id_change):
                select_book = search_book(id_change, library)
                if not select_book:
                    print('id не найден')
                    continue
                select_book[0].change_status()
                print_info(library)
                save_data(library)
            else:
                print('Неправильный id')
                continue
    elif user_action == '0':
        print('До встречи в нашей библиотеке')
        save_data(library)
        seans = False
    else:
        print('Я не знаю этой команды, попробуйте снова')
