"""
data_class.

Created by: Arkin E
Date: 16/02/2024
"""

# Import(s)
# from dataclasses import dataclass

# @dataclass
class CakeRecipe:
    """Information to bake a cake."""

    def __init__(self,
                name: str,
                serving_number: int,
                vegan_friendly: bool,
                garnishes: list[str]):
        """Create a cake recipe."""
        self.name = name
        self.serving_number = serving_number
        self.vegan_friendly = vegan_friendly
        self.garnishes = garnishes


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

for cake in my_cakes:
    print("---------------")
    print(f"Cake: {cake.name}")
    print(f"Serves: {cake.serving_number}")
    print(f"Vegan: {cake.vegan_friendly}")
    print("Garnish with:")
    for garnish in cake.garnishes:
        print(f"- {garnish}")