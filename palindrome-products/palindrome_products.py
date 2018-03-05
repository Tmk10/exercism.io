def is_prime(number):
    if number==1:
        return False
    return all((number % y for y in range(2, number)))


def palindrom_check(number):
    if str(number) == str(number)[::-1]:
        return True
    return False


def factors(n, min_factor, max_factor):
    return [(i, n // i) for i in range(min_factor, int(n ** 0.5) + 1) if n % i == 0 and n / i <= max_factor]


def largest_palindrome(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("Incorrect range")
    for x in range(max_factor, min_factor - 1, -1):
        for y in range(max_factor, min_factor - 1, -1):
            if palindrom_check(x * y):
                if is_prime(x * y):
                    return (x * y, (x, y))
                return (x * y, set(factors(x * y, min_factor, max_factor)))
            
    raise ValueError("No palindrom in given range")


def smallest_palindrome(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("Incorrect range")
    for x in range(min_factor, max_factor - 1):
        for y in range(min_factor, max_factor - 1):
            if palindrom_check(x * y):
                if is_prime(x * y):
                    return (x * y, (x, y))
                return (x * y, factors(x * y, min_factor, max_factor))
    raise ValueError("No palindrom in given range")


