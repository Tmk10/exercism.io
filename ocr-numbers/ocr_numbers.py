ocr_dict = {175: "0", 9: "1", 158: "2", 155: "3", 57: "4", 179: "5", 183: "6", 137: "7", 191: "8", 187: "9"}


def convert(input_grid):
    if len(input_grid[1]) % 3 or len(input_grid) % 4:
        raise ValueError("Wrong input")
    result = []
    for y in range(0, len(input_grid), 4):
        for x in range(0, len(input_grid[0]), 3):
            grid = [input_grid[y][x:x + 3], input_grid[y + 1][x:x + 3], input_grid[y + 2][x:x + 3],
                    input_grid[y + 3][x:x + 3]]
            temp_li = [[1 if value != " " else 0 for value in element] for element in grid[:-1]]
            temp_ocr_nr = int("".join([str(element) for item in temp_li for element in item]), 2)
            result.append(ocr_dict.get(temp_ocr_nr, "?"))
        if y < len(input_grid) - 4:
            result.append(",")
    return "".join(result)


