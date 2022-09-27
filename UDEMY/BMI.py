# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = float(weight) / float(height) ** 2

if BMI < 18.5:
    print ("You are underweight.")
elif 18.5<BMI<25:
    print ("You have a normal weight.")
elif 25<BMI<30:
    print ("You are overweight.")
elif 30<BMI<35:
    print ("You are obese.")
else:
    print ("You are clinically obese.")




