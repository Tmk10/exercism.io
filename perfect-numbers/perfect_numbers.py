def aliquot(number):
    aliquot_sum = 0
    for i in range(1, number):
        if number % i == 0:
            aliquot_sum += i
    return aliquot_sum

def classify(number):
    if number < 1:
        raise ValueError("Only natural numbers")
    if number == aliquot(number):
        return "perfect"
    if number < aliquot(number):
        return "abundant"
    if number > aliquot(number):
        return "deficient"




