from itertools import combinations



def is_triangle(func):
    def wrapper(arg):
        if not all(item >= max(arg) for item in map(sum, combinations(arg, 2))):
            return False
        return func(arg)
    return wrapper


def is_equilateral(sides):
    if len(set(sides)) == 1 and not 0 in set(sides):
        return True
    return False

@is_triangle
def is_isosceles(sides):
    if len(set(sides)) == 2 or len(set(sides)) == 1:
        return True
    return False

@is_triangle
def is_scalene(sides):
    if len(set(sides)) == 3:
        return True
    return False
