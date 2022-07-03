#Q17.Write a function which will take multiple list as an input and give me concatenation of all the elements as a list.

def add_lst(*lst):
    final_lst = []
    for i in lst:
        if type(i) == list:
            final_lst.extend(i)
    print(final_lst)


add_lst([1, 2, 3], ['you', 'are', True], [2.95, 78, False], 12)