#Q15.Write a function which will be able to print an index of all primitive element which you will pass.

def primitive_element(*db):
    print("Index of primitive elements in the collection: ")
    for i in range(0, len(db)):

        if type(db[i]) == int or type(db[i]) == float or type(db[i]) == str or type(db[i]) == bool:
            print(i, db[i], type(db[i]))

    else:
        print("Rest are non primitive elements")


primitive_element(213, 42, 45.234, True, (123, 435.241, 'abc'), [False, 213, 1, 4, 45.2454, 241, 'google'], 'shubh',
                  False, 325.254, 3)

