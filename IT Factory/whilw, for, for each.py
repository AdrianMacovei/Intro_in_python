
litri_benzina = 10

while litri_benzina > 0:
    print("Vruum!, Vruum!")
    litri_benzina -= 1
    if litri_benzina <=3:
        print("Se aprinde becul rosu")

print("STOP! Nu mai avem benzina!")

# for loop
for i in range(1,102, 2): #dalmatienii din 2 in 2 -pasul lui i
    print(f'Dalmatianul cu nr {i}')
#parcurgere lista cu for prin intermediul indexului'
numere = [3,7, 10, 20, 20]
for i in range (0, len(numere)):
    print(f'Numarul curent este {numere[i]}')

# for each

for numar in numere:
     #for letter in word for culoare in culori
    print (f'Numarul curent este {numar} ')
s= 0
for numar in numere:
    s += numar
print(f'Suma numerelor este {s}')

# de cate ori apare 3 in [3,2,3,3,2,2]
num = [3, 2, 3, 3, 2, 2, 3, 5]
aparitie = 0
for numar in num:
    if numar == 3:
        aparitie += 1
print(f'Numarul 3 apare de {aparitie} ori')