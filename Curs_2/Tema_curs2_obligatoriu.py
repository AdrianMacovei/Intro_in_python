# Exercitul 1
# Conditiile if, elif, else controleaza curgerea codului, fiind necesara indeplinirea conditiei(True)
# pentru a rula codul din interiorul acesteia
# asemenatoare cu ramurile unui copac sau chiar un labirint, cu 2 directii inainte si la dreapta, daca conditia
# este True se face dreapta si se ruleaza ce este acolo daca nu se merge inainte pana la urmatoarea
# conditie care iarasi se evalueaza.

# Exercitul 2
x = input("Te rog introdu un numar:\n")
if x.isdigit():
    print(f'{x} este un numar natural.')
else:
    print(f'{x} nu este un numar natural.')

# Exercitul 3
x = int(x)
if x < 0:
    print(f'{x} este un numar negativ.')
elif x == 0:
    print(f'{x} este un numar neutru.')
else:
    print(f'{x} este un numar pozitiv.')
#
# Exercitul 4
if -2 < x < 13:
    print(f'{x} este un numar cuprins in intervalul (-2, 13)')
else:
    print(f'{x} nu este un numar cuprins in intervalul (-2, 13)')

# Exercitul 5
y = int(input("Te rog introdu un al doilea numar:\n"))

if (x - y) < 5:
    print(f"Diferenta dintre {x} si {y} este mai mica decat 5.")
else:
    print(f"Diferenta dintre {x} si {y} este mai mare decat 5.")

# Exerictiul 6
if not (5 < x < 27):
    print(f'{x}  nu este inclus in intervalul (5, 27)')
else:
    print(f'{x} este inclus in intervalul (5, 27)')

# Exercitul 7
x = int(input("Te rog introdu un numar:\n"))
y = int(input("Te rog introdu un alt numar:\n"))

if x == y:
    print(f"{x} este egal cu {y}.")
elif x < y:
    print(f"{x} este mai mic decat {y}.")
else:
    print(f"{x} este mai mare decat {y}.")

# Exercitul 8
x, y, z = float(input("Te rog introdu cu spatiu intre ele lungimea celor trei laturi ale triunghiului:/n"))
if x == y == z:
    print("Acesta este un triunghi echilateral.")
elif x == y or y == z or z == x:
    print("Acesta este un triunghi isoscel.")
else:
    print("Acesta este un triunghi oarecare.")

# Exercitul 9
lista_vocale_romana = ["a", "ă", "â", "e", "i", "î", "o", "u"]
lista_consoane_roaman = ["b", "c", "d", "f", "g", "h", "j", "l", "m", "n", "p", "r", "s", "ș", "t", "ț", "v", "z"]
litera = input("Te rog introdu o litera:\n").lower()
if litera in lista_vocale_romana:
    print(f"{litera.upper()} este o vocala.")
elif litera in lista_consoane_roaman:
    print(f"{litera.upper()} este o consoana.")
else:
    print(f"{litera.upper()} nu e este un caracter valid. Fie ai introdus mai mult de un caradcter fie ai folosit "
          f"un caracter ce nu apartine limbii roamne. Try again!")
# cred ca merge si sa facem string cu vocale si string cu consoane
string_vocale = "aăâeiîou"
string_consoane = "bcdfghjlmnprsștțvz"
if litera in string_vocale:
    print(f"{litera.upper()} este o vocala.")
elif litera in string_consoane:
    print(f"{litera.upper()} este o consoana.")
else:
    print(f"{litera.upper()} nu e este un caracter valid. Fie ai introdus mai mult de un caradcter fie ai folosit "
          f"un caracter ce nu apartine limbii roamne. Try again!")

# Exercitul 10
nota = float(input("Introdu nota pe care ai luat-o astazi:\n"))
if 0 <= nota <= 10:
    if nota > 9:
        nota = "A"
        print(f"Nota ta coincide notei {nota}.")
    elif nota > 8:
        nota = "B"
        print(f"Nota ta coincide notei {nota}.")
    elif nota > 7:
        nota = "C"
        print(f"Nota ta coincide notei {nota}.")
    elif nota > 6:
        nota = "D"
        print(f"Nota ta coincide notei {nota}.")
    elif nota > 4:
        nota = "E"
        print(f"Nota ta coincide notei {nota}.")
    else:
        nota = "F"
        print(f"Nota ta coincide notei {nota}.")
else:
    print("Nota invalida")
