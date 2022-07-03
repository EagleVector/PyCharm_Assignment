#Q14.You have to write a function which will take a string and return the length of it without using a inbuilt fun len.

def str_len(s):
    count = 0
    if type(s) == str:
        for i in s:
            count = count + 1
        print("Length of the string is: ", count)

    else:
        print("Please Enter a string")


str_len('Abra ka Dabra')