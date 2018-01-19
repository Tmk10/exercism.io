def slices(series, length):
    result =[]

    if length > len(series) or length == 0:
        raise ValueError("Length is incorrect")
    while len(series) >= length:
        result.append(list(map(int,series[0:length])))
        series = series[1:]
    return result





print(slices("01234",1))