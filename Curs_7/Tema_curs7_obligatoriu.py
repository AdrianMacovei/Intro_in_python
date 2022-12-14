from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    @staticmethod
    def descrie():
        print('Cel mai probabil am colturi.')


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura**2

    @property
    def latura(self):
        print("Getter for latura called.")
        return self.__latura

    @latura.setter
    def latura(self, value):
        self.__latura = value
        print("Setter for latura called.")

    @latura.deleter
    def latura(self):
        print("Deleter for latura called.")
        del self.__latura


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        print("Getter for latura called.")
        return self.__raza

    @raza.setter
    def raza(self, value):
        self.__raza = value
        print("Setter for latura called.")

    @raza.deleter
    def raza(self):
        print("Deleter for latura called.")
        del self.__raza

    def aria(self):
        return FormaGeometrica.PI * self.__raza ** 2

    @staticmethod
    def descrie():
        print("Eu nu am colturi.")
p = Patrat(3)
p.descrie()
try:
    p.__latura
except AttributeError as e:
    print('Patrat object has no attribute __latura!')
print(p.aria())
p.latura = 6
print(p.latura)
del p.latura
try:
    print(p.latura)
except AttributeError as e:
    print("'Patrat' object has no attribute '_Patrat__latura'")
c = Cerc(3)
print(c.aria())
print(c.raza)
print(c.aria())
c.raza = 6
print(c.raza)
del c.raza
try:
    print(c.latura)
except AttributeError as e:
    print("'Cerc' object has no attribute '_Cerc__latura'")
c.descrie()
p.descrie()