def say(number):
    if int(number) < 0 or int(number) >= 1e12:
        raise ValueError("Incorrect number")
    number=int(number)
    list_from_number = [int(item) for item in "{:,}".format(number).split(",")]
    result_string=""
    if number == 0:
        result_string = "zero"
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
    scale = {

        2: "thousand",
        3: "million",
        4: "billion",
    }
    for item in list_from_number:
        main = item // 100
        reminder = item - (main * 100)
        if main:
            result_string += non_reapeting_numbers[main] + " hundred" if main * 100 == item else non_reapeting_numbers[
                                                                                               main] + " hundred" + " and "
        if reminder:
            result_string += non_reapeting_numbers[reminder] if reminder % 10 ==0 or reminder < 20 else non_reapeting_numbers[reminder //10 * 10] + "-" + non_reapeting_numbers[reminder % 10]

        if item > 0:
            result_string += " " + scale[len(list_from_number)] + " " if len(list_from_number) > 1 else ""

        list_from_number = list_from_number[1:]

    return result_string.rstrip()

