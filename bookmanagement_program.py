from datetime import datetime, timedelta

class BookManagement:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def register_book(self, title, author):
        if title in self.books:
            print(f"'{title}' is already registered.")
        else:
            self.books[title] = author
            print(f"'{title}' by {author} has been registered.")

    def borrow_book(self, title, borrower):
        if title not in self.books:
            print(f"'{title}' is not available in the library.")
        elif title in self.borrowed_books:
            print(f"'{title}' is already borrowed by {self.borrowed_books[title]['borrower']}.")
        else:
            due_date = datetime.now() + timedelta(weeks=2)
            self.borrowed_books[title] = {'borrower': borrower, 'due_date': due_date}
            print(f"'{title}' has been borrowed by {borrower}. Due date is {due_date.strftime('%Y-%m-%d')}.")

    def return_book(self, title):
        if title in self.borrowed_books:
            del self.borrowed_books[title]
            print(f"'{title}' has been returned.")
        else:
            print(f"'{title}' was not borrowed.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for title, author in self.books.items():
                status = "Available" if title not in self.borrowed_books else f"Borrowed by {self.borrowed_books[title]['borrower']}"
                print(f"'{title}' by {author} - {status}")

if __name__ == "__main__":
    bm = BookManagement()
    bm.register_book("The Great Gatsby", "F. Scott Fitzgerald")
    bm.register_book("1984", "George Orwell")
    bm.list_books()
    bm.borrow_book("1984", "John Doe")
    bm.list_books()
    bm.return_book("1984")
    bm.list_books()