from operator import is_
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from replit import clear

clear()

# TODO: [1] Create objects

## OBJECT CREATED AND STORED
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu() # Step 3
is_on = True #Step 3
money = MoneyMachine()

# TODO: [2] Call objects as needed
## CALL METHOD ( FUNCTION ) FROM CLASS
# money_machine.report()
# coffee_maker.report()

# TODO: [3] Create while loop (actual program)

while is_on:
    options = menu.get_items() 
    menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        ## TODO: [4] Check if resources sufficient
        is_sufficient = coffee_maker.is_resource_sufficient(drink)
        if is_sufficient:
            #print("Can make")
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
           