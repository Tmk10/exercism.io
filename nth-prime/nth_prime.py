def prime_check(number):
    if number == 2:
        return 1
    else:
        for i in range(2,int(number**0.5) +1):
            if number % i == 0:
                return False
    return True

def nth_prime(positive_number):
    if positive_number < 1:
       raise ValueError("It is not positive number")
    counter = 0
    number = 1
    while counter < positive_number:
        number +=1
        if prime_check(number):
            counter +=1
    return number