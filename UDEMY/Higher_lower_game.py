# aleg random A si B din data_game

# daca raspund corect B devine A iar in loc de B aleg random din nou din data_game pana cand dau raspuns gresit

# daca raspunsul este corect se stere consola

# am un curent score care creste cu fiecare raspuns corect


import random
from art_higher_lower import logo, vs
from game_data import data


def interface_game(random_a, random_b, score):
    print(logo)
    print(f'Compare A:{random_a["name"]}, a {random_a["description"]}, from {random_a["country"]}.')
    print(vs)
    print(f'Against B:{random_b["name"]}, a {random_b["description"]}, from {random_b["country"]}.')


def game():
    random_a = random.choice(data)
    random_b = random.choice(data)
    score = 0
    wrong = False
    while not wrong:
        interface_game(random_a, random_b, score)
        first_number_of_followers = random_a["follower_count"]
        print(first_number_of_followers)
        second_number_of_followers = random_b["follower_count"]
        print(second_number_of_followers)
        answer_user = input("Who has more followers? Type 'A' or 'B':\n").upper()
        if answer_user == 'A':
            if second_number_of_followers <= first_number_of_followers:
                score += 1
                random_a = random_b
                random_b = random.choice(data)
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                wrong = True
        elif answer_user == 'B':
            if second_number_of_followers > first_number_of_followers:
                score += 1
                random_a = random_b
                random_b = random.choice(data)
                print(f"You are right! Curent score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                wrong = True


game()