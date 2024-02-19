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
        self.title = title if title.strip() != "" else "N/A"

        self.director = director if director.strip() != "" else "N/A"

        self.year_published = year_published if year_published >= 1878 \
                                and year_published <= 2024 else "N/A"

        self.genre = genre if genre.strip() != "" else "N/A"

        self.imbd_rating = imbd_rating if imbd_rating >= 0 \
                            and imbd_rating <= 10 else "N/A"

    def description(self):
        """Print out film and description."""
        print(f"\n{self.title} ({self.year_published}):"
                f"\nDirector: {self.director}"
                f"\nGenre: {self.genre}"
                f"\nIMBD Rating: {self.imbd_rating}")

classic_film = Film("Gone with the Wind", "Victor Fleming",
                    1939, "Drama", 8.2)
modern_film = Film("Barbie", "Greta Gerwig", 2023, "Comedy", 6.9)

print(classic_film.title + " " + modern_film.director)

classic_film.description()


class Car:
    def __init__(self, tank_size: float) -> None:
        pass