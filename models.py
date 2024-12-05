import json
from constans import *


def load_data(file_name: str):
    """
    loading the saved library from a file
    :param file_name:
    :return:
    """
    librari = []
    with open(file_name, "r") as file:
        lib = json.load(file)
    for b in lib:
        librari.append(Library(b['id'], b['title'], b['author'], b['year'], b['status']))
    return librari


def save_data(librari: list):
    """
    save the library to a file
    :param librari:
    :return:
    """
    save_data = []
    for book in librari:
        save_data.append(book.__dict__)
    save_json = json.dumps(save_data)
    with open(DATA_LIBRARY, "w") as file:
        file.writelines(save_json)


def print_info(librari: list):
    """
    display the contents of the library
    :param librari:
    :return:
    """
    for l in librari:
        print(f'id: {l.id} {l.title}, автор: {l.author}, год издания: {l.year}. Cтатус - {l.status}')


def dell_book(id: str, librari: list):
    """
    remove a book from the library
    :param id:
    :param librari:
    :return:
    """
    for book in librari:
        if id == book.id:
            librari.remove(book)


def search_book(search_value: str, librari: list):
    """

    search for a book in the library
    :param search_value:
    :param librari:
    :return:
    """
    search_books=[]
    for book in librari:

        if search_value in [book.id, book.title, book.author, book.year]:
            search_books.append(book)

    if not search_books:
        print('Книга не найдена')
    return search_books

def control_id(id:str):
    """
     checking the correctness of id input
    """
    if id.isdigit():
        return True
    return False
class Library():
    def __init__(self, id, title, author, year, status='в наличии'):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def change_status(self):
        if self.status == 'в наличии':
            self.status = 'выдана'
        elif self.status == 'выдана':
            self.status = 'в наличии'
