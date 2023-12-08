class Author:
    """Each instance represents an uniq author in the library"""
    def __init__(self, name: str, country: str, birthday: str, books=None):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = [] if books is None else books

    def __eq__(self, other):
        return self.name == other.name and self.country == other.country and self.birthday == other.birthday

    def __str__(self):
        bl = [b.name for b in self.books]
        bs = "'" + "', '".join(bl) + "'"
        return f"class Author\nName: {self.name} \nCountry: {self.country} \nBirthday: {self.birthday} \nBooks: {bs}"


class Book:
    """Each instance represents an uniq book in the library"""
    __book_amount = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f"Book name: {self.name} \tYear: {self.year} \tAuthor: {self.author.name}"

    @classmethod
    def add_amount(cls):
        cls.__book_amount += 1

    @classmethod
    def get_amount(cls):
        return cls.__book_amount


class Library:
    """Represents a library database and methods for working with it"""

    def __init__(self, name: str, books=None, authors=None):
        self.name = name
        self.books = [] if books is None else books
        self.authors = [] if authors is None else authors

    def __str__(self):
        bl = [" - " + str(b) for b in self.books]
        bs = "\n".join(bl)
        return f"class Library \nName: {self.name} \nBooks: \n{bs}"

    def new_book(self, name: str, year: int, author: Author) -> Book:
        if author in self.authors:
            for a in self.authors:
                if a == author:
                    author = a
                    break
            book = Book(name, year, author)
            author.books.append(book)
            self.books.append(book)
            Book.add_amount()
            return book
        else:
            self.authors.append(author)
            book = Book(name, year, author)
            author.books.append(book)
            self.books.append(book)
            Book.add_amount()
            return book

    def group_by_author(self, author: Author) -> list | None:
        if author in self.authors:
            return author.books[:]

    def group_by_year(self, year: int) -> list:
        return [b for b in self.books if b.year == year]

    @staticmethod
    def get_book_amount():
        return Book.get_amount()
