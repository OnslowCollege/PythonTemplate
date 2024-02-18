"""
class_instances.py.

Created by: Arkin E
Date: 19/02/2024
"""

class Film:
    """Class that stores films and information regarding."""

    def __init__(self, title: str, director: str, year_published: int,
                 genre: str, imbd_rating: float):
        """Instance of film."""
        self.title = title
        self.director = director
        self.year_published = year_published
        self.genre = genre
        self.imbd_rating = imbd_rating

    def description(self):
        """Print out film and description."""
        print(f"{self.title} ({self.year_published}):"
                f"\nDirector:{self.director}")

classic_film = Film("Gone with the Wind", "Victor Fleming",
                    1939, "Drama", 8.2)
modern_film = Film("Barbie", "Greta Gerwig", 2023, "Comedy", 6.9)

print(classic_film.title + " " + modern_film.director)

classic_film.description()
