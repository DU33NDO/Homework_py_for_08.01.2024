# название книги, год выпуска, издателя, жанр, автора, цену. #
class Book:
    def __init__(self):
        self.name = None
        self.year_of_release = None
        self.manufacturer = None
        self.genre = None
        self.author = None
        self.cost = None

    def __repr__(self):
        return f"Name of a book: {self.name}, Year of release: {self.year_of_release}, Manufacturer: {self.manufacturer}, Genre: {self.genre}, Author: {self.author}, Cost: {self.cost} tenge"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_year_of_release(self):
        return self.get_year_of_release

    def set_year_of_release(self, year_of_release):
        self.year_of_release = year_of_release

    def get_manufacturer(self):
        return self.manufacturer

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_genre(self):
        return self.genre

    def sete_genre(self, genre):
        self.genre = genre

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost


name = input("name: ")
year_of_release = int(input("Year of release: "))
manufacturer = input("manufacturer: ")
genre = input("Genre: ")
author = input("author: ")
cost = int(input("cost in tenge: "))

ex1 = Book()
ex1.set_name(name)
ex1.set_year_of_release(year_of_release)
ex1.set_manufacturer(manufacturer)
ex1.sete_genre(genre)
ex1.set_author(author)
ex1.set_cost(cost)
print(ex1)
