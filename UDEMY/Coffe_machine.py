from os import system
from time import sleep

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

logo_1 = '''
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' 
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'"
'''

# global variables
water = 300
milk = 200
coffee = 100
money_achived = 0
# this values are the max capacity for each ingredients and this values will decrease
# after each sell drink until no drink can be prepare and will need realimentation
# !!! money_achived will increase


def calculate_min_value_of_ingredients(name):
    """ This function calculates the minimum value of each ingredients (water, milk, coffee)"""
    list_values = []
    for name_of_drink in MENU:
        value = MENU[name_of_drink]["ingredients"][name]
        list_values.append(value)
    return min(list_values)


def realimentation_machine():
    """This function when is call will refill water, milk, coffee and money_achived to base value 300, 200, 100
    respetiv 0, and will need a corect password to have access"""

    password = input("Introdu parola de 4 cifre:")
    while password != "1996":
        realimentation_machine()
    else:
        global water, milk, coffee, money_achived
        water = 300
        milk = 200
        coffee = 100
        money_achived = 0
        return


def pay_for_drink():
    """This funtion will ask user to introduce money for his drink and will return the sum of coins introduced"""
    print("Please insert coins.")
    half_dollars = input("how many fifty cents?: ")
    quarters = input("how many quarters?: ")
    dimes = input("how many dimes?: ")
    nickles = input("how many nickles?: ")
    pennies = input("how many pennies?: ")
    # this line of code is if user don't introduce anything "" or if introduce negative values
    if half_dollars == "" or int(half_dollars) < 0:
        half_dollars = 0
    else:
        half_dollars = int(half_dollars)

    if quarters == "" or int(quarters) < 0:
        quarters = 0
    else:
        quarters = int(quarters)

    if dimes == "" or int(dimes) < 0:
        dimes = 0
    else:
        dimes = int(dimes)

    if nickles == "" or int(nickles) < 0:
        nickles = 0
    else:
        nickles = int(nickles)

    if pennies == "" or int(pennies) < 0:
        pennies = 0
    else:
        pennies = int(pennies)
    customer_money = (half_dollars * 0.5) + (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return customer_money


def chose_a_drink():
    """This funtion will ask user to chose what he want to drink, and will return, name od the drink,
    ingredients of the drink anf cost o the drink"""
    while True:  # this while will recall the corp of fuction until user will chose some valid predefinition chose
        user_choice = input("  What do you like to drink?\n 1. Esspreso\n 2. Latte\n "
                            "3. Cappucino \n (chose a number)\n")
        # keep this string because if i will use integer form will rise eror if user dont type anything
        # I can change them in condition to int but will not help me so I keep them str
        if user_choice == "1":
            return list(MENU.keys())[0], MENU["espresso"]["ingredients"], MENU["espresso"]["cost"]
        elif user_choice == "2":
            return list(MENU.keys())[1], MENU["latte"]["ingredients"], MENU["latte"]["cost"]
        elif user_choice == "3":
            return list(MENU.keys())[2], MENU["cappuccino"]["ingredients"], MENU["cappuccino"]["cost"]
        elif user_choice == "112":  # this line of code is for administrator use will go to realimentation_machine()
            realimentation_machine()
            coffee_machine_main()
        else:
            print("Wrong type! Chose Again!")
            coffee_machine_main()


def can_prepare(water_used, milk_used, coffee_used):
    """This funtion will verify if we have enough ingredients for drink what user chose and will return TRUE or FALSE"""
    return water >= water_used and milk >= milk_used and coffee >= coffee_used


def preparation(water_used, milk_used, coffee_used, cost_of_drink):
    """This funtion will take from global tank ingredients for customer drink"""
    global water, milk, coffee, money_achived
    water -= water_used
    milk -= milk_used
    coffee -= coffee_used
    money_achived += cost_of_drink


def print_warning():
    """This function will warning if machine don't have more ingredients to prepare even one type of drink"""
    if water < calculate_min_value_of_ingredients("water") or coffee < calculate_min_value_of_ingredients("coffee")\
            or milk < calculate_min_value_of_ingredients("milk"):
        print("No drink available, need to refill!!!⚠️⚠️⚠️")


def clear():
    """This function will clear the console after every command of drink"""
    sleep(3)
    system('cls')


def coffee_machine_main():
    # i put this code in a function because need to come back on loop
    # when user type invalid number in chose_a_drink()
    while True:  # this will keep run infinitely the code below
        print(logo_1)
        print_warning()
        # unpack the return of chose_a_drink function
        name_of_drink, ingredients_of_drink, price_of_drink = chose_a_drink()
        water_for_prep = ingredients_of_drink["water"]
        milk_for_prep = ingredients_of_drink["milk"]
        coffee_for_prep = ingredients_of_drink["coffee"]
        # if machine have ingredients for drink will go to pay_for_drink
        if can_prepare(water_for_prep, milk_for_prep, coffee_for_prep):
            print(f"Your {name_of_drink} cost is {price_of_drink}.")
            money_introduced = pay_for_drink()
            if money_introduced > price_of_drink:
                # this will calculate the change if customer introduce more money than is necessary
                change = round(money_introduced - price_of_drink, 2)
                preparation(water_for_prep, milk_for_prep, coffee_for_prep, price_of_drink)
                print(f"Here is {change} in change.\nHere is your {name_of_drink} ☕ . Enjoy!😊")
                clear()
            elif money_introduced == price_of_drink:
                preparation(water_for_prep, milk_for_prep, coffee_for_prep, price_of_drink)
                print(f"Here is your {name_of_drink} ☕. Enjoy!😊")
                clear()
            else:
                print("Sorry that's not enough money. Money refunded.")
                clear()
        # if not will print a warning message
        else:
            print("Insuficient ingredients. Need refill!⚠️")
            clear()


coffee_machine_main()
