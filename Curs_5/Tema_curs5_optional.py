"""1. Funcție care primește o lună din an și returnează câte zile are acea luna"""


def give_days_in_month(leap_year, month):
    if month in ["April", "June", "September", "November"]:
        return 30
    elif month in ["January", "March", "May", "July", "August", "October", "December"]:
        return 31
    elif month == "February":
        if leap_year == "True":
            return 29
        else:
            return 28
    else:
        print("Invalid month.")


month = input("Introduce a month:\n")
month = month.capitalize()
leap_year = input("Is a leap_year?(True or False)")
leap_year = leap_year.capitalize()
print(give_days_in_month(leap_year, month))

'''
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)

● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
'''

def calculate(a,b):
    return a + b, a - b, a * b, round(a / b, 2)

adding, substraction, multiplication, division = calculate(2,4)
print(f"Suma:{adding}, diferenta:{substraction}, inmultirea:{multiplication}, impartirea:{division}")

''' 3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
} '''


def how_much_time_a_number_appear(lst):
    dict_num = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    }
    for nr in lst:
        dict_num[nr] += 1
    return dict_num

lst_2 = [0, 0, 2, 3, 3, 3, 4, 5, 6, 9, 9]
print(how_much_time_a_number_appear(lst_2))


'''4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele'''

def find_biggest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


print(find_biggest_number(3,4,5))


'''5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)'''

def sum_of_range_numbers(number):
    """Function will return sum of numbers in range 0 to number inclusive"""
    sum = 0
    for nr in range(number + 1):
        sum += nr
    return sum

print(sum_of_range_numbers(5))


'''HARD'''

'''1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune'''
list1 = [1, 1, 3, 4]
list2 = [2, 2, 5, 6]
# output {3, 4}


def find_common_elements(list1, list2):
    set_1 = set()
    for element_1 in list1:
        for element_2 in list2:
            if element_1 == element_2:
                set_1.add(element_1)
    if set_1:
        return set_1
    else:
        return "No common elements found."

print(find_common_elements(list1, list2))


'''2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.'''

price = 121
discount = 30

def calculate_price_with_discount(price, discount = 0):
    if 0 < discount < 100:
        discounted_price = price - ((discount * price)/100)
        round(discounted_price, 2)
        return discounted_price
    else:
        return f"A discount of {discount}% is invalid."
print(calculate_price_with_discount(price, discount))

'''3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)'''
from datetime import datetime
import pytz
country = "China"
def calculate_date_time(country):
    if country == "Romania":
        time_zone = pytz.timezone('Europe/Bucharest')
        curent_dat_and_time = datetime.now(time_zone)
        return curent_dat_and_time
    elif country == "China":
        time_zone = pytz.timezone("HongKong")
        curent_dat_and_time = datetime.now(time_zone)
        return curent_dat_and_time

print(calculate_date_time(country))


'''4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)'''

date_birthday = datetime(2022, 10, 19, 00)
curent_dat_and_time = datetime.now()
def calculate_time_until_birthday():
    remaining = date_birthday - curent_dat_and_time
    return remaining

print(calculate_time_until_birthday())
