from string import ascii_lowercase
from random import randint


class Caesar():
    def __init__(self,key=3):
        self.key = key


    def encode(self, text):
        to_cipher = ""
        text = text.lower().replace(" ", "")
        for letter in text:
            to_cipher += letter if letter in ascii_lowercase else ""
        rotate = "".maketrans(
            {k: chr((ord(k) + self.key)) if (ord(k) + self.key) <= 122 else chr((ord(k) + self.key - 26)) for k in
             ascii_lowercase})
        to_cipher = to_cipher.translate(rotate)
        return to_cipher

    def decode(self, text):
        rotate = "".maketrans(
            {k: chr((ord(k) - self.key)) if (ord(k) - self.key) >= 97 else chr((ord(k) - self.key + 26)) for k in
             ascii_lowercase})
        text = text.translate(rotate)
        return text


class Cipher(Caesar):
    def __init__(self, key=None):
        if key and key.isalpha() and key.islower():
            self.key = key
        elif key == None:
            self.key = "".join([chr(randint(97, 122)) for _ in range(0, 101)])
        else:
            raise ValueError("Incorrect key")
        cipher = {key: value for value, key in zip(range(0, 26), ascii_lowercase)}
        self.cipher_list = [cipher[x] for x in self.key]

    def encode(self, text):
        while len(text) > len(self.cipher_list):
            self.cipher_list.extend(self.cipher_list[0:])
        result =[Caesar(key).encode(letter) for key, letter in zip(self.cipher_list,text)]
        return "".join(result)

    def decode(self, text):
        while len(text) > len(self.cipher_list):
            self.cipher_list.extend(self.cipher_list[0:])
        result =[Caesar(key).decode(letter) for key, letter in zip(self.cipher_list,text)]
        return "".join(result)
