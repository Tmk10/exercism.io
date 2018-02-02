class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")[::-1]

    def is_valid(self):
        if self.card_num.isdigit() and len(self.card_num) > 1:
            a= divmod(sum([int(number) if not index % 2 else  int(number) * 2 if (int(number) * 2) < 9 else (int(number) * 2) - 9 for index, number in
                    enumerate(self.card_num)]),10)[1]

            return not bool(a)
        return False

