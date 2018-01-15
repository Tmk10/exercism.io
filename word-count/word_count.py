import re
def word_count(phrase):
    phrase = re.sub("[^0-9a-zA-Z']+", ' ', phrase).rstrip().casefold()
    phrase = phrase.split(" ")
    print(phrase)
    result = {}
    for word in phrase:
        if word in result:
            continue
        else:
            result[word] = phrase.count(word)

    return result


