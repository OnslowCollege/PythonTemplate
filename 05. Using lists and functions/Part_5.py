"""
Part_5.py.

Created by: Arkin E
Date: 28.02.2024
"""


class Helicopter:
    def __init__(self, number):
        self.number = number

    def down(self):
        print(f"{self.number} down")

    def up(self):
        print(f"{self.number} up")

def main():
    helicopters = []
    for i in range(100):
        helicopters.append(Helicopter(i + 1))  # Create helicopters with numbers 1-100

    # Call up for the first 50
    for chopper in helicopters[:50]:
        chopper.up()

    # Call down for the next 50
    for chopper in helicopters[50:]:
        chopper.down()

if __name__ == "__main__":
    main()
