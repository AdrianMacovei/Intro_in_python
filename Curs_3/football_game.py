import random
from time import sleep
import os
logo = """
|             |             |
 |___          |          ___|
 |_  |         |         |  _|
.| | |.       ,|.       .| | |.
|| | | )     ( | )     ( | | ||
'|_| |'       `|'       `| |_|'
 |___|         |         |___|
 |             |             |
 |_____________|_____________|
"""


def footbal_game():
    print(logo)
    players = ["Messi", "Pique", "Alves", "Carevic", "Alba", "Ronaldo", "Neymar"]
    reserve_players = ["Mbappe", "Kane", "Zidane", "Maradona"]
    max_changes = 3
    numbers_of_refuse_to_change = 5
    print(f"The match has begun. Let's wish success to our team of: {', '.join(players)}.")
    print(f"On the bench we have the following players: {', '.join(reserve_players)}.")
    while max_changes > 0 and numbers_of_refuse_to_change > 0:
        make_a_change = input("Do you want to make a change?? (y/n)\n")
        make_a_change = make_a_change.lower()
        if make_a_change == "y":
            player_changed = input("Who do you want to change? (name of player)\n").lower().capitalize()
            player_from_reserve = input("Who do you want to change with?? (name of player)\n").lower().capitalize()
            if player_changed in players and player_from_reserve in reserve_players:
                players.remove(player_changed)
                players.append(player_from_reserve)
                reserve_players.remove(player_from_reserve)
                max_changes -= 1
                if max_changes >= 1:
                    print(f"{player_from_reserve} entered the field and {player_changed} came out."
                          f" You still have {max_changes} changes.")
                    print(f"The team is made up of {', '.join(players)} and on the bench are "
                          f"the players {', '.join(reserve_players)}")
                    print("The players continue the match, it's a tight match.")
            elif player_changed not in players:
                print(f"Player {player_changed} is not on the field.")
                print(f"The team is made up of {', '.join(players)} and on the bench are "
                      f"the players {', '.join(reserve_players)}")
            else:
                print(f"Player {player_from_reserve} is not on the bench.")
                print(f"The team is made up of {', '.join(players)} and on the bench are "
                      f"the players {', '.join(reserve_players)}")
        else:
            print(f"The players continue to play, the team being made up of {', '.join(players)}.")
            numbers_of_refuse_to_change -= 1
    print(f"You have reached the maximum number of changes, the players will "
          f"continue the match in the formation {', '.join(players)}.")
    your_team_goals = random.randint(0, 8)
    opposing_team_goals = random.randint(0, 8)
    sleep(4)
    if your_team_goals == opposing_team_goals:
        print(f"The match ended in a draw with the score {your_team_goals}:{opposing_team_goals}.")
    elif your_team_goals > opposing_team_goals:
        print(f"Congratulations! Your team won the match with the score {your_team_goals}:{opposing_team_goals}.")
    else:
        print("\n")
        print(f"Your team lost by score {your_team_goals}:{opposing_team_goals}."
              f"\nI'm sure next time you'll win!")
    play_again = input("Do you want to play again? (y or n)\n")
    play_again = play_again.lower()
    if play_again == "y":
        os.system('cls')
        footbal_game()


footbal_game()
