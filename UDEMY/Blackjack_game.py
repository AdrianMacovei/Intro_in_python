############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.
# dealer win if both have 21
import random
from art_blackjack import logo
import os


def play_again():
    """Aceasta functie este utilizata daor pentru recursion astfel se creeaza un loop ce va rula tot codul iar si
    iar pana cand userul va spune ca nu doreste sa mai joace din nou"""
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_first_cards = [random.choice(cards), random.choice(cards)]
    print(f'Your cards are {player_first_cards}')
    computer_first_cards = [random.choice(cards), random.choice(cards)]
    print(f'Computer first card is: {computer_first_cards[0]}')

    def computer_cards_score(computer_cards_list, score_computer):
        """Aceasta functie calculeaza scorul catilor pe care le primeste
        computerul si returneza valoarea respectivului scor"""
        score_computer += sum(computer_cards_list)
        if score_computer < 17:
            i = 1
            while score_computer < 17:
                computer_cards_list.append(random.choice(cards))
                i += 1
                score_computer += computer_cards_list[i]
                if score_computer > 21 and 11 in computer_cards_list:
                    computer_cards_list.remove(11)
                    computer_cards_list.append(1)
                    score_computer = sum(computer_cards_list)
        print(f"Dealerul are urmatoarele carti: {computer_cards_list}.")
        return score_computer

    def player_cards_score(player_cards_list, score_player, continue_looping):
        """Aceasta functie calculeaza scorul playerului si returneaza valoarea acestuia"""
        score_player += sum(player_cards_list)
        while continue_looping:
            # print(f"In acest moment ai scorul egal cu {score_player}.")
            if score_player > 21 and 11 in player_cards_list:
                player_cards_list.remove(11)
                player_cards_list.append(1)
                score_player = sum(player_cards_list)
            elif score_player < 21:
                take_a_card = input("Do you want to draw a card? (y/n): \n")
                take_a_card = take_a_card.lower()
                if take_a_card == "y":
                    player_cards_list.append(random.choice(cards))
                    print(f"Ai urmatoarele carti: {player_cards_list}.")
                    score_player = sum(player_cards_list)
                elif take_a_card == "n":
                    continue_looping = False
            else:
                continue_looping = False
        return score_player, player_cards_list

    player_score = player_cards_score(player_cards_list=player_first_cards, score_player=0, continue_looping=True)
    computer_score = computer_cards_score(computer_first_cards, 0)
    print(f"    Ai un scor final egal cu {player_score[0]}.")
    print(f"    Dealeru are un scor total de {computer_score}.")
    if player_score[0]< 21:
        if player_score == computer_score and computer_score != 21:
            print("Este egalitate.")
        elif player_score[0] > computer_score:
            print("Ai castigat!")
        elif computer_score > 21:
            print("Ai castigat!")
        else:
            print("Dealerul a castigat!")
    elif player_score[0] == 21:
        if computer_score != 21 and len(player_score[1]) < 3:
            print("BlackJack! Ai castigat")
        else:
            print("Ai castigat")
    else:
        print("Dealerul a castigat!")
    play_again_answer = input("Vrei sa joci din nou:(y or n)?\n")
    play_again_answer = play_again_answer.lower()
    if play_again_answer == "y":
        os.system('cls')
        play_again()


play_again()