import art
print(art.logo)
bidders = {

}
anymore_bidders = True
while anymore_bidders:
    bidders_name = input("Who\'s bidding? \n")
    bidders_bid = int(input("How much is your bid? "))
    bidders[bidders_name] = bidders_bid
    are_there_more_bidders = input('Are there more bidders? Type "yes" or "no" ').lower()
    if are_there_more_bidders == "yes":
        print("\n" * 25)
    else:
        anymore_bidders = False
        print("\n" * 25)
highest_bid = 0
highest_bidder = ''
for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        highest_bidder = bidder
print(f'The winner is {highest_bidder} with a bid of ${highest_bid}.')
