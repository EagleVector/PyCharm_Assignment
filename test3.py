#Q3 : Try to print all the number divisible by 3 in between a range of 40 - 400.

i = 40
while i <= 400:
    if i % 3 == 0:
        print(i , end = " ")
    i = i + 1