import random
import os

logo = """
 _______           _______  _______  _______   _________          _______    _                 _______  ______   _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  \__   __/|\     /|(  ____ \  ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/| (    \/| (    \/     ) (   | )   ( || (    \/  |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|
| |      | |   | || (__    | (_____ | (_____      | |   | (___) || (__      |   \ | || |   | || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )     | |   |  ___  ||  __)     | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)
| | \_  )| |   | || (            ) |      ) |     | |   | (   ) || (        | | \   || |   | || |   | || (  \ \ | (      | (\ (   
| (___) || (___) || (____/\/\____) |/\____) |     | |   | )   ( || (____/\  | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__
(_______)(_______)(_______/\_______)\_______)     )_(   |/     \|(_______/  |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/
                                                                                                                                  
 """


def guess_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'am thinking of a number between 1 and 100.")

    def dificulty():
        dificulty_level = input("Choose a difficulty. Type 'easy', 'medium' or 'hard':\n").lower()
        if dificulty_level == "easy":
            return 10
        elif dificulty_level == "medium":
            return 7
        elif dificulty_level == "hard":
            return 5
        else:
            print("Chose a right level of dificulty!")
            return dificulty()
    attempts = dificulty()
    number_to_guess = random.randint(1, 100)
    
    def guess(number_of_tries):
        if number_of_tries >= 1:
            print(f"You have {number_of_tries} attempts to guess.")
            user_number = int(input("Make a guess:\n"))
            if user_number > number_to_guess:
                print("Too high.\n"
                      "Guess again.")
                number_of_tries -= 1
                guess(number_of_tries)
            elif user_number < number_to_guess:
                print("Too low.\n"
                      "Guess again.")
                number_of_tries -= 1
                guess(number_of_tries)
            elif user_number == number_to_guess:
                print(f"You got it! The answer was {user_number}.")
        else:
            print("Ai irosit toate incercarile. Ai pierdut!")
    guess(attempts)

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        os.system('cls')
        guess_game()


guess_game()
