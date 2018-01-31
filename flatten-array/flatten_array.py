def flatten(iterable, flatten_array =[]):
    while iterable:
        if not isinstance(iterable[0], list):
            if iterable[0] !=None:
                flatten_array.append(iterable[0])
            iterable = iterable[1:]

        else:
            flatten(iterable[0])
            iterable = iterable[1:]

    return flatten_array

print(flatten([[0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]]))




