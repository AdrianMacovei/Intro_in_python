"""1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()"""
import math


class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self. culoare = culoare

    def descrie_cerc(self):
        print(f"Cercul are culoarea {self.culoare} si raza {self.raza}")

    def aria(self) -> float:
        return math.pi * (self.raza ** 2)

    def diametru(self) -> float:
        return 2 * self.raza

    def circumferinta(self) -> float:
        return 2 * math.pi * self.raza


cerc = Cerc(2, "alba")
cerc.descrie_cerc()
print(cerc.aria())
print(cerc.diametru())
print(cerc.circumferinta())

"""Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie()."""


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Dreptunghiul are culoarea {self.culoare}, lungimea de {self.lungime} si latimea de {self.latime}")

    def aria(self):
        return self.latime * self.lungime

    def perimetrul(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, culoare_noua):
        self.culoare = culoare_noua


dreptunghi = Dreptunghi(2, 3, "rosu")
dreptunghi.descrie()
print(dreptunghi.aria())
print(dreptunghi.perimetrul())
dreptunghi.schimba_culoarea("albastru")
dreptunghi.descrie()


"""3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)"""


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f"Eu sunt {self.nume} {self.prenume} si am un salariu de {self.salariu}")

    def nume_complet(self) -> str:
        return self.nume + self.prenume

    def salariu_lunar(self) -> int:
        return self.salariu

    def salariu_anual(self) -> int:
        return self.salariu * 12

    def marire_salariu(self, procent: int) -> float:
        self.salariu += ((self.salariu * procent)/100)
        return self.salariu


angajat_1 = Angajat("Macovei", "Adrian", 3500)
angajat_1.descrie()
print(angajat_1.nume_complet())
print(angajat_1.salariu_lunar())
print(angajat_1.salariu_anual())
print(angajat_1.marire_salariu(12))

"""4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)"""

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma_retrasa):
        self.sold -= suma_retrasa
        return self.sold

    def creditare_cont(self, suma_introdusa):
        self.sold += suma_introdusa
        return self.sold


cont = Cont(123434, "Macovei Adrian", 4200)
cont.afisare_sold()
print(cont.debitare_cont(1200))
print(cont.creditare_cont(800))