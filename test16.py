#Q16.Write a function which will take input as a dict and give me out a list of all the values even in case of 2 level nesting it should work.

def dict_elements(*args):
    for i in args:
        print(i.keys())

        for j in i.keys():
            print(i[j])


dict_elements({'a': 12, 'abc': [99.8, 8, False], 'b': 34.87, 'c': True})