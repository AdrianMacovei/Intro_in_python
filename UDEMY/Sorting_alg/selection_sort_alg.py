lst = [10, 5, 8, 20, 2, 18]
n = len(lst)
for i in range(n):
    min_index = i
    for j in range(i+1, len(lst)):
        if lst[min_index] > lst[j]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]
print(lst)
# se cauta cel mai mic element se pune la primul index, dupa care se cauta cel ami mic in elementele ramase si se adauga la ultimul index
# se gaseste mai sus cel mai mic 2 si se schimba cu 10
# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:
# One loop to select an element of Array one by one = O(N)
# Another loop to compare that element with every other Array element = O(N)
# Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)