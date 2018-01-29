class BowlingGame(object):
    def __init__(self):
        self.total_score = 0
        self.frame_table = [[] for _ in range(0, 10)]
        self.rolls = []
        self.frame = 1
        self.status = True

    def strike_or_spare(self, frame):
        if len(frame) == 1:
            return "strike"
        elif len(frame) == 2 and sum(frame) == 10:
            return "spare"

    def roll(self, pins):
        if not self.status:
            if sum(self.frame_table[self.frame -2]) == 10:
                self.frame_table.extend([pins])
            else:
                return "Game Over"
        if self.status == True:
            if pins < 0 or pins > 10:
                raise ValueError("Wrong number of pins")
            else:
                self.rolls.append(pins)
                self.frame_table[self.frame - 1].append(pins)
                if sum(self.frame_table[self.frame - 1]) == 10 or len(self.frame_table[self.frame - 1]) == 2:
                    if sum(self.frame_table[self.frame - 1]) > 10:
                        raise ValueError("To many points in frame")
                    self.frame += 1

            if self.frame == 11:
                self.status = False
        else:
            return "Game Over"

    def score(self):
        if self.status == False:
            for frame in self.frame_table:
                if self.strike_or_spare(frame) == "strike":
                    self.total_score += self.rolls[0] + self.rolls[1] + self.rolls[2]
                    self.rolls = self.rolls[1:]

                elif self.strike_or_spare(frame) == "spare":
                    self.total_score += self.rolls[0] + self.rolls[1] + self.rolls[2]
                    self.rolls = self.rolls[2:]
                else:
                    self.total_score += self.rolls[0] + self.rolls[1]
                    self.rolls = self.rolls[2:]
            return self.total_score
        return "Game not ended yet"


a = BowlingGame()
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(0)
a.roll(10)
a.roll(10)
a.roll(10)
print(a.score())
print(a.frame_table)
print(a.frame_table[11])