"""
Task_1.

Created by: Arkin E
Date: 20.02.2024
"""

class Movie:
    def __init__(self, title: str, release_year: int,
                 production_cost: float, box_office_earnings: float):

        self.title = title
        self.release_year = release_year
        self.production_cost = float(production_cost)
        self.box_office_earnings = float(box_office_earnings)

    def calculate_net_profit(self):
        """Calculates and returns the net profit of the movie."""
        self.net_profit = self.box_office_earnings - self.production_cost
        return self.net_profit

    def display_data(self):
        """Displays the movie's details, including calculated net profit."""
        print(f"Title: {self.title}")
        print(f"Release Year: {self.release_year}")
        print(f"Production Cost: ${self.production_cost:.2f}")
        print(f"Box Office Earnings: ${self.box_office_earnings:.2f}")
        print(f"Net Profit: ${self.calculate_net_profit():.2f}")


"""Creates and displays Movie objects with calculated net profits."""
movie1 = Movie("Avatar", 2009, 237000000, 2922917914)
movie2 = Movie("Avengers: Endgame", 2019, 356000000, 2797501369)
movie3 = Movie("Titanic", 1997, 200000000, 2229263212)

print("\nMovie Details:")
movie1.display_data()
print("\n---")
movie2.display_data()
print("\n---")
movie3.display_data()
