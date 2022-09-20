# Exercitul 1
music_notes = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI", "DO"]
print(music_notes)
music_notes = music_notes[::-1]
print(music_notes)
music_notes.reverse()
print(music_notes)

# Exercitul 2
print(f'Nota DO apare de {music_notes.count("DO")} ori.')

# Exercitul 3
list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
# first method
list_1.extend(list_2)
print(list_1)
# second method
# print(list_1 + list_2)

# Exercitul 4
list_1.sort()
print(list_1)
list_1.remove(0)
print(list_1)

# Exercitul 5
list_1 = [3, 1, 0, 2, 6, 5, 4]
empty_list = []
if list_1 == empty_list:
    print("Lista este goala.")
else:
    print("Lista nu este goala.")
# mai este varianta cu lungimea listei egal cu 0

# Exercitul 6
list_1.clear()
print(list_1)

# Exercitul 7
if list_1 == empty_list:
    print("Lista este goala.")
else:
    print("Lista nu este goala.")

# Exercitul 8
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
keys = dict1.keys()
print(keys)

# Exercitul 9
print(f"Ana a luat nota {dict1['Ana']}.")
print(f"Gigel a luat nota {dict1['Gigel']}.")
print(f"Dorel a luat nota {dict1['Dorel']}.")

# Exercitul 10
dict1["Dorel"] = 6
print(f'Dorel are acum nota {dict1["Dorel"]}.')

# Exercitul 11
# del dict1("Gigel")
print(dict1)
dict1["Ionica"] = 9
print(dict1)

# Exercitul 12
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

# Exercitul 13
if weekend <= zile_sapt:
    print("Weekend este un subset al zilelor din săptămânii.")
else:
    print("Weekend nu este un subset al zilelor din săptămânii.")
# or
if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor din săptămânii.")
else:
    print("Weekend nu este un subset al zilelor din săptămânii.")

# Exercitul 14
print(zile_sapt.difference(weekend))

# Exercitul 15
print(zile_sapt.intersection(weekend))