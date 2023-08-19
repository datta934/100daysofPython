
#
# auction = {}
#
# def otherUser():
#     add = input("Do you want to run other bid?")
#     if add == 'yes':
#         user()
#     else:
#         declareWinner(auction)
#
# def declareWinner(record):
#     high = 0
#     for bidder in record:
#         bid_amount = record[bidder]
#         if bid_amount > high:
#             high = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${high}")
#
#
# def user():
#     name = input("What is your name?: ")
#     bid = input("What is your bid$?: ")
#     auction[name] =bid
#     otherUser()
#
# user()

# Angela's Solution
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
      print("")





