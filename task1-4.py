from abc import ABC, abstractmethod
from datetime import datetime as dt


class Printable(ABC):
    """
    Абстрактный базовый класс Printable определяет интерфейс для объектов,
    которые могут быть напечатаны.
    """
    @abstractmethod
    def print_info(self):
        pass


class Book(ABC):
    """
    Класс Book представляет книгу с атрибутами title, author и year.
    Методы класса:
    info(): возвращает строку с информацией о книге.
    __str__(): возвращает строковое представление объекта книги.
    __eq__(): сравнивает две книги на равенство по атрибутам.
    from_string(): создает объект книги из строки с данными.
    print_info(): выводит информацию о книге на экран.
    Свойство book_age:
    book_age: возвращает возраст книги в годах.
    book_age.setter: позволяет установить возраст книги, изменяя год издания.
    """
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return (f"Название:{self.title}, Автор:{self.author}, "
                f"Год издания:{self.year}"
                )

    def __str__(self):
        return f"{self.title} {self.author} {self.year}"

    def __eq__(self, other):
        return (isinstance(other, Book)
                and self.title == other.title
                and self.author == other.author
                and self.year == other.year
                )

    def print_info(self):
        print(self.info())

    @property
    def book_age(self):
        current_year = dt.now().year
        return current_year - self.year

    @book_age.setter
    def book_age(self, age):
        current_year = dt.now().year
        self.year = current_year - age

    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(",")
        # .stip() удаляет пробелы в начале и конце строки,
        #  на случай ошибки ввода
        return cls(title.strip(), author.strip(), int(year.strip()))


class EBook(Book):
    def __init__(self, title, author, year, format):
        # super() используется для вызова конструктора родительского класса
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return (f"Название:{self.title}, Автор:{self.author}, "
                f"Год издания:{self.year}, Формат:{self.format}"
                )
