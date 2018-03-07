from copy import deepcopy
def value_check(li):
    if li:
        length = len(li[0])
    for element in li:
        if len(element) != length:
            raise ValueError("Wrong dimensions of list")
        for item in element:
            if item != " " and item != "*" and item != '"':
                raise ValueError("Invalid character in list")

def count_mines(mines, board):
    cycle = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    for coordinate in mines:
        for item in cycle:
            x, y = coordinate[0] - item[0], coordinate[1] - item[1]
            try:
                if x >= 0 and y >= 0 and board[x][y] != "*":
                    if board[x][y] == " ":
                        board[x][y] = 0
                    board[x][y] += 1
            except IndexError:
                continue
    return board

def board(input_board_array):
    value_check(input_board_array)
    mines = []
    board = [[item if item == "*" else " " for item in element] for element in input_board_array]
    temp_board = deepcopy(board)
    for row in temp_board:
        for element in row:
            if element == "*":
                mines.append((temp_board.index(row), row.index(element)))
                temp_board[temp_board.index(row)][row.index(element)] = "+"
    if mines:
        return ["".join(str(x) for x in element) for element in count_mines(mines, board)]
    return ["".join(str(x) for x in element) for element in board]










