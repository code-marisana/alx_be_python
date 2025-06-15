class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def return_book(self):
            if self._is_checked_out:
                    self._is_checked_out = False
            else:
                print(f"Book already returned!")

    def check_out_book(self):
            if self._is_checked_out:
                print(f"{self.title} is unavailable")
            else:
                self._is_checked_out = True

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self,book):
        self._books.append(book)
          
    
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")

    def return_book(self, title):
         for book in self._books:
              if book.title == title:
                   book.return_book()

    def check_out_book(self, title):
         for book in self._books:
              if book.title == title:
                   book.check_out_book()