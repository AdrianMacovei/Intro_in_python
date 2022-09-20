# bubble sort algorithm compare 1 by 1 start at index 0 and 1
# and change place between them
# after first loop we have a max setted at index len(lsita)-1
# is stable because dont change index of elem if they are equal
# alte_numere = [9, 7, 2, -5, 12, 3, 1, -6, -4, 3]
# n = len(alte_numere) -1
# while True:
#     swapped = False
#     for index in range(n):
#         if alte_numere[index] > alte_numere[index + 1]:
#             alte_numere[index], alte_numere[index + 1] = alte_numere[index + 1], alte_numere[index]
#             swapped = True
#     if swapped == False:
#         break
# print(alte_numere)

# official version
alte_numere = [9, 7, 2, -5, 12, 3, 1, -6, -4, 3]
n = len(alte_numere)

for i in range(n):
    swapped = False
    for j in range(n-i-1):
        if alte_numere[j] > alte_numere[j + 1]:
            alte_numere[j], alte_numere[j + 1] = alte_numere[j + 1], alte_numere[j]
            swapped = True
    if swapped == False:  # for more efficiency
        break
print(alte_numere)