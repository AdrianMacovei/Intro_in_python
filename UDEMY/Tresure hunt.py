print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print ("Please be careful what you chose, any wrong chose will finish the game.")
print ("Your adventure to start the treasure start. You will go on this road until the first intersection, here you have to choose either to go on the right or on the left road.")
# will introduce a variable for this input answer named road_chosen and will make this less and i will make it run evem if the asnwer is with lower or upercase
road_chosen_1 = input("Which one will you choose, left or right?\n")
road_chosen = road_chosen_1.lower()
if road_chosen == "right":
  print ("You chose the right road. Keep going and you will find the tresure.")
  print ("Time to continue our adventure. You go until will find a bridge. Here is a person who will let you pass only if you will anwer correct to his riddle.")
  riddle_answer = input("There’s only one word in the dictionary that’s spelled wrong. What is it?\n").lower()
  if riddle_answer == "wrong":
    print ("Very well, you are a step closer to find the tresure.")
    print ("You go until a house, you step in to it and there are 3 doors who go to a different chamber. This doors are numbered with 1, 2 and 3.")
    number_choice = int(input ("What number you will chose? \n"))
    if number_choice == 1 or number_choice == 2 or number_choice == 3:
      if number_choice == 2:
        print ("Good choice! Now you can continue to the last chalenge. In the back of this house is a forest where leave a spirit who guards the tresure. If you want to take the tresure need first to defeat that spirit. For that you can use one of this three arms:1= sword,2= lamp or 3= holy water")
        
        arm_chose = int(input("Which one you will use?\n"))
  
        if arm_chose == 1:
          print ("Game over! Spirit defeated you!")
        elif arm_chose == 2:
          print ("Game over! Spirit defeated you!")
        elif arm_chose == 3:
          print ("Congratulations 🍾! You defeat the spirit using right arm! You find the treasure and now you are the richest man on th world.💰💍")
        else:
          print ("Wrong arm choice. Need to use on of these three!")
         
      elif number_choice == 1:
       print ("GAME OVER! You chose a chamber full of fire 🔥 and you were made steak 🥩.")
      else:
       print ("GAME OVER! You chose a chambers full of crocodiles 🐊 and you get eaten by them")
            
    else:
      print ("Wrong number! Try again!")

  else:
    print ("GAME OVER!🚫 You answer is wrong!")  
   
  
else:
  print ("GAME OVER!🚫 You chose a dead end.")   


# rint ("Congratulations 🍾! You find the treasure and now you are the richest man on th world.💰💍p👑""GAME OVER! You chose a chambers full of crocodiles 🐊 and you get eaten by them")


