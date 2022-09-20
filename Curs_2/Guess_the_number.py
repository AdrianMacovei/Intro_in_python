import random
import os
logo = '''
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ 
 |G|u|e|s|s| |t|h|e| |n|u|m|b|e|r| 
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ 
'''


def guess_the_number():
    print(logo)
    number_calculator = random.randint(0, 1000)
    continue_loop = True
    number_of_tries = 0
    while continue_loop:
        user_choice = int(input("Ghiceste numarul la care s-a gandit calculatorul (1-1000):\n"))
        number_of_tries += 1
        if 0 <= user_choice <= 1000:
            if user_choice == number_calculator:
                continue_loop = False
                print("Ai castigat, ai ghicit numarul!")
                print(f"Ai castigat din {number_of_tries} incercari.")
            elif user_choice > number_calculator:
                print(f"Mai incearca, numarul la care m-am gandit este mai mic decat {user_choice}.")
            elif user_choice < number_calculator:
                print(f"Mai incearca, numarul la care m-am gandit este mai mare decat {user_choice}.")
        else:
            print("Numarul trebuei sa fie in intervalul 0-1000.")
    should_continue = input("Vrei sa incerci din nou?(y or n)\n")
    if should_continue == "y":
        os.system('cls')
        guess_the_number()


guess_the_number()
