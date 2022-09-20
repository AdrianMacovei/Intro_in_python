class Cont_bancar:
    # atribute, fields definite prin constructor
    def __init__(self, titular_cont, iban):  # asa se face constructor in python
        self.titular_cont = titular_cont  # in java this
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.__pin = 7777
        self.incercari_activare = 0

    # interogare sold = metoda sau actiunea clasei
    def interogare_sold(self):
        print(f'Titular cont {self.titular_cont}')
        print(f'IBAN-ul contuluui este {self.iban}')
        print(f'Sold cont: {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr. incercari gresite {self.incercari_activare}')
        print("-----------------------------------------")

    # activare cont = metoda sau actiunea clasei
    def activare_cont(self, pin_utilizator):
        if self.incercari_activare < 3:
            if pin_utilizator == self.__pin:
                print(f'Cardul clientului {self.titular_cont} a fost activat cu succes')
                self.activ = True
            else:
                print(f'PIN gresit dl. {self.titular_cont}')
                self.incercari_activare += 1
        else:
            self.activ = False
            print("Ati gresit PIN-ul de trei ori. Contul dvs este blocat")

    # metoda alimentare_cont
    def alimentare_cont(self, suma_depusa):
        self.salut()
        self.sold += suma_depusa
        print(f'Ati depus suma de {suma_depusa} si acum aveti soldul contului egal cu {self.sold}')

    # metoda debitare cont (cheltuire)
    def debitare_cont(self, suma_cheltuita):
        self.salut()
        if suma_cheltuita <= self.sold:
            self.sold -= suma_cheltuita
            print(f'Ati debitat suma de  {suma_cheltuita} si acum aveti soldul egal cu {self.sold}')
        else:
            print(f'Suma nu este disponibila')

    def salut(self):
        print(f'Buna, {self.titular_cont}')

