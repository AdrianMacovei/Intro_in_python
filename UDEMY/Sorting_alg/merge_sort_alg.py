# Python program for implementation of MergeSort
lst = [38, 27, 43, 3, 9, 82, 10]


def mergeSort(lst):
    if len(lst) > 1:

        # Finding the mid of the array
        mid = len(lst) // 2

        # Dividing the array elements
        L = lst[:mid]

        # into 2 halves
        R = lst[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1


mergeSort(lst)
print(lst)