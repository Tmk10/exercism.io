def recite(start=0, take=1):
    result = []
    bottle_counter = start
    take_counter = take
    delta = bottle_counter - take_counter
    for x in range(bottle_counter, delta, -1):
        if bottle_counter:
            result.append("{0} {1} of beer on the wall, {0} {1} of beer.".format(bottle_counter,
                                                                                 "bottles" if bottle_counter > 1 else "bottle"))
        else:
            result.append("No more bottles of beer on the wall, no more bottles of beer.")
        if take_counter:
            if bottle_counter > 1:
                result.append(
                    "Take one down and pass it around, {0} {1} of beer on the wall.".format(bottle_counter - 1,
                                                                                            "bottles" if bottle_counter - 1 > 1 else "bottle"))
            if bottle_counter == 1:
                result.append(("Take it down and pass it around, ""no more bottles of beer on the wall."))
            if bottle_counter == 0:
                result.append(("Go to the store and buy some more, ""99 bottles of beer on the wall."))
            bottle_counter -= 1
            take_counter -= 1
            if take_counter != 0:
                result.append('')

    return result