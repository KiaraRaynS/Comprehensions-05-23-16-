

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


def average_grades():
    complete_dict = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                        'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                        'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                        'River': {'Homework 1': 85, 'Homework 2': 91}
    }

