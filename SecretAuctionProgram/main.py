from os import system
import art

def clear():
   system('cls')
clear()
print(art.logo)
#HINT: You can call clear() to clear the output in the console.
print("Enter the Secret Auction Program")
bids_dictionary = {}

def add_dic_values(person_name,bid_amount):
  bids_dictionary[person_name] = bid_amount

def highest_bid_memeber():
  bid_value = 0
  winner = ""
  for name in bids_dictionary:
    if bid_value <  bids_dictionary[name]:
      bid_value = bids_dictionary[name]
      winner = name
  print(f"Bid winner {winner}, because bid amount is $ {bid_value}")
bid_exists = True
while bid_exists == True:
  
  name = str(input("Enter your Name: "))
  bid_value = int(input("Enter the Bid $ ammount: "))
  add_dic_values(name,bid_value)
  auction_exist = str(input("Enter yes if any other bids exist :"))
  if auction_exist == "yes":
    bid_exists = True
  else:
    bid_exists = False
  clear()

highest_bid_memeber()

