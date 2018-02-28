def saddle_points(matrix):
    transp_matrix = list(zip(*matrix))
    results = []
    if not all(len(i) == len(matrix[1]) for i in matrix):
        raise ValueError("Lists have different length")
    for x in matrix:
        for y in x:
            if y == max(x) and y == min(transp_matrix[x.index(y)]):
                results.append((matrix.index(x), x.index(y)))
    return set(results)
