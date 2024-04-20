bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with the amount of {highest_bid}")


while not bidding_finished:
    name = input("enter your name")
    price = input("what is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other biddders? yes, no")

    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        # clear()
