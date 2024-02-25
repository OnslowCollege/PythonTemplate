"""
Task_4.

Created by: Arkin E
Date: 22.02.2024
"""

class CellPhone:

    def __init__(self, make, model, year, price, camera=False, internet=False):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.camera = camera
        self.internet = internet

    def display_data(self):
        camera_str = "with camera" if self.camera else "without camera"
        internet_str = "with internet access" if self.internet \
            else "without internet access"
        print(f"Make: {self.make}, Model: {self.model},"
            f"Year: {self.year}, Price: ${self.price:.2f}")
        print(f"Features: {camera_str}, {internet_str}")

    def depreciated_value(self, years):
        depreciation_rate = 0.67
        depreciated_value = self.price * (1 - depreciation_rate) ** years
        return f"Depreciated value after {years} years: ${depreciated_value:.2f}"


p1 = CellPhone("Nokia", "6610", 2002, 400)
p2 = CellPhone("Samsung", "Galaxy S3", 2012, 600, True, True)
p3 = CellPhone("Apple", "iPhone X", 2017, 1000, True, True)

p1.display_data()
print(p1.depreciated_value(9))  # 9 years since 2002

p2.display_data()
print(p2.depreciated_value(12))  # 12 years since 2012

p3.display_data()
print(p3.depreciated_value(7))  # 7 years since 2017
