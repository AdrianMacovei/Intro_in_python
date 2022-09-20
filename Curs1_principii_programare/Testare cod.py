from replit import clear
from art.py  import logo
def matematical_calculator(number1, operation, number2):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        return number1 / number2
    else:
        return "Invalid operation choice."

def should_continue():
    return input("Type 'y' if you want to continue calculating using or type 'n' if you want to restart the calculator:\n")

def calculator():
    first_number = float(input("What's the first number?:\n"))
    keep_going = True
    while keep_going == True:
        pick_operation = input("+\n-\n*\n/\nPick an operation?:\n")
        second_number = float(input("What's the second number?:\n"))
        result = matematical_calculator(first_number, pick_operation, second_number)
        print(f"{first_number} {pick_operation} {second_number} = {result}")
        answer = should_continue()
        if answer == "y":
            first_number = result
        else:
            keep_going = False
            clear()
            calculator()
calculator()