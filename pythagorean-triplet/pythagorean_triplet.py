def is_coprime(*args):
    div_list = []
    for arg in args:
        for i in range(2, arg + 1):
            if not arg % i:
                div_list.append(i)
                if div_list.count(i) > 1:
                    return False
    return True


def primitive_triplets(number_in_triplet):
    if number_in_triplet % 2:
        raise ValueError(str(number_in_triplet) + " is odd")
    result = []
    for m in range(number_in_triplet // 2 + 1, 1, -1):
        for n in range(1, number_in_triplet // 2 + 1):
            if 2 * m * n == number_in_triplet and m > n and is_coprime(m, n):
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                result.append(tuple(sorted([a, b, c])))
    return set(result)


def triplets_in_range(range_start, range_end):
    range_end += 1
    return set([(x, y, z) for x in range(range_start, range_end) for y in range(range_start, range_end) for z in
                range(range_start, range_end) if x ** 2 + y ** 2 == z ** 2 and x < y])


def is_triplet(triplet):
    triplet = sorted(list(triplet))
    if triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2:
        return True
    return False

