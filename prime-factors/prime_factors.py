def prime_factors(natural_number):
    result =[]
    divider =2
    while natural_number > 1:
        if divmod(natural_number, divider)[1] == 0:
            result.append(divider)
            natural_number = natural_number // divider
        else:
            divider +=1
    return result
