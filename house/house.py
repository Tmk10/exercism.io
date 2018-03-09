verses = ['the house that Jack built.', 'the malt', 'the rat', 'the cat', 'the dog',
          'the cow with the crumpled horn', 'the maiden all forlorn',
          'the man all tattered and torn', 'the priest all shaven and shorn',
          'the rooster that crowed in the morn', 'the farmer sowing his corn',
          'the horse and the hound and the horn']
verbs = (
"is", "lay in", "ate", "killed", "worried", "tossed", "milked", "kissed", "married", "woke", "kept", "belonged to")
adverbs = ("This", "that",)


def recite(start_verse, end_verse):
    main_result = []
    pattern = "{} {} {}"
    def verse(start_verse):
        result = []
        for j in range(start_verse):
            if start_verse - j == 1:
                result.append(pattern.format(adverbs[0], verbs[0], verses[j]))
            else:
                result.append(pattern.format(adverbs[1], verbs[j + 1], verses[j]))
        result.reverse()
        if start_verse < end_verse and i != end_verse :
            result.append("")
        return result
    for i in range(start_verse,end_verse+1):
        main_result.extend(verse(i))
    return main_result