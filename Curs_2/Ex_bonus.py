import random
import os
art_logo = """

         88 88                        
         88 ""                        
         88                           
 ,adPPYb,88 88  ,adPPYba,  ,adPPYba,  
a8"    `Y88 88 a8"     "" a8P_____88  
8b       88 88 8b         8PP"""""""  
"8a,   ,d88 88 "8a,   ,aa "8b,   ,aa  
 `"8bbdP"Y8 88  `"Ybbd8"'  `"Ybbd8"'  
"""


def rool_the_dice():
    print(art_logo)
    rooldice = random.randint(1, 6)
    user_choice = int(input("Ghiceste ce numar va arata zarul(1-6):\n"))
    if 1 <= user_choice <= 6:
        if user_choice == rooldice:
            print(f"Ai ghicit. Felicitari! Ai ales {user_choice} si zarul a fost {rooldice}.")
        elif user_choice > rooldice:
            print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {user_choice} si zarul a fost {rooldice}.")
        else:
            print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {user_choice} si zarul a fost {rooldice}.")
    else:
        print("Te rog sa alegi un numar din intervalul (1-6).")
    should_continue = input("Vrei sa incerci din nou?(y or n)\n")
    if should_continue == "y":
        os.system('cls')
        rool_the_dice()


rool_the_dice()

