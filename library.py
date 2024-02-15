"""
library_catalogue.

Created: by Arkin
Date: 14/02/2024
"""

class Book:
    """Create books."""
    def __init__(self) -> None:
        self.title: str
        self.author: str
        self.isbn: int
        self.availability: bool

class LibraryCatalogue:
    """Stores books."""



"Huwi's First Egg", "Kat Mereweather", 123, (1 copy available)
"The Kuia and the Spider", "Patricia Grace", 124, (1 copy available)
"Hairy Maclary from Donaldson's Dairy", "Lynley Dodd", 125, (1 copy loaned)
"Where the Wild Things Are", "Maurice Sendak", 345, (2 copies available)
"Under the Mountain", "Maurice Gee", 346, (1 copy available)
"Horrakapotchkin", "Margaret Mahy", 347, (1 copy available)
"Salmagundi", "Joy Cowley", 409, (1 copy available, 1 copy loaned)
"How Māui Found His Father and the Magic Jawbone", "Peter Gossage", 410, 2