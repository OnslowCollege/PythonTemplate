"""
library_catalogue.

Created: by Arkin
Date: 14/02/2024
"""

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    isbn: int
    availability: bool = True  # Default to available

books = [
    Book("Huwi's First Egg", "Kat Mereweather", 123, True),
    Book("The Kuia and the Spider", "Patricia Grace", 124, True),
    Book("Where the Wild Things Are", "Maurice Sendak", 345, True, 2),
    Book("Under the Mountain", "Maurice Gee", 346, True, 1),
    Book("How Māui Found His Father and the Magic Jawbone", "Peter Gossage", 410, True, 2),
]


class LibraryCatalogue:
    def __init__(self):
        self.books = books

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, isbn: int):
        for index, book in enumerate(self.books):
            if book.isbn == isbn:
                self.books.pop(index)
                print(f"Book with ISBN {isbn} removed successfully.")
                return
        print(f"Book with ISBN {isbn} not found in library.")

    def search_by_title(self, title: str):
        matches = [book for book in self.books if title.lower() in book.title.lower()]
        if matches:
            print(f"Found {len(matches)} books matching '{title}':")
            for book in matches:
                print(f"  - {book.title} by {book.author} ({book.isbn})")
                if book.availability:
                    print(f"      - Available for issue")
                else:
                    print(f"      - Currently unavailable")
        else:
            print(f"No books found matching '{title}'.")

    def search_by_isbn(self, isbn: int):
        for book in self.books:
            if book.isbn == isbn:
                print(f"Book with ISBN {isbn}:")
                print(f"  - Title: {book.title}")
                print(f"  - Author: {book.author}")
                if book.availability:
                    print(f"      - Available for issue")
                else:
                    print(f"      - Currently unavailable")
                return
        print(f"Book with ISBN {isbn} not found in library.")

    def list_books(self):
        print("**Library Catalogue**")
        for book in self.books:
            print(f"  - {book.title} by {book.author}")


def main():
    catalogue = LibraryCatalogue()

    while True:
        print("\nLibrary Menu:")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search by title")
        print("4. Search by ISBN")
        print("5. List all books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = int(input("Enter ISBN: "))
            catalogue.add_book(Book(title, author, isbn))
            print("Book added successfully.")
        elif choice == "2":
            isbn = int(input("Enter ISBN of book to remove: "))
            catalogue.remove_book(isbn)
        elif choice == "3":
            title = input("Enter book title to search: ")
            catalogue.search_by_title(title)
        elif choice == "4":
            isbn = int(input("Enter ISBN to search: "))
            catalogue.search_by_isbn(isbn)
        elif choice == "5":
            catalogue.list_books()
        elif choice == "6":
            print("Exiting library program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()