from art import logo

still_bids = True
bids = {}
winner = ""


def find_highest_bidder(bidding_dictionary):
    global winner
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print(logo)

while still_bids:
    name = input("What's your name?: ").title()
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there more users who wants to bid? Type Yes or No:\n").lower()
    print("\n" * 20)
    if should_continue == "no":
        still_bids = False
        find_highest_bidder(bids)
