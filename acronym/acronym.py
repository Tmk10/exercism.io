import re
from string import punctuation

def abbreviate(words):
    words = re.findall("\w+",words)
    print(words)
    result_string = ""
    for word in words:
        result_string += word[0].upper()
    return result_string

