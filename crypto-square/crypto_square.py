from re import findall
import math


def encode(plain_text):
    if len(plain_text) < 1:
        return ""
    plain_text = findall('\w', plain_text.lower())
    r = round(math.sqrt(len(plain_text)))
    c = round(len(plain_text) / r)
    result = [None for _ in range(r)]
    counter = 0
    while plain_text:
        result[counter] = list(plain_text[0:c])
        plain_text = plain_text[c:]
        if len(result[counter]) < c:
            result[counter].extend([" "] * (c - len(result[counter])))
        counter += 1
    result = ["".join([result[y][x] for y in range(r)]) for x in range(c)]
    return " ".join(result)
