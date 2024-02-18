"""
class_instances.py.

Created by: Arkin E
Date: 19/02/2024
"""

class Film:
    def __init__(self, title: str, director: str, year: int):
       self.title = title
       self.director = director
       self.year_published = year_published

classic_film = Film("Gone with the Wind", "Victor Fleming", 1939)
modern_film = Film("Barbie", "Greta Gerwig", 2023)

print(classic_film.title + " " + modern_film.director)

