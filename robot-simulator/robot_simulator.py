# Globals for the bearings
# Change the values as you see fit
EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2


class Robot(object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def advance(self):
        self.coordinates = list(self.coordinates)
        if self.bearing == EAST:
            self.coordinates[0] += 1
        elif self.bearing == WEST:
            self.coordinates[0] -= 1
        elif self.bearing == NORTH:
            self.coordinates[1] += 1
        elif self.bearing == SOUTH:
            self.coordinates[1] -= 1

        self.coordinates = tuple(self.coordinates)

    def turn_left(self):
        if self.bearing > 0:
            self.bearing -= 1
        else:
            self.bearing = 3

    def turn_right(self):
        if self.bearing < 3:
            self.bearing += 1
        else:
            self.bearing = 0

    def simulate(self, commands):
        A = self.advance
        R = self.turn_right
        L = self.turn_left
        for command in commands:
            eval(command + "()")

