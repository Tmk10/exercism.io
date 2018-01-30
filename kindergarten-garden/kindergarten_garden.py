class Garden:
    student_list = ("Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana",
                    "Joseph", "Kincaid", "Larry")

    def __init__(self, diagram, students=student_list):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)
        self.plant_dict = {"C": "Clover", "G": "Grass","R":"Radishes","V":"Violets"}


    def plants(self,student_name):
        index = self.students.index(student_name)
        student_plants = self.diagram[0][index*2:index*2 +2] + self.diagram[1][index*2:index*2 +2]
        result = [self.plant_dict.get(key) for key in student_plants]
        return result





