from replit import clear #pip install eplit
from logo2 import hammer
print(hammer)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Dheeraj": 123, "Mitali": 321}
    # bidding conditions
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if should_continue == "no":
        binding_finished = True
        find_highest_bidder(bids)
        exit()
    elif should_continue == "yes":
        clear()

    else:
        print("choose valid option:")
