def largest_product(series, size):
    if not series.isdigit() and len(series) > 0 or size > len(series) or size < 0:
        raise ValueError("Series is not a number")
    li = []
    result = []
    while len(series) >= size > 0:
        li.append(series[0:size])
        series = series[1:]
    for item in li:
        result.append(eval("*".join(item)))
    if result:
        return max(result)
    else:
        return 1


print(largest_product("754302836", 3))
