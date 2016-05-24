from enum import Enum


def read_water_data():
    with open("water_data.txt") as opened_file:
        water_data = opened_file.readlines()
        return [list.split(',') for list in water_data]


def remove_vowels():
    letter_list = list("List Comprehensions are the Greatest!")
    end_list = [letter for letter in letter_list if letter not in ('a', 'e', 'i', 'o', 'u')]
    print(end_list)


def temp_string_to_float():
    floated_temps = []
    water_data = read_water_data()
    water_temps = [item[4] for item in water_data]
    for item in water_temps:
        item = float(item)
        floated_temps.append(item)

    print(floated_temps)


def water_temperatures():
    water_data = read_water_data()
    water_temps = [item[4] for item in water_data]
    floated_temps = []
    for item in water_temps:
        item = float(item)
        floated_temps.append(item)
    fahrenheit_temperature = [temp * 1.8 + 32 for temp in floated_temps]
    print(fahrenheit_temperature)


def water_dates_height_dictionairy():
    water_data = read_water_data()
    dates_list = [item[5] for item in water_data]
    dates = []
    for date in dates_list:
        date = date.replace('\n', '')
        dates.append(date)
    height = [item[1] for item in water_data]
    dates_height_dict = {date: height[index] for index, date in enumerate(dates)}
    print(dates_height_dict)


def get_day_of_week(year, month, day):
    from enum import Enum
    class DayOfWeek(Enum):
        Sunday = 0
        Monday = 1
        Tuesday = 2
        Wednesday = 3
        Thursday = 4
        Friday = 5
        Saturday = 6
    month_table = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= 1 if month < 3 else 0
    return DayOfWeek(int((year + year / 4 - year / 100 + year / 400 + month_table[month - 1] + day) % 7))


def average_height():
    water_data = read_water_data()
    dates_list = [item[5] for item in water_data]
    heights_list = [item[1] for item in water_data]
    day_list = [item[8:10] for item in dates_list]
    days = []
    for day in day_list:
        day = int(day)
        days.append(day)
    days_heights = {day: heights_list[index] for index, day in enumerate(days)}
    for day in days_heights.keys():
        monday_heights = []
        tuesday_heights = []
        wednesday_heights = []
        thursday_heights = []
        friday_heights = []
        saturday_heights = []
        sunday_heights = []
        years = 2015
        months = 8
        thanks_joel = get_day_of_week(years, months, day)
        if thanks_joel == DayOfWeek.Monday:
            monday_heights.append(days)
        if thanks_joel == DayOfWeek.Tuesday:
            tuesday_heights.append(days)
        if thanks_joel == DayOfWeek.Wednesday:
            wednesday_heights.append(days)
        if thanks_joel == DayOfWeek.Thursday:
            thursday_heights.append(days_heights.values())
        if thanks_joel == DayOfWeek.Friday:
            friday_heights.append(days_heights.values())
        if thanks_joel == DayOfWeek.Saturday:
            saturday_heights.append(days_heights.values())
        if thanks_joel == DayOfWeek.Sunday:
            sunday_heights.append(days_heights.values())
    print(sunday_heights)


def nested_comprehension():
    homework_dict = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                     'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                     'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                     'River': {'Homework 1': 85, 'Homework 2': 91}
                     }
    homework_1_grades = for key in homework_dict.keys():

