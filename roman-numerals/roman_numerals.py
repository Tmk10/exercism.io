def numeral(number):
    result = ""
    roman_dict = {1000: 'M', 900: "CM", 500: 'D', 400: "CD", 100: 'C', 90: "XC", 50: 'L', 40: "XL", 10: 'X', 9: "IX",
                  5: 'V', 4: "IV", 1: 'I'}
    for key in roman_dict.keys():
        quotient = number // key
        if quotient > 0:
            result += quotient * roman_dict[key]
            number -= quotient * key
    return result
