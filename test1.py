# Q1 : Try to print this by using while loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *

n = int(input("Enter the number of rows: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("* ",end = " ")
        j = j + 1
    print("\n")
    i = i + 1