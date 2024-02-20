"""
Task_1.

Created by: Arkin E
Date: 20.02.2024
"""

class BasketballPlayer:
    def __init__(self, name: str, num_games_played: int, total_goals) -> None:
        self.name = name
        self.num_games_played = num_games_played
        self.total_goals = total_goals

    # agg is average goals per game
    def calulate_agg(self):
        return self.total_goals / self.num_games_played

    def display_average(self):
        print(f"{self.name}, Average goals per game: {self.calulate_agg()}")

player_1 = BasketballPlayer("Karen", 20, 80)
player_1.display_average()
