def is_isogram(string):
    li =[]
    string = string.replace(" ", "").replace("-", "").casefold()
    for letter in string:
        if letter in li:
            return False
            break
        else:
            li.append(letter)
    return True

# Second solution
""" def is_isogram(string):
    string = string.replace(" ", "").replace("-", "").casefold()
    if len(string) == len(set(string)):
        return True
    else:
        return False"""
