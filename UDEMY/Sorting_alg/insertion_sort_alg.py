# Traverse through 1 to len
# ex for better undestanding 7 will be compare with 9, 7<9 atunci la indecele 0 se va pune 7 iar 9 va trece la indicele 1
# apoi 2 se comapra cu 9 este mai mic deci 9 va trece in locul lui 2 si se compara acum 2 cu 7 este mai mic
# se va face schimbul 2 la indicele 0 si 7 la indicele 1 daca nu era mai mic ramanea 2 la indicele 1
lst = [9, 7, 2, -5, 12, 3, 1, -6, -4, 3]
for i in range(1, len(lst)):

    key = lst[i]
    # Move elements of lst[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i - 1
    while j >= 0 and key < lst[j]:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key
print(lst)