from datetime import date, datetime
from calendar import monthrange


def meetup_day(year, month, day_of_the_week, which):
    day_to_number_dict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5,
                          "Sunday": 6}

    if which == "1st":
        day = 1
        default_date = date(year, month, day)
        while day_to_number_dict[day_of_the_week] != default_date.weekday():
            day += 1
            default_date = date(year, month, day)
        return default_date
    elif which == "2nd":
        day = 8
        default_date = date(year, month, day)
        while day_to_number_dict[day_of_the_week] != default_date.weekday():
            day += 1
            default_date = date(year, month, day)
        return default_date
    elif which == "3rd":
        day = 15
        default_date = date(year, month, day)
        while day_to_number_dict[day_of_the_week] != default_date.weekday():
            day += 1
            default_date = date(year, month, day)
        return default_date

    elif which == "teenth":
        day = 13
        default_date = date(year, month, 13)
        while day_to_number_dict[day_of_the_week] != default_date.weekday():
            day += 1
            default_date = date(year, month, day)
        return default_date

    elif which == "4th":
        day = 22
        default_date = date(year, month, day)
        while day_to_number_dict[day_of_the_week] != default_date.weekday():
            day += 1
            default_date = date(year, month, day)
        return default_date

    elif which == "5th":
        day = 29
        default_date = date(year, month, day)
        while day_to_number_dict[day_of_the_week] != default_date.weekday():
            day += 1
            default_date = date(year, month, day)
        return default_date

    elif which == "last":
        day = monthrange(year, month)[1]
        default_date = date(year, month, day)
        while day_to_number_dict[day_of_the_week] != default_date.weekday():
            day -= 1
            default_date = date(year, month, day)
        return default_date


# Ugly but working
