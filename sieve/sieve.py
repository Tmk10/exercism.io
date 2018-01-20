from math import sqrt


def sieve(limit):
    lst = list(range(2, limit + 1))
    gen = (x for x in lst if x < sqrt(limit))
    for number in gen:
        for x in lst:
            if x % number ==0 and x != number:
                lst.remove(x)
    return lst




