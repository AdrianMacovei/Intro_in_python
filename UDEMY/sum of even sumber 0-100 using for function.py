#Write your code below this row 👇
sum_even = 0
for sum in range (1,101):
    # or can use range (0,101,2) pentru a adauga numere din 2 in 2
    if sum % 2 == 0:
        sum_even += sum
print (sum_even)