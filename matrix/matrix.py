class Matrix(object):


    def __init__(self, matrix_string):
        self.matrix = [[int(x) for x in element.split(" ") if x.isdigit()] for element in matrix_string.splitlines()]
        self.rows = self.matrix
        self.columns = [list(x) for x in zip(*self.matrix)]



"""self.matrix = matrix_string.split("\n")
        self.matrix = [item.split(" ") for item in self.matrix]"""

a= Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
print(a.matrix)