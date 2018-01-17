from itertools import permutations

def detect_anagrams(word, candidates):
    anagrams_list=[]
    for phrase in candidates:
        if len(phrase) == len(word) and word.casefold() != phrase.casefold():
            for str in permutations(phrase):
                if "".join(str).casefold() == word.casefold():
                    anagrams_list.append(phrase)
                    break

    return anagrams_list





print(detect_anagrams("Orchestra",["carthorse", "carthorse", "radishes"]))