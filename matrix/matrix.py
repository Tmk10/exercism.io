class Matrix(object):


    def __init__(self, matrix_string):
        self.matrix = [[int(x) for x in element.split(" ") if x.isdigit()] for element in matrix_string.splitlines()]
        self.rows = self.matrix
        self.columns = [list(x) for x in zip(*self.matrix)]

