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
get_bid_amount: bool = True

# Main loop
while main_loop:

    while reserve_price < 0:
        try:
            reserve_price = float(input("What is the reserve price? ($): "))

            if reserve_price < 0:
                print("Please enter a number 0 or above.")
            
            else:
                print("\nAction has started")

        except ValueError:
            print("Please enter a number 0 or above.")

    print(f"Current highest bid is ${highest_bid}")

    bidders_name = input("\nWhat is your name? ('F' to finish) ")

    if bidders_name.lower() == "f":
        main_loop = False

        for bidder in bidding_history.keys():
            print(f"{bidder}, bid {bidding_history[bidder]}$")
    else:
        get_bid_amount = True
        while get_bid_amount:
            try:
                current_bid = float(input("\nWhat is your bid? ($): "))

                if current_bid <= highest_bid:
                    print("Your bid isn't high enough!"
                        f"\nPlease enter amount above ${highest_bid}")

                else:
                    get_bid_amount = False
                    highest_bid = current_bid
                    bidding_history[bidders_name] = highest_bid
            except ValueError:
                print(f"Please enter a number above ${highest_bid}.")
