class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self,book):
        self._books.append(book)
    
    def check_out_book(self, book_title):
        for book in self._books:
            if book.title == book_title:
                if book._is_checked_out:
                    print(f"{book_title} is unavailable")
                else:
                    book._is_checked_out = True

    def return_book(self, book_title):
        for book in self._books:
            if book.title == book_title:
                if book._is_checked_out:
                    book._is_checked_out = False
                else:
                    print(f"Book already returned!")
    

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")