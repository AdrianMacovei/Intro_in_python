#Write your code below this row 👇
for number in range (1,101): #i use for and range to have all number from 1-100
    if number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print (number)