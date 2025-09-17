book_list = []
class Library:
    def __init__(self):
        pass
    def add_book(book):
        book_list.append(book)
    def remove_book(book):
        book_list.remove(book)
    def show_all_books():
        print("--- Library Catalog ---")
        print(f"Book: {Book.title} by {Book.author}")
        print(f"EBook: {Ebook.title} by {Ebook.author}")
        print(f"AudioBook: {Audiobook.title} by {Audiobook.author}")

class Book:
    def __init__(self, titleValue, authorValue):
        self.title = titleValue
        self.author = authorValue
    def show_info(self):
        print(f"The book is called {self.title} and is written by {self.author}")

class Ebook(Book):
    def __init__(self):
        super().__init__()
    def download(self):
        print(f"You downloaded {self.title} by {self.author}")

class Audiobook(Book):
    def __init__(self):
        super().__init__()
    def play_sample(self):
        print(f"The book {self.title} by {self.author} is sample playing")

