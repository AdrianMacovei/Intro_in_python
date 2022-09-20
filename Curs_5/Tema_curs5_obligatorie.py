"""1.Funcție care să calculeze și să returneze suma a două numere"""


def add_two_numbers(a=0, b=0):
    """Return a + b"""
    return a + b


'''2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar'''


def verify_number_is_even(a):
    """Return true if number is even and False otherwise"""
    if a % 2 == 0:
        return True
    else:
        return False


'''3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)'''


def calculate_name_characters(name):
    """Return numbers of characters in string"""
    cnt = 0
    name = name.replace(" ", "")
    name = name.replace("-", "")
    for letter in name:
        cnt += 1
    return cnt


print(calculate_name_characters(input("Introduce your full name:\n")))


'''4. Funcție care returnează aria dreptunghiului'''


def calculate_area_of_rectangle(length, width):
    """Return area of rectangle"""
    return length * width


print(calculate_area_of_rectangle(2, 2))


'''5. Funcție care returnează aria cercului'''


def calculate_area_of_circle(r):
    """Calculate and return area of circle"""
    pi = 3.14
    return pi * (r * r)


print(calculate_area_of_circle(5))

'''6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.'''


def verify_char_in_string(string, char_to_verifie):
    """Verify if a char is in string, return True if is in and Flase otherwise"""
    for char in string:
        if char == char_to_verifie:
            return True
    return False


print(verify_char_in_string('abcdef', 'g'))

'''7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''


def find_lower_and_upper(string):
    """Print number of characters with lower case and upper case in  a given string"""
    cnt_lower_case = 0
    cnt_upper_case = 0
    string = string.replace(" ", "")
    for letter in string:
        if letter == letter.upper():
            cnt_upper_case += 1
        elif letter == letter.lower():
            cnt_lower_case += 1
    print(f"Nr de caractere lower case este {cnt_lower_case}.")
    print(f"Nr de caractere upper case exte {cnt_upper_case}.")


find_lower_and_upper("Mama mama MAMA")

'''8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive'''


def change_negativ_to_positive(lst_nr):
    """Change all negativ numbers in a list with positive and return it"""
    for idx in range(len(lst_nr)):
        if lst_nr[idx] < 0:
            lst_nr[idx] = -lst_nr[idx]
    return lst_nr


print(change_negativ_to_positive([1, -3, -3, 3, 4]))

'''9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''


def is_biggest(x, y):
    if x > y:
        print(f"Primul număr {x} este mai mare decat al doilea nr {y}.")
    elif y > x:
        print(f"Al doilea nr {y} este mai mare decat primul nr {x}.")
    else:
        print("Numerele sunt egale.")


is_biggest(3, 2)

'''10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''


def insert_number_in_set(nr, set_1):
    """Function will return True if nr will be inserted in set, false if number
    is already in set"""
    if nr in set_1:
        print(f"Nu am adaugat {nr} în set. Acesta există deja.")
        return False
    else:
        set_1.add(nr)
        print(f"Am adaugat {nr} în set.")
        return True


set_1 = {1, 2, 3}
print(insert_number_in_set(5, set_1))
