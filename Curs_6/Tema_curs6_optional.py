"""1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)

● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/"""
from datetime import datetime
from prettytable import PrettyTable


class Factura:
    SERIE = 1234567789

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua

    def schimba_pretul(self, pret_nou):
        self.pret_buc = pret_nou

    def schimba_nume__produs(self, nume_nou):
        self.nume_produs = nume_nou

    def genereaza_factura(self):
        print(f"Factura seria {Factura.SERIE} numar {self.numar}")
        print(f"Data: {datetime.now()}")
        total = self.cantitate * self.pret_buc
        # print(f"Produs | Cantitate | Pret bucata | Total\n"
        #       f"{self.nume_produs} | {self.cantitate} | {self.pret_buc} | {self.cantitate * self.pret_buc}")
        mytable = PrettyTable(["Produs", "Cantitate", "Pret bucata", "Total"])
        mytable.add_row([self.nume_produs, self.cantitate, self.pret_buc, total])
        print(mytable)


factura = Factura(1, "televizor", 5, 1500)
factura.schimba_cantitatea(8)
factura.schimba_pretul(1400)
factura.schimba_nume__produs("frigider")
factura.genereaza_factura()

"""2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0"""


class Car:
    def __init__(self, model, maxim_speed):
        self.model = model
        self.max_speed = maxim_speed
        self.brand = "Ford"
        self.actual_speed = 0
        self.disponible_colors = {"red", "black", "grey", "white", "blue"}
        self.color = "grey"
        self.registered = False

    def describe_car(self):
        print(f"Here is a {self.brand} {self.model} with {self.color} color, and a maxim speed of {self.max_speed}."
              f" Car is registered: {self.registered} and it's actual speed is {self.actual_speed}.")

    def register_car(self):
        self.registered = True

    def paint_car(self, new_color):
        if new_color in self.disponible_colors:
            self.color = new_color
        else:
            print("This color isn't available.")

    def accelerate_car(self, value):
        if value < 0:
            print("Invalid, only positive value")
        else:
            if (self.actual_speed + value) <= self.max_speed:
                self.actual_speed += value
            else:
                print("Value too big, maximum speed exceeded!!!")
            if self.actual_speed == self.max_speed:
                print("Maximum speed reached!")

    def brake_car(self):
        self.actual_speed = 0


car = Car("Focus", 180)
car.describe_car()
car.register_car()
car.paint_car("black")
car.paint_car("yellow")
car.accelerate_car(-30)
car.accelerate_car(80)
car.accelerate_car(101)
car.brake_car()
car.describe_car()


"""3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:

● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict"""


class TodoList:
    dict_with_tasks = {}

    @staticmethod
    def add_task(name, decription):
        TodoList.dict_with_tasks[name] = decription

    @staticmethod
    def completion_task(name):
        print(f"Congratulation! You finish task {name}")
        del TodoList.dict_with_tasks[name]

    @staticmethod
    def show_my_tasks():
        for tasks in TodoList.dict_with_tasks:
            print(tasks)
        # print(TodoList.dict_with_tasks.keys())

    @staticmethod
    def show_more_details(name_of_task):
        if name_of_task in TodoList.dict_with_tasks:
            print(TodoList.dict_with_tasks[name_of_task])
        if name_of_task not in TodoList.dict_with_tasks:
            ask = input(f"Do you want to add the task '{name_of_task}' in TODO list? (y or n)")
            ask = ask.lower()
            if ask == "y":
                description = input(f"Please describe task named {name_of_task}:\n")
                TodoList.dict_with_tasks[name_of_task] = description
            else:
                print("La revedere!")


todo = TodoList()

todo.add_task("learn IT", "for 3 hours per day i will write code and i will make prjects")
todo.add_task("learn for exam", "for 3 hours per day i will learn from books to take my exam")
todo.add_task("cooking cake", "make a delicious cake")
todo.show_my_tasks()
todo.completion_task("cooking cake")
todo.show_my_tasks()
todo.show_more_details("learn IT")
todo.show_more_details("learn to sing")
todo.show_my_tasks()
