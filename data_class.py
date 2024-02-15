"""
data_class.

Created by: Arkin E
Date: 16/02/2024
"""

# Import(s)
from dataclasses import dataclass

@dataclass
class CakeRecipe:
    """Information to bake a cake."""
    name: str
    serving_number: int
    vegan_friendly: bool
    garnishes: list[str]

banana_cake = CakeRecipe(
    "Banana Cake",
    4,
    True,
    ["Vegan ganache", "Candles",
    "Banana slices"]
)

shortcake = CakeRecipe("Strawberry Shortcake", 1, False,
    ["Edible ball bearings"]
)

sponge_cake = CakeRecipe("Vinally sponge", 12, False, [])

print(banana_cake.name)