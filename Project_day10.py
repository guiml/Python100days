from unicodedata import name
from replit import clear
from art import logoCalc

def add(a,b):
    return(float(a)+float(b))
def sub(a,b):
    return(float(a)-float(b))
def mult(a,b):
    return(float(a)*float(b))
def div(a,b):
    return(float(a)/float(b))

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}




clear()
print(logoCalc)

def calc():
    first_number = float(input("What's the first number? "))
    print("+ - * /")

    cont = True

    while cont:
        calc_operator = input("Pick an operator: ")
        second_number = float(input("What's the next number? "))
        calc_func = operations[calc_operator]
        result = calc_func(first_number,second_number)
        print(f"{float(first_number)} {calc_operator} {float(second_number)} = {result}")

        if input(f"Type 'y to continue calculating with {result}, or type 'n' to start a new calculation.") == 'y':
            first_number = result
        else:
            cont = False
            clear()
            print(logoCalc)
            calc()

calc()


