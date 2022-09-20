fructe = ["mar", "banana", "portocala", 3, True, 3]
#listele in python pot sa cuprinda elemente de tiputi diferite
#au dimensiune dinamica
print(fructe)
#afisam un element in f de index
print(fructe[0])
#adaugam un nou element
fructe.append("rosie")

#suprascriere element
fructe[0] = "para"
print(fructe)

#aflam dimensiune
print(len(fructe))

#scoate si ne returneza ultimu element
last = fructe.pop()
print('ultimul elem: ', last)
print('lista: ', fructe)

#de cate ori apare un element
print(fructe.count(3))

#extindem lista
fructe_exotice = ["ananas", "kiwi"]
fructe.extend(fructe_exotice)
print(fructe)

