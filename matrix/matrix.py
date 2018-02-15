class Matrix(object):

    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")
        self.matrix = [item.split(" ") for item in self.matrix]
        self.matrix = [[int(x) for x in element if x.isdigit()] for element in self.matrix]
        self.rows = self.matrix
        self.columns = [list(x) for x in zip(*self.matrix)]



