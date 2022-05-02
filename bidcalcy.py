import clear

print()
bids = {}

bidding_finshed = False

def find_heigest_bid (biddeing_record):
    heigest_bid = 0
    winner = ""
    for bidder in biddeing_record:
        bid_ammount = biddeing_record[bidder]
        if bid_ammount > heigest_bid:
            heigest_bid = bid_ammount
            winner = bidder

    print(f"the winner is {winner} with a bid of {heigest_bid}")

while not bidding_finshed:
    name = input("What is your name :- ")
    prize = int(input("What is your bid :- "))
    bids[name] = prize

    should_continue =  input("there are any other bidder ? type yes or no ")
    if should_continue == "no":
        bidding_finshed = True
        find_heigest_bid(bids)
    elif should_continue == "yes": 
        clear
