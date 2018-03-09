from itertools import combinations


def is_triangle(sides):
    if not all(item >= max(sides) for item in map(sum, combinations(sides, 2))):
        return False
    return True


def is_equilateral(sides):
    if len(set(sides)) == 1 and not 0 in set(sides):
        return True
    return False


def is_isosceles(sides):
    if is_triangle(sides):
        if len(set(sides)) == 2 or len(set(sides)) == 1:
            return True
    return False


def is_scalene(sides):
    if is_triangle(sides):
        if len(set(sides)) == 3:
            return True
    return False
