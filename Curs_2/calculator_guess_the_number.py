from time import sleep
import os


def computer_guess_number():
    logo = '''
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ 
 |G|u|e|s|s| |t|h|e| |n|u|m|b|e|r| 
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ 
'''
    print(logo)
    print("Gandeste-te la un numar cuprins intre 0-1000, tine-l minte, eventual scrie-l pe o foaie de hartie."
          "In continuare eu voi incerca sa ghicesc numarul la care te-ai gandit utilizand cat mai putine incercari")
    last_number = 1000
    # ultimul numar din intervalul in care se situeaza numrul care trebuie ghicit
    first_number = 0
    # primul numar din intervalul in care se situeaza numrul care trebuie ghicit
    guessed = False
    # conditia ca while loop sa ruleze la infinit
    guess_tries = 0
    # timp dat userului sa se gandeasca la numar
    sleep(10)

    while not guessed:
        guess_tries += 1
        middle_number = int(first_number + last_number) // 2
        first_ask = input(f"Numarul tau este {middle_number}?(y or n):\n")
        first_ask = first_ask.lower()
        '''puteam sa pun si la sfarstiul liniei 23 .lower dar am obs ca uneori da eroare si in loc de caracter lowercase
        apare ceva hexazecimal <buid-in method lower of str object at 0x000025DBC etc> si se evalueaza cu aceasta mai 
        departe <buid-in method lower of str object at 0x000025DBC etc> == 'n' false si nu mai intra in bloc
      '''
        if first_ask == "n":
            second_ask = input(f"Numarul tau este mai mare decat {middle_number}?(y or n):\n")
            second_ask = second_ask.lower()
            if second_ask == "y":
                first_number = middle_number
            else:
                last_number = middle_number
        elif first_ask == "y":
            guessed = True
            print(f"Se pare ca numarul la care te-ai gandit este {middle_number}.")
            print(f"Am avut nevoie de {guess_tries} icercari pentru a ghici.")
            play_again = input("Vrei sa incerci din nou?(y or n):\n")
            play_again = play_again.lower()
            if play_again == "y":
                os.system('cls')
                computer_guess_number()


computer_guess_number()
