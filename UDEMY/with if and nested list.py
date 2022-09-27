rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
image =[rock, paper, scissors]
#Write your code below this line 👇
import random
computer_chose = random.randint(0, 2)
# i used randint function for random computer choice
if player_chose == 0 or player_chose == 1 or player_chose == 2:
  #conditie necesara pentru a lua in calcul doar cele 3 numere
  print (f"Your chose is: {image[player_chose]}")
  print (f"Computer chose is: {image[computer_chose]}")
  if player_chose == 0 and computer_chose == 2:
   print ("You win!")
  elif computer_chose == 0 and player_chose ==2:
   print ("You lose!")
  elif computer_chose > player_chose:
   print("You lose!")
  elif player_chose > computer_chose:
   print("You win!")
  else:
    print ("Equality")
else:
 print ("Wrong type! Try again!")