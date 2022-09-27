# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = str(input("Where do you want to put the treasure? "))
#use name of variable with [] to fins the element on number x on input ex name[1]=n
# use int to chanege again the type
orizontal = int(position[0])
vertical = int(position[1])
#select row
#selected_row = map[orizontal -1]
# select colomn abd chanege element
#selected_row[vertical -1] = "X"
# another way is 
map[orizontal-1][vertical - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")