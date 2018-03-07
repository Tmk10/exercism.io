class Queen(object):
    def __init__(self, row, column):
        self.wq = (row, column)
        self.check_values()

    def __getitem__(self, item):
        return self.wq[item]

    def check_values(self):
        if not all([True if coordinate >= 0 and coordinate < 8 else False for coordinate in self.wq]):
            raise ValueError("Wrong coordinates")

    def board(self, another_queen):
        board = [["_" for y in range(8)] for x in range(8)]
        board[wq[0]][wq[1]] = "W"
        board[another_queen[0]][another_queen[1]] = "B"
        return ["".join(element) for element in board]

    def can_attack(self, another_queen):
        if another_queen.wq == self.wq:
            raise ValueError("Queens on the same position")
        row_dst = abs(self.wq[0] - another_queen[0])
        col_dst = abs(self.wq[1] - another_queen[1])
        if self.wq[0] == another_queen[0] or self.wq[1] == another_queen[1] or row_dst == col_dst:
            return True
        return False





