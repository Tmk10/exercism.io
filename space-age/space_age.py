def round_decorator(f):
    def wrap(arg):
        x = round(f(arg), 2)
        return x

    return wrap


class SpaceAge:
    def __init__(self, seconds):
        self.__seconds = seconds
        self.__earth_year = 31557600
        self.__earth_time = seconds / 31557600

    def __call__(self, value):
        return value

    @property
    def seconds(self):
        return self.__seconds

    @round_decorator
    def on_earth(self):
        return self.__earth_time

    @round_decorator
    def on_mercury(self):
        return self.__earth_time / 0.2408467

    @round_decorator
    def on_venus(self):
        return self.__earth_time / 0.61519726

    @round_decorator
    def on_mars(self):
        return self.__earth_time / 1.8808158

    @round_decorator
    def on_jupiter(self):
        return self.__earth_time / 11.862615

    @round_decorator
    def on_saturn(self):
        return self.__earth_time / 29.447498

    @round_decorator
    def on_uranus(self):
        return self.__earth_time / 84.016846

    @round_decorator
    def on_neptune(self):
        return self.__earth_time / 164.79132


