from random import randint as ri
from string import ascii_uppercase


class Robot(object):
    __name_list = []

    def __init__(self):
        self.name = self.__generate_name()
        Robot.__name_list.append(self.name)

    def __generate_name(self):
        while True:
            value = "{1}{2}{0}".format(str(ri(100, 999)), chr(ri(65, 90)), chr(ri(65, 90)))
            if value not in Robot.__name_list:
                return value

    def reset(self):
        self.__init__()


