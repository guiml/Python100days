from contextlib import nullcontext
from art import logocafe
from replit import clear


# TODO: Build dictionaries

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

clear()

# TODO: Build report function

def print_report():
    """
    Print report
    """
    for key in resources:
        print(f"{key.capitalize()}: {resources[key]}")

# TODO: Build buy function

def count_coins(quarters, dimes, nickels, penies):
    total = int(quarters)*0.25
    total = total + int(dimes)*0.10
    total = total + int(nickels)*0.05
    total = total + int(penies)*0.01
    return(float(total))


def subtract_resources(type_of_coffee):
    for i in MENU[type_of_coffee]['ingredients']:
        resources[i] = resources[i] - MENU[type_of_coffee]['ingredients'][i]

print(logocafe)


def coffee_machine():
    switch_off = False
        
    while not switch_off:
        stop_now = False
        type_of_coffee = input("What would you like? (espresso/latte/cappuccino): ")
        if type_of_coffee == "off":
            switch_off = True
        else:
            switch_off = False
            if type_of_coffee not in ['report','latte','cappuccino','espresso']:
                print("Sorry, command not recognized.")
            else:
                if type_of_coffee == "report":
                    print_report()
                else:
                    #print(type_of_coffee)
                    # Part 1:: Check if resources are sufficient
                    for i in MENU[type_of_coffee]['ingredients']:
                        #print(i)
                        if int(resources[i]) < float(MENU[type_of_coffee]['ingredients'][i]):
                            lacking_resource = i
                            stop_now = True
                            
                    if not stop_now:
                        print("Plese insert coins")
                        quarters = input("how many quarters?: ")
                        dimes = input("how many dimes?: ")
                        nickels = input("how many nickels?: ")
                        penies = input("how many penies?: ")
                        money_provided = count_coins(quarters, dimes, nickels, penies)
                        product_cost = float(MENU[type_of_coffee]['cost'])
                        if  money_provided < product_cost:
                            print(f"Not enough money, provicded: ${money_provided}, needed ${product_cost}")
                        else:
                        #Part 2:: Check if client has enough funds
                            subtract_resources(type_of_coffee)
                            print(f"Here is your change ${round(money_provided - product_cost,2)}")
                            print(f"Here is your {type_of_coffee} ☕️. Enjoy!")
                    else:
                        print(f"Sorry there is not enough {lacking_resource}")





coffee_machine()








