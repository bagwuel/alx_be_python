class Book:
    def __init__(self, title, authur):
        self.title = title
        self.author = authur
    
    def print_name(self):
                return(type(self).__name__)

    def get_name(self):
        return(f"{self.title} by {self.author}")

    def get_size(self):
        return("")



class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_size(self):
        return(f", File Size: {self.file_size}")



class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_size(self):
        return(f", Page Count: {self.page_count}")


class Library:
    def __init__(self):
        self._book = []

    def add_book(self, book):
        self._book.append(book)

    def list_books(self):
        for book in self._book:
            print(f"{book.print_name()}: {book.get_name()}{book.get_size()}")
