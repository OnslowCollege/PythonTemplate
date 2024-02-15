"""
library_catalogue.

Created: by Arkin
Date: 14/02/2024
"""

# Imports
from dataclasses import dataclass

# Book class
@dataclass
class Book:
    """Stores book values."""

    # Values for book
    title: str
    author: str
    isbn: int
    availability: bool = True  # Default to available

# Add some books thru book class
books = [
    Book("Huwi's First Egg", "Kat Mereweather", 123, True),
    Book("The Kuia and the Spider", "Patricia Grace", 124, True),
    Book("Where the Wild Things Are", "Maurice Sendak", 345, True),
    Book("Under the Mountain", "Maurice Gee", 346, True),
    Book("How Māui Found His Father and the Magic Jawbone",
         "Peter Gossage", 410, True),
]


# Catalogue class for saving books
class LibraryCatalogue:
    """Stores books in cataloge."""

    def __init__(self):
        """Add the details from the book."""
        self.books = books

    # Function to add a book
    def add_book(self, book: Book):
        """Add a book function."""
        self.books.append(book)

    # Function to remove a book
    def remove_book(self, isbn: int):
        """Remove a book from saved list."""

        # Check book by isbn
        for index, book in enumerate(self.books):
            if book.isbn == isbn:

                # Remove book
                self.books.pop(index)
                print(f"Book with ISBN {isbn} removed successfully.")
                return

        # If isbn was not found
        print(f"Book with ISBN {isbn} not found in library.")

    # Search for book by title
    def search_by_title(self, title: str):
        """Search for books by title."""

        # Check if book was found
        matches = [book for book in self.books if title.lower() \
                   in book.title.lower()]

        # If book was found print book and details
        if matches:
            print(f"Found {len(matches)} books matching '{title}':")
            for book in matches:

                print(f"  - {book.title} by {book.author} ({book.isbn})")

                # If book is available or not print accordingly
                if book.availability:
                    print("      - Available for issue")
                else:
                    print("      - Currently unavailable")

        # If no books were found that matches the title
        else:
            print(f"No books found matching '{title}'.")

    # Search book by isbn and print details if can
    def search_by_isbn(self, isbn: int):
        """Look up book by entered isbn."""

        # Get books details and check if one matches the isbn given
        for book in self.books:
            if book.isbn == isbn:

                # Print details for the book
                print(f"Book with ISBN {isbn}:")
                print(f"  - Title: {book.title}")
                print(f"  - Author: {book.author}")

                # Print if book is available
                if book.availability:
                    print("      - Available for issue")
                else:
                    print("      - Currently unavailable")
                return

        # If isbn given doesn't match any book in list
        print(f"Book with ISBN {isbn} not found in library.")

    # List all the books and their details
    def list_books(self):
        """List out books."""

        print("**Library Catalogue**")
        for book in self.books:
            print(f"  - {book.title} by {book.author}")

# Main code for user interface
def main():
    """Get users input and call functions accordingly."""

    catalogue = LibraryCatalogue()

    # Print out options
    get_choice = True
    while get_choice:
        print("\nLibrary Menu:")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search by title")
        print("4. Search by ISBN")
        print("5. List all books")
        print("6. Exit")

        # Get choice
        choice = input("Enter your choice: ")

        # If user wants to add a book get details for book to add and do so
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = int(input("Enter ISBN: "))
            catalogue.add_book(Book(title, author, isbn))
            print("Book added successfully.")

        # If user wants to remove a book ask for isbn of book to remove
        elif choice == "2":
            isbn = int(input("Enter ISBN of book to remove: "))
            catalogue.remove_book(isbn)

        # If user wants to search for a book by title get title to search
        elif choice == "3":
            title = input("Enter book title to search: ")
            catalogue.search_by_title(title)

        # If user wants to search for a book by isbn get isbn to search
        elif choice == "4":
            isbn = int(input("Enter ISBN to search: "))
            catalogue.search_by_isbn(isbn)

        # If user wants to list out the books print out all books and details
        elif choice == "5":
            catalogue.list_books(isbn)

        # If user wants to stop the program stop the loop and exit code
        elif choice == "6":
            print("Exiting library program.")
            get_choice = False

        # If choice user entered was not listed
        else:
            print("Invalid choice. Please try again.")

# Initialize code
if __name__ == "__main__":
    main()
