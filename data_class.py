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

my_cakes = [
    CakeRecipe("Banana Cake", 4 , True,
               ["Vegan ganache", "Candles",
                "Banana slices"]
    ),
    CakeRecipe("Strawberry Shortcake", 1, False,
               ["Edible ball bearings"]
    ),
    CakeRecipe("Vinally sponge", 12, False, []
    )
]

my_cakes.append(
    CakeRecipe("Chocolate Cake", 1, True,
        ["Cook's blood", "Sweat", "Tears"]
    )
)

print(banana_cake.name)