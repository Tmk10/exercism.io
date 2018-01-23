def sum_of_multiples(limit, multiples):
    result_set = set()
    for number in multiples:
        counter = 0
        while counter < limit - number and number != 0:
            counter += number
            result_set.add(counter)
    return sum(result_set)

