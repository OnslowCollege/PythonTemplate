"""
Part_5.py.

Created by: Arkin E
Date: 28.02.2024
"""

class House:
    def __init__(self, id, address, num_bedrooms, price, area):
        self.id = id
        self.address = address
        self.num_bedrooms = num_bedrooms
        self.price = price
        self.area = area

    def calculate_price_per_area(self):
        return self.price / self.area

    def calculate_price_per_room(self):
        return self.price / self.num_bedrooms

    def show_info(self):
        print(f"ID: {self.id}  Address: {self.address}")
        print(f"Number of bedrooms: {self.num_bedrooms}  Asking price: ${self.price:,}")
        print(f"Price by area ${self.calculate_price_per_area():,.0f}")
        print(f"Price per room ${self.calculate_price_per_room():,.0f}")
        print("**************")

def main():
    houses = []
    houses.append(House("DGB2354", "22 Helens Rd", 4, 320000, 240))
    houses.append(House("DGB2355", "2 Aston Crescent", 3, 110000, 190))
    houses.append(House("DGB2356", "5 Stratton St", 5, 550000, 380))

    for house in houses:
        house.show_info()

if __name__ == "__main__":
    main()
