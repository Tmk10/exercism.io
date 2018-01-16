def hey(phrase):
    if phrase.isupper() == True:
        return 'Whoa, chill out!'
    if phrase.strip()[-1:] == "?":
        return 'Sure.'
    if phrase.strip() == "":
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
