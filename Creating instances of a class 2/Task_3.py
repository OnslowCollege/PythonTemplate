"""
Task_3.

Created by: Arkin E
Date: 22.02.2024
"""

class Country:
    def __init__(self, name: str, continent: str, leader: str,
                capital: str, population: int, land_area: int):
        self.name = name
        self.continent = continent
        self.leader = leader
        self.capital = capital
        self.population = population
        self.land_area = land_area

    def calculate_population_density(self) -> float:
        if self.land_area > 0:
            return self.population / self.land_area
        # Handle cases with zero land area
        else:
            return 0.0
    def display_data(self):
        print(f"Country name: {self.name}")
        print(f"Continent: {self.continent}")
        print(f"Leader: {self.leader}")
        print(f"Capital: {self.capital}")
        print(f"Population: {self.population:,}")  # Use comma separator for readability
        print(f"Land Area: {self.land_area} km^2")
        print(f"Population Density: "
              f"{self.calculate_population_density():.2f} people/km^2")

# Create some country objects
ireland = Country("Ireland", "Europe", "Micheal Martin", "Dublin", 6399152, 84421)
china = Country("China", "Asia", "Xi Jinping", "Beijing", 1444400000, 9596961)
brazil = Country("Brazil", "South America", "Jair Bolsonaro", "Brasília", 215322959, 8515767)

# Display their data
print("\nCountry Details:")
ireland.display_data()
print("\n---")
china.display_data()
print("\n---")
brazil.display_data()
