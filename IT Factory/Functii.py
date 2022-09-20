def printGreeting():
    print("Buna ziua! Bine ati venit!")

def print_greeting_by_name(nume, prenume):
    print(f"Buna ziua, {nume} {prenume}!")

def media_nr(a, b, c):
    return((a+b+c)/3)

def pi_value():
    return 3.14159265358979323846 # return este ultima instructuine ce va fi executata

#exercitiu daca persoana este majora return true altfel false
def verificare_varsta(varsta):
    if varsta >= 18:
        return True
    else:
        return False
# se ia varsta utilizatorului
age = int(input("Ce varsta aveti?\n"))
if verificare_varsta(age) == True:
    print("Esti major")
else:
    print("Esti minor")
#zona de apelare functie
printGreeting()
print_greeting_by_name('Macovei', 'Adrian')
print(media_nr(3, 3, 4))
print(pi_value())