import re


def verify(isbn):
    result = 0
    if re.match("(^\d{1})-(\d{3})-(\d{5})-(\d{1}|X$)", isbn) or re.match("(^\d{9})(\d$|X$)", isbn):
        isbn = isbn.replace("-", "")
        for index, symbol in enumerate(isbn):
            result += int(symbol) * (10 - index) if symbol != "X" else + 10
        if result % 11 == 0:
            return True
        else:
            return False
    return False


print(verify("3598215088"))
