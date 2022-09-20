# Exercitiul 1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
# first
for index in range(len(masini)):
    print(f"Masina mea preferata este {masini[index]}.")
# second
for masina in masini:
    print(f"Masina mea preferata este {masina}.")
# third
i = 0
while i < len(masini):
    print(f"Masina mea preferata este {masini[i]}.")
    i += 1

# Exercitiul 2
for i in range(1, len(masini) - 1):
    masini[i] = masini[i].upper()
    print(masini)
else:
    print(masini)

# Exercitiul 3
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
masina_dorita = input("Ce marc de masina doriti sa cumparati?\n")
for masina in masini:
    if masina == masina_dorita:
        print(f"Am gasit masina dorita de dvs.")
        break
    else:
        print(f"Am gasit masina {masina}, mai cautam.")
else:
    print("Nu avem aceasta marca de masina.")

# Exercitiul 4
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == "Lăstun" or masina == "Trabant":
        continue
    print(f"S-ar putea sa va placa {masina}.")

# Exercitiul 5
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
masini_vechi = []
masini_noi = []
for index, masina in enumerate(masini):
    # functia enumerate creeaza o lista de tuple de tipul [(index, masina)] pentru fiecare masina
    # astfel putem schimba mai usor valoarea atunci cand nu stim indexul
    if masina == "Lăstun":
        masini_vechi.append(masina)
        masini[index] = "Tesla"
        masini_noi.append(masini[index])
    elif masina == "Trabant":
        # am schimbat cu 2 masini noi deoarece nu vedeam logiva in a aprea in lista dde 2 ori Tesla
        masini_vechi.append(masina)
        masini[index] = "Range Rover"
        masini_noi.append(masini[index])
print(f"Modelel vechi de masini din parc sunt: {', '.join(masini_vechi)}.")
# join ne va ajuta sa printam fara paranteze patrate si ghilimele
print(f"Modelele noi de masini din parc sunt:{', '.join(masini_noi)}.")

# Exercitiul 6
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

descriere_masina = {
    'Dacia': "se remarca prin cel mai bun raport calitate-pret, dotari full option s i consum redus",
    'Lastun': "masina de colectie pentru pasionati, pastrata in conditii optime ii va creste valoarea proportional cu timpul",
    'Opel': " raport calitate-pret foarte bun, spatiu si confort, consum redus",
    'Audi': "conditii de limuzina, confort foarte ridicat, motor foarte puternic de peste 200 CP, consum mediu",
    'BMW': "bord moder, putere mare peste 200 CP, full option dotari, consum mediu "
}

print("Masinile pe care le avem in parc sunt:")
for item in pret_masini.items():
    print(f"{item[0]} --> pret: {item[1]}")

buget_client = int(input("\nCare este bugetul dvs? (euro)\n"))
masini_in_buget = []
print("Masinile care se incadreaza in buget sunt:\n")
for nume_masina in pret_masini:
    # iteram prin cheile dict pret masini
    # fiecsare cheie se salveaza in nume_masini dupa se adauga in if in paranteze patrate
    # pentru a afla valoarea cheiei
    if pret_masini[nume_masina] <= buget_client:
        masini_in_buget.append(nume_masina)
        print(f"{nume_masina} --> pret: {pret_masini[nume_masina]} euro.")
        # se printeza numele masinii si pretul sau doar daca are pret mai mic de 15000
oprire = 0
nehotarat = True
while nehotarat:
    for masina in masini_in_buget:
        # acest cod ne va ajuta sa iesim din while si for daca atunci cand terminam de prezentat masinile din lista
        # clientul nu este interesat de niciuna
        oprire += 1
        if oprire == (len(masini_in_buget) + 1):
            nehotarat = False
            print("Se pare ca nu avem ceea ce cautati. Va multumim!")
            break
        client_interes = input(f"V-ar interesa achizitionarea masinii {masina} la pretul"
                               f" de {pret_masini[masina]}? (y or n)")
        if client_interes == "y":
            print(f"Ati facut o alegere foarte buna! {masina} are urmatoarele "
                  f"caracteristici: {descriere_masina[masina]}.")
            client_achizitie = input(f"Doriti sa achizitionati masina {masina}? (y or n)")
            if client_achizitie == "y":
                print(f"Felicitari! Sunteti noul proprietar al masinii {masina}.")
                nehotarat = False
                break
            elif client_achizitie == "n":
                continue
            else:
                print("Va rugam raspundeti cu y or n.")
                continue
        elif client_interes == "n":
            continue
        else:
            print("Va rugam raspundeti cu y or n.")
            continue
# am vrut in acest exercitiu sa ma joc putin cu break si continue

# Exercitiul 7

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

count_three = 0
for num in numere:
    if num == 3:
        count_three += 1
print(f"Numarul 3 apare de {count_three} ori.")

# Exercitiul 8
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
print(sum_of_numbers)

# Exercitiul 9
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

max_number = 0
for num in numbers:
    if num > max_number:
        max_number = numbers
print(f"Cel mai mare numar este {max_number}.")

# Exercitiul 10
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for idx, num in enumerate(numbers):
    if num > 0:
        numbers[idx] = -num
print(numbers)
# metoda aceasta ne pastreaza si indexul numarului negativ
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for idx in range(len(numbers)):
    if numbers[idx] > 0:
        numbers[idx] = numbers[idx] * -1
print(numbers)
# mai simplu
