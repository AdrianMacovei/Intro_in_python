from OOP.Cont_bancar import Cont_bancar

cont1 = Cont_bancar("Adrian Macovei", 'RO0001')
cont2 = Cont_bancar("Bogdan Macovei", 'RO002')

cont1.activare_cont(7777)
cont2.activare_cont(7777)


cont1.alimentare_cont(1260)
cont2.alimentare_cont(780.60)



cont1.debitare_cont(1300)
cont2.debitare_cont(780.60)
cont1.interogare_sold()
cont2.interogare_sold()



