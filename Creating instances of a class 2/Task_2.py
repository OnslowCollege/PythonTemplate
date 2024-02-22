"""
Task_1.

Created by: Arkin E
Date: 20.02.2024
"""

class Movie:
    def __init__(self, title: str,
                 director: str, date: int, 
                 rating: float, genre: str):
        self.title = title
        self.director = director
        self.date = date
        self.rating = rating
        self.genre = genre