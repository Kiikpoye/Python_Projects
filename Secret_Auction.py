import os

os.system("cls")
print("Welcome to the secret auction program.")

bids = {}
bidding_ongoing = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while bidding_ongoing:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    other_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bid == "no":
        bidding_ongoing = False
        find_highest_bidder(bids)
    elif other_bid == "yes":
        os.system("cls")
input()
