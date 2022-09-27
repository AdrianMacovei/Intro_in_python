#create a new variabable to store the input
number = int(input("Check this number: "))
#create a function called prime_checker who will say if a number is prime
def prime_checker(n):
    #this numbers 2 and 3 are excception
    if n==2 or number==3:
        print("It's a prime number.")
    #important to add 5 and 7 to cover all numbers 0-100 if will be after 100 is needed to put 11 too on condition    
    elif n%2==0 or n%3==0 or n%5== 0 or n%7==0:
            print("It's  not a prime number.")
    else: 
        print("It's a prime number.")
#call the funtion with argument and its parameter
prime_checker(n = number)
