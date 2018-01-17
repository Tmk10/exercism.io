def decode(string):
    string_array = list(string)
    decoded_string = ""
    while string_array:
        if not string_array[0].isdigit():
            decoded_string += string_array[0]
            string_array = string_array[1:]
        elif string_array[0].isdigit() and string_array[1].isdigit():
            string_array[0] = string_array[0] + string_array[1]
            string_array.pop(1)
        elif string_array[0].isdigit() and not string_array[1].isdigit():
            decoded_string += int(string_array[0]) * string_array[1]
            string_array = string_array[2:]
    return decoded_string

def encode(string):
    encoded_string = ""
    while string:
        encoded_string += string[0] if (len(string) - len(string.lstrip(string[0]))) == 1 else str(
            len(string) - len(string.lstrip(string[0]))) + string[0]
        string = string.lstrip(string[0])
    return encoded_string
