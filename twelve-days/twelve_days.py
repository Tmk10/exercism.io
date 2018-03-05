def recite(start_verse, end_verse):
    day_numerals = (
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh",
    "twelfth")
    main_verse = "On the {} day of Christmas my true love gave to me, "
    verse = ('and a Partridge in a Pear Tree.', 'two Turtle Doves, ', 'three French Hens, ', 'four Calling Birds, ',
             'five Gold Rings, ', 'six Geese-a-Laying, ', 'seven Swans-a-Swimming, ', 'eight Maids-a-Milking, ',
             'nine Ladies Dancing, ', 'ten Lords-a-Leaping, ', 'eleven Pipers Piping, ', 'twelve Drummers Drumming, ')
    main_result = []
    for x in range(start_verse, end_verse + 1):
        start_verse, end_verse = x, x
        result = [main_verse.format(day_numerals[start_verse - 1])]
        if end_verse > 1:
            second_part = [sentence for sentence in verse[end_verse - 1::-1]]
        else:
            second_part = [sentence[4:] for sentence in verse[:end_verse]]
        result.extend(second_part)
        result = [("".join(result))]
        main_result.extend(result)
    return main_result
