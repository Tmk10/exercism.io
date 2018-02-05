def translate(text):
    result = ""
    wovels = ("a", "e", "i", "o", "u")
    for item in text.split():
        if item[0] in wovels:
            result = text + "ay"
        else:
            suffix = ""
            for letter in item:
                if letter == "u" and suffix[-1] == "q":
                    suffix += letter
                    item = item[1:]

                elif letter not in wovels:
                    suffix += letter
                    item = item[1:]
                    wovels = ("a", "e", "i", "o", "u", "y")

                else:
                    result += " " + item + suffix + "ay"
                    break
    return result.lstrip()
