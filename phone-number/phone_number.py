import re


class Phone:
    def __init__(self, number):
        phone_pattern = re.compile(r"^\W?([\d]{1})?\s*.?([2-9]{1}\d{2})\W?\s*([2-9]{1}\d{2})\W?\s*(\d{4})\s*$")
        if phone_pattern.match(number) is None:
            raise ValueError("Incorrect number")
        if phone_pattern.match(number).groups()[0] not in ("1",None):
            raise ValueError("Incorrect number")
        else:
            self.result = phone_pattern.match(number).groups()[1:]
            self.number = "".join(self.result)
            self.area_code = self.result[0]

    def pretty(self):
        return "({}) {}-{}".format(self.result[0], self.result[1], self.result[2])

