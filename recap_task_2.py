"""
recap_task_2.

Created by: Arkin
Date: 12/02/2024
"""

# Variables
highest_bid: float = 0
current_bid: float = -1
bidders_name: str = ""
bidding_history: dict = {}
reserve_price: float = -1
main_loop: bool = True


# Main loop
while main_loop:
    reserve_price = -1

    while reserve_price < 0:
        try:
            reserve_price = float(input("What is the reserve price? ($): "))

            if reserve_price < 0:
                print("Please enter a number 0 or above.")

        except ValueError:
            print("Please enter a number 0 or above.")

    print("Action has started")
    print(f"Current highest bid is ${highest_bid}")

    bidders_name = input("What is your name? (Y/N to finish) ")

    if bidders_name.lower() == "y" or bidders_name.lower() == "n":
        main_loop = False

        for bidder in bidding_history.keys():
            print(f"{bidder}, bid {bidding_history[bidder]}$")
    else:
        while current_bid < highest_bid:
            try:
                current_bid = float(input("\nWhat is your bid? ($): "))

                if current_bid <= highest_bid:
                    print("Your bid isn't high enough!"
                        f"\nPlease enter amount above ${highest_bid}")

                else:
                    highest_bid = current_bid
                    bidding_history[bidders_name] = highest_bid
            except ValueError:
                print(f"Please enter a number above ${highest_bid}.")
