# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check?\n"))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
if year % 100 > 0 and year % 4 == 0:
  print ("This year is a leap year.")
elif year % 400 == 0 and year % 4 ==0:
  print ("This year is a leap year.")
else: 
  print ("This year is a normal year.")
  