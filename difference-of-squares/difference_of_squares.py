def square_of_sum(count):
    sum = 0
    while count > 0:
        sum += count
        count -= 1
    return sum ** 2


def sum_of_squares(count):
    sum = 0
    while count > 0:
        sum += count ** 2
        count -= 1
    return sum


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)


print(square_of_sum(10))
print(sum_of_squares(10))
