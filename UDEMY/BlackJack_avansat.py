import random
from art_blackjack import logo
import os


def play_again():
    """Aceasta functie este utilizata daor pentru recursion astfel se creeaza un loop ce va rula tot codul iar si
    iar pana cand userul va spune ca nu doreste sa mai joace din nou"""
    print(logo)
    cards = {"2♣": 2, "2♠": 2, "2♥": 2, "2♦": 2, "3♣": 3, "3♠": 3, "3♥": 3, "3♦": 3, "4♣": 4, "4♠": 4, "4♥": 4, "4♦": 4,
             "5♣": 5, "5♠": 5, "5♥": 5, "5♦": 5, "6♣": 6, "6♠": 6, "6♥": 6, "6♦": 6, "7♣": 7, "7♠": 7, "7♥": 7, "7♦": 7,
             "8♣": 8, "8♠": 8, "8♥": 8, "8♦": 8, "9♣": 9, "9♠": 9, "9♥": 9, "9♦": 9, "10♣": 10, "10♠": 10, "10♥": 10,
             "10♦": 10, "A♣": 11, "A♠": 11, "A♥": 11, "A♦": 11, "J♣": 10, "J♠": 10, "J♥": 10, "J♦": 10, "Q♣": 10,
             "Q♠": 10, "Q♥": 10, "Q♦": 10, "K♣": 10, "K♠": 10, "K♥": 10, "K♦": 10}
    player_first_cards = [random.choice(list(cards.keys())), random.choice(list(cards.keys()))]
    print(f'Your cards are {player_first_cards[0]} {player_first_cards[1]}')
    computer_first_cards = [random.choice(list(cards.keys())), random.choice(list(cards.keys()))]
    print(f"Computer first card is: {computer_first_cards[0]}, {computer_first_cards[1]}.")

    def computer_cards_score(computer_cards_list, score_computer):
        """Aceasta functie calculeaza scorul catilor pe care le primeste
        computerul si returneza valoarea respectivului scor"""
        values_cards_computer = [cards[computer_cards_list[0]], cards[computer_cards_list[1]]]
        # am facut o lista separata cu scorul cartilor ca sa imi fie mai usor sa fac scor total
        score_computer += sum(values_cards_computer)
        i = 1
        # i ne va spune cel mai mare index al scorului listei de carti, la inceput 2 carti (index 0 si 1)
        if score_computer == 21:
            return score_computer, computer_cards_list
        while score_computer < 17:
            # computerul va trage carti pana cand scorul sau va depasi 17
            computer_cards_list.append(random.choice(list(cards.keys())))
            i += 1
            values_cards_computer.append(cards[computer_cards_list[i]])
            score_computer += values_cards_computer[i]
            # adaugam la scor valoarea de la index i
            if score_computer > 21 and 11 in values_cards_computer:
                # acest bloc de cod va transforma Ace-ul de la 11 la 1 atunci cand scor mai mare de 21
                values_cards_computer.remove(11)
                values_cards_computer.append(1)
                score_computer = sum(values_cards_computer)
        # functia ne va returna intr-un final scor total pe care il putem salva intr-o variabila
        return score_computer, computer_cards_list

    def player_cards_score(player_cards_list, score_player, continue_looping):
        """Aceasta functie calculeaza scorul playerului si returneaza valoarea acestuia"""
        values_cards_player = [cards[player_cards_list[0]], cards[player_cards_list[1]]]
        # am creat o lista cu valorile cartilor si pentru player - usurinta in a calcula suma totala
        score_player += sum(values_cards_player)
        i = 1
        while continue_looping:
            # cat timp scorul va fi sub 21 o sa tot intrebam playerul daca vrea carte
            if score_player > 21 and 11 in values_cards_player:
                # blocu acesta va schimba valoarea Ace-ului la 1 atunci cand scor mai mare de 21
                values_cards_player.remove(11)
                values_cards_player.append(1)
                score_player = sum(values_cards_player)
            elif score_player < 21:
                take_a_card = input("Do you want to draw a card? (y/n): \n")
                take_a_card = take_a_card.lower()
                if take_a_card == "y":
                    i += 1
                    player_cards_list.append(random.choice(list(cards.keys())))
                    values_cards_player.append(cards[player_cards_list[i]])
                    print(f"Ai urmatoarele carti: {', '.join(player_cards_list)}.")
                    score_player = sum(values_cards_player)
                elif take_a_card == "n":
                    continue_looping = False
            else:
                continue_looping = False
        # functia noastra va returna doua valori sub forma de tuple
        return score_player, player_cards_list
    # salvam cele doua valori returante in 2 variabile
    player_score, player_cards = player_cards_score(player_cards_list=player_first_cards,
                                                    score_player=0, continue_looping=True)
    computer_score, computer_cards = computer_cards_score(computer_first_cards, 0)
    print(f"    Ai un scor total egal cu {player_score}.  😇 ")
    # blocul acesta de cod va compara scorurile obtinute in interiorul functiilor de mai sus
    if computer_score == 21 and len(computer_cards) <= 2:
        print(f"Dealerul are urmtoarele carti {', '.join(computer_cards)}")
        # .join ne va ajuta sa printam elementele dintr-o lista fara paranteze patrate sau virgula
        print("BlackJack! Dealerul a castigat!")
    elif player_score == 21 and len(player_cards) <= 2:
        print("BlackJack! Ai castigat! 🏆 ")
    elif player_score > 21 or (player_score == 21 and computer_score == 21):
        print(f"Dealerul are urmtoarele carti {', '.join(computer_cards)}")
        print(f"    Dealeru are un scor total egal cu {computer_score}.  😈 ")
        print("Dealerul a castigat! ☠️")
    elif player_score < computer_score < 21:
        print(f"Dealerul are urmtoarele carti {', '.join(computer_cards)}")
        print(f"    Dealeru are un scor total egal cu {computer_score}.  😈 ")
        print("Dealerul a castigat! ☠️")
    elif player_score == computer_score:
        print(f"Dealerul are urmtoarele carti {', '.join(computer_cards)}")
        print(f"    Dealeru are un scor total egal cu {computer_score}.  😈 ")
        print("Este egalitate. 😛 ")
    else:
        print(f"Dealerul are urmtoarele carti {', '.join(computer_cards)}")
        print(f"    Dealeru are un scor total egal cu {computer_score}.  😈 ")
        print("Ai castigat! 🏆 ")
    play_again_answer = input("Vrei sa joci din nou:(y or n)?\n")
    play_again_answer = play_again_answer.lower()
    if play_again_answer == "y":
        os.system('cls')
    # aceasta metoda se numeste recursion - practic chemam o functie in corpul sau pentru a o rula din nou
    # si din nou - atentie la infinite loop - aici conditia este sa raspunda n ca sa iasa din loop
        play_again()


play_again()
