my_var = 5
# utilizam standardul snake_case pentru a numi variabila
# numele variabilei trebui sa inceapa cu litere sau _ nu cu cifre
# putem sa scriem o variabila cu litera mare doar daca aceasta este Constanta
DAYS_IN_WEEK = 7  # variabila care nu isi modifica valoarea
# pot pune _ la inceputul unei variabile dar nu este recomandat
_var = 11  # variabila privata in OOP
# python este case sensitive
myvar = 12  # variabile diferite
myVar = 45

a, b, c = 10, 20, 30  # initializare pe aceeasi linie

# d, f, g, h = 10, 34, 34, 45, 56  # da eroare deoarece nu poate mapa cum trebuie valorile

g = h = i = "Aceeasi valoare"
# initializare string gol
var1 = ""
var2 = 5
print(var1)
print(var1 == var2)
# nu putem folosi keywords in numele variabilei sau nume de functii, librarii
# print = 100  #aici o  sa dea eroare deoarece am suprascris functia prin in integer
# numele trebuie sa fie explicit, usor de inteles pentru oricine citeste cosul

# bolean tipuri de date binare (0/1, true/false)
# functia type() ne spune de ce tip este o anumita variabila
print(type(var2))
from math import floor, ceil

# convertirea explicita a unei variabile dintr-un string  in  int, str, bool, float
# putem converti float -- int dar pierdem zecimalele
# daca vrem rotunjire in sus (folosim functia ceil) sau jos (functia floor) din libraria math
nr_zecimal = 100.6
print(ceil(nr_zecimal))
print(floor(nr_zecimal))

# cand facem type casting trebuie sa facem asignare
alfa = "1234"
int(alfa)  # nu se schimba tipul variabile
