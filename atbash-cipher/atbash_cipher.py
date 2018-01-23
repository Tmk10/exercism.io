from string import ascii_lowercase


def encode(plain_text):
    cipher = "".maketrans(ascii_lowercase, ascii_lowercase[::-1])
    encoded_text = ""
    lst = [str(letter.casefold().translate(cipher)) for letter in plain_text if str(letter).isalnum()]
    while lst:
        encoded_text += "".join(lst[:5]) + " "
        lst = lst[5:]
    return encoded_text.rstrip()


def decode(ciphered_text):
    cipher = "".maketrans(ascii_lowercase, ascii_lowercase[::-1])
    decoded_text = ciphered_text.translate(cipher)
    return decoded_text.replace(" ", "")

