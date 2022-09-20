# Exercitiul 1

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for num in alte_numere:
    if num % 2 == 0:
        numere_pare.append(num)
    else:
        numere_impare.append(num)

    if num > 0:
        numere_pozitive.append(num)
    else:
        numere_negative.append(num)
print(numere_pare)
print(numere_impare)
print(numere_negative)
print(numere_pare)
print(numere_impare)
print(numere_negative)
print(numere_pozitive)

# Exercitiul 2
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
n = len(alte_numere)
for i in range(n):  # 0-10
    for j in range(n-i-1):  # 0-9
        if alte_numere[j] > alte_numere[j + 1]:
            alte_numere[j], alte_numere[j + 1] = alte_numere[j + 1], alte_numere[j]
# folosind debugger am observat ca incepe de la cel mai mare, il duce pe 12 intai in capat dupa 9 etc
print(alte_numere)

# Exercitiul 3
from random import randint

number_to_guess = randint(1, 30)
guessed = False

while not guessed:
    user_input = int(input("What number i have in mind? (0-30)\n"))
    if user_input > number_to_guess:
        print("Too high.")
    elif user_input < number_to_guess:
        print("Too low.")
    elif user_input == number_to_guess:
        print(f"Congratulation. You guess the number")
        guessed = True

# Exercitiul 4
number = int(input("Insert a number:\n"))

for i in range(1, number + 1):
    print(str(i) * i)

# Exercitiul 5
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f"Cifra curenta este {tastatura_telefon[i][j]}.")