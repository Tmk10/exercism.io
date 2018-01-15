import string


def is_pangram(sentence):
    sentence = sentence.replace(" ", "").casefold()
    li = string.ascii_lowercase
    for letter in li:
        if letter not in sentence:
            return False


    return True
