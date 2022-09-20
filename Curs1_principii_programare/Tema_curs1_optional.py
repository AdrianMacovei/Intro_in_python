from math import ceil

# Exercitiul 1
string_impar = input("Te rog sa introduci un string cu dimensiune impara:\n")
dim_string = int(len(string_impar))
char_middle = ceil((dim_string / 2)-1)
print(f'Caracterul din mijlocul cuvantului introdus este {string_impar[char_middle]}.')

# Exercitiul 2
string_pali = input("Te rog sa introduci un string cu dimensiune impara:\n")
assert (str(string_pali) == str(string_pali)[::-1])
print("Cuvantul introdus este palindrom.")
# am incercat si cu if deoarece pe assert il vad ca pe un if condition mai primitiv
if string_pali == string_pali[::-1]:
    print("Cuvantul introdus este palindrom.")
else:
    print("Cuvantul introdus nu este palindrom.")

# Exercitiul 3
string_1, string_2 = input("Te rog sa introduci 2 cuvinte: \n").split(); print(string_1, "\n", string_2)

# Exercitiul 4
cuvant = input("Introdu un cuvant de la tastatura:\n")
first_char = cuvant[0]
# ne va da prima litera/char
last_index = int(cuvant.rindex(first_char))
# asa aflam indexul unde gasim prima litera ultima oara in string de la stanga la dreapta
rest_chars = cuvant[last_index:len(cuvant)]
# asa putem face sa printam doar anumite caractere din string dintr-un interval(index)
# important print(string[2:5]) va printa doar caracterele de la index 2 pana la 4 nu si pe cel de la index 5
# (string slice)
cuvant = cuvant[1:last_index].replace(first_char, first_char.upper())
# asa schimbam prima litera in upper in afara de prima aparitie si ultima
cuvant_cu_upper = first_char + cuvant + rest_chars
print(cuvant_cu_upper)
# printam ce o iesit

# Exercitiul 5
user = input("Introduceti un user-name:\n")
password = input("Introduceti o parola:\n")
password = "*" * len(password)
print(f'Parola pentru userul {user} este {password} si are {len(password)} caractere')
