class School(object):
    def __init__(self, name):
        self.name = name
        self.__rank = [(i, []) for i in range(1, 9)]

    @property
    def rank(self):
        return self.__rank

    def grade(self, grade):
        return tuple(self.rank[grade - 1][1])

    def add(self, student, grade):
        self.rank[grade - 1][1].append(student)

    def sort(self):
        result = [(item[0], tuple(sorted(item[1]))) for item in self.__rank if item[1]]
        result.sort()
        return result



