from replit import clear
from art import logo
print(logo)

bids = {} # am creat un dict gol
bidding_finished = False # am creat o variabila care opreste while loop

def find_highest_bidder(bidding_record):
  highest_bid = 0 # utilizam cele doua var pentru a salva valoarea ce mai mare respectiv numele cheii pt acea valoare
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record: # bidding_record e un dict cu toate keys and value salvate (bids)
    bid_amount = bidding_record[bidder] 
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price #cream un dict cu fiecare key(nume) si val aferenta
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids) # functia care calculeaza cea mai mare valoare
  elif should_continue == "yes":
    clear()
    
