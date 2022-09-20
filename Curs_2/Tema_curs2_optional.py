# Exercitiul 1
x = int(input("Introdu un numar intreg:\n"))
if 1000 <= x:
    print(f"{x} are cel putin 4 cifre")
else:
    print(f"{x} nu are cel putin 4 cifre")

# Exercitiul 2
x = int(input("Introdu un numar intreg:\n"))

if 100000 <= x <= 999999:
    print(f"{x} are exact 6 cifre")
elif x > 999999:
    print(f"{x} are mai mult de 6 cifre")
else:
    print(f"{x} are mai putin de 6 cifre")

# Exercitiul 3
x = int(input("Introdu un numar intreg:\n"))

if x % 2 == 0:
    print(f"{x} este un numar par.")
else:
    print(f"{x} este un numar impar.")

# Exercitiul 4
x = int(input("Introdu un numar intreg:\n"))
y = int(input("Introdu un al doileq numar intreg:\n"))
z = int(input("Introdu un al treilea numar intreg:\n"))
greater_number = 0
print(f"Numerele pe care le-ai introdus sunt: {x}, {y}, {z}.")
if x > y and x > z:
    greater_number = x
elif y > x and y > z:
    greater_number = y
else:
    greater_number = z
print(f"Cel mai mare numar introdus este egal cu {greater_number}.")

# Exercitiul 5
x = int(input("Te rog sa introduci valoarea primului unghi al triunghiul:\n"))
y = int(input("Te rog sa introduci valoarea unghiului al doilea din triunghi:\n"))
z = int(input("Te rog sa introduci valoarea unghiului al treilea din triunghi:\n"))

if (x+y+z) == 180:
    print("Triunghiul este valid.")
else:
    print("Triunghiul nu este valid. Hint: suma unghiurilor 180.")

# Exercitiul 6
string_dat = "Coral is either the stupidest animal or the smartest rock"
x = int(input("Introdu un numar:"))
# if x > 57:
#     x %= 57 # partea asta ne poate ajuta daca userul introduce ceva mai mare dact 57 lungimea caracterului
print(len(string_dat))
indexuri_fara_x = len(string_dat) - x
print(string_dat[0:indexuri_fara_x])

# Exercitiul 7
string_dat = "Coral is either the stupidest animal or the smartest rock"
string_nou = string_dat[:5] + string_dat[-5:]
print(string_nou)
# daca e sa vedem spatiul ca nefiind caracter
string_dat = string_dat.replace(" ", "")
string_nou = string_dat[0:5] + string_dat[-5:]
print(string_nou)

# Exercitiul 8
string_dat = "Coral is either the stupidest animal or the smartest rock"
index = string_dat.index("rock")
index = int(index)
print(index)
print(string_dat[:index])

# Exercitiul 9
string_introdus = input("Introdu un cuvant:\n").lower()
first_char = string_introdus[0]
last_char = string_introdus[-1]
assert first_char == last_char
# Daca sunt diferite da eroare

# Exercitiul 10
string_dat = "0123456789"
numere_pare = string_dat[::2] # (0:len(string_dat):2)
numere_impare = string_dat[1::2]
print(numere_pare, numere_impare)