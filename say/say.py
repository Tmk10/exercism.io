def say(number):
    result_string = ""
    list_from_number = "{:,}".format(number).split(",")
    len_of_list = len(list_from_number)
    non_reapeting_numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    scale = (
        "hundred",
        "thousand",
        "million",
        "billion",
    )
    print(list_from_number)
    print(len(list_from_number))
    for item in list_from_number:
        for digit in item:
            if len(item) == 3 and item[1] != "0":
                result_string += (non_reapeting_numbers[int(digit)] + " " + scale[0] + " and ")
                item = item[1:]
                continue
            elif len(item) == 3 and item[1] == "0":
                result_string += (non_reapeting_numbers[int(digit)] + " " + scale[0])
                item = item[1:]
                continue
            elif len(item) == 2 and item != 0 and item[1] != "0":
                result_string += (non_reapeting_numbers[int(digit + "0")]) + "-"
                item = item[1:]
                continue
            elif len(item) == 2 and digit != "0" and item[1] == "0":
                result_string += (non_reapeting_numbers[int(digit + "0")])
                item = item[2:]
                continue
            elif len(item) == 1 and digit != "0":
                result_string += (non_reapeting_numbers[int(digit)] + "")
        result_string += " " + scale[len(list_from_number) - 1] + " " if len(list_from_number) > 1 else ""
        list_from_number = list_from_number[1:]
    return result_string


print(say(100))
