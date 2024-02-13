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
name_counter: int = 1

# Main loop
while main_loop:

    # Loop until valid reserve price is added
    while reserve_price < 0:

        # Get the users input for reserve price
        try:
            reserve_price = float(input("What is the reserve price? ($): "))

            # Check if the input was valid
            if reserve_price < 0:
                print("Please enter a number 0 or above.")
            
            # If it was valid
            else:
                print("Action has started")

        # If value was not a float/int
        except ValueError:
            print("Please enter a number 0 or above.")

    # Start auction
    print(f"\nCurrent highest bid is ${highest_bid}")

    # Get bidders name
    bidders_name = input("\nWhat is your name? ('F' to finish) ")

    # If bidder already bid add counter
    if bidders_name in bidding_history:
        name_counter += 1
        bidders_name = bidders_name + str(name_counter)

    # If you want auction to stop
    if bidders_name.lower() == "f":
        main_loop = False

        # Check if reserve price was met
        if highest_bid >= reserve_price:
            print(f"Action won by {bidding_history.keys()} ")

        # Print auction history from dictionary
        for bidder in bidding_history:
            print(f"{bidder}, bid {bidding_history[bidder]}$")

    # If auction continues
    else:

        # Loop until bidders bids a valid amount
        get_bid_amount = True
        while get_bid_amount:

            # Get bidders bid
            try:
                current_bid = float(input("What is your bid? ($): "))

                # If bidders bid is lower than current highest bid
                if current_bid <= highest_bid:
                    print("Your bid isn't high enough!"
                        f"\nPlease enter amount above ${highest_bid}")

                # If bid valid set current bid as the new highest bid
                else:
                    get_bid_amount = False
                    highest_bid = current_bid
                    bidding_history[bidders_name] = highest_bid

            # If bidder did not enter a float/int
            except ValueError:
                print(f"Please enter a number above ${highest_bid}.")
