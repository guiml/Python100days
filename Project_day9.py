from unicodedata import name
from replit import clear
clear()

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

#### HEADER ####
print(logo)
print("\nBID YOUR PRICE\n")


#### BODY ####

dict_names_bids = {}

end_bid = False
while end_bid == False:
    name_i = input("What is your name? ")
    value_i = input("What is your bid? $")

    dict_names_bids[name_i] = value_i
    
    end_bid_i = input("Are there any other bidders? Type 'yes or 'no'.")
    if end_bid_i == 'no':
        end_bid = True
    else:
        clear()
        

# print(dict_names_bids)

max_value = max(dict_names_bids.values())
max_key = max(dict_names_bids, key=dict_names_bids.get)
print(f"The winner is {max_key} with a bid of ${max_value}")
