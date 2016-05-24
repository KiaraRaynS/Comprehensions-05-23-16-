from enum import Enum


class DayOfWeek(Enum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6


def get_day_of_week(year, month, day):
    month_table = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= 1 if month < 3 else 0
    return DayOfWeek(int((year + year / 4 - year / 100 + year / 400 + month_table[month - 1] + day) % 7))
