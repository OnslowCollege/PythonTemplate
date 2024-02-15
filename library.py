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



"Huwi's First Egg", "Kat Mereweather", 123, 1
"The Kuia and the Spider", "Patricia Grace", 124, 1
"Where the Wild Things Are", "Maurice Sendak", 345, 2
"Under the Mountain", "Maurice Gee", 346, 1
"How Māui Found His Father and the Magic Jawbone", "Peter Gossage", 410, 2