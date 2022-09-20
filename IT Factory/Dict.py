#declaram si initializam
dict_gol = {}

note_elevi = {"Gigel":10,"Costel":9, "Ana":10}

#adaugare de elemente
note_elevi["Sebi"] = 7

#printam dict
print(note_elevi)

#aflam elemente
print(note_elevi["Gigel"])
print(note_elevi.get("Gigel"))

#actualizam valori
note_elevi["Costel"] = 10
print(note_elevi)

#aflam dimensiunea
print(len(note_elevi))

#stergem valori
note_elevi.pop("Gigel")
print(note_elevi.get("Gigel", 'nu mai avem acest elev'))

# returneaza cheile
print (note_elevi.keys())

#SET = lista de elemente in care fiecare element apare o singura data
#Coada = pers1, pers2, pers3 structura de tip FIFO - first in first out
#Stiva LIFO- last in first out