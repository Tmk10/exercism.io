import re


def decode(string):
    decoded_string = ""
    for i in range(len(string)):
        try:
            int(string[i])
        except ValueError:
            decoded_string += string[i]
        else:
            decoded_string += int(string[i]) * string[i + 1]
    return decoded_string


def encode(string):
    encoded_string = ""
    while string:
        encoded_string += str(len(string) - len(string.lstrip(string[0]))) + string[0]
        string = string.lstrip(string[0])
    # return encoded_string.replace("1{1}\D", "")
    return re.sub("1{1}\D", encoded_string,"")


print(encode("XYZzzzxzcasd"))
print(decode("ab2c2afg4 "))
