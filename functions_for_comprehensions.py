

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


def average_wave_by_day():
    from statistics import mean
    import datetime
    water_data = read_water_data()
    dates = [item[5] for item in water_data]
    dates_list = []
    for date in dates:
        date = date.replace('\n', '')
        dates_list.append(date)
    heights_list = [item[1] for item in water_data]
    dates_heights = {date: heights_list[index] for index, date in enumerate(dates_list)}
    monday_heights = []
    tuesday_heights = []
    wednesday_heights = []
    thursday_heights = []
    friday_heights = []
    saturday_heights = []
    sunday_heights = []
    for key, value in dates_heights.items():
        key_day = datetime.datetime.strptime(key, "%Y-%m-%d")
        key_day = key_day.isoweekday()
        if key_day == 1:
            monday_heights.append(float(value))
        if key_day == 2:
            tuesday_heights.append(float(value))
        if key_day == 3:
            wednesday_heights.append(float(value))
        if key_day == 4:
            thursday_heights.append(float(value))
        if key_day == 5:
            friday_heights.append(float(value))
        if key_day == 6:
            saturday_heights.append(float(value))
        if key_day == 7:
            sunday_heights.append(float(value))
    a_mon = sum(monday_heights)/len(monday_heights)
    a_tue = sum(tuesday_heights)/len(tuesday_heights)
    a_wed = sum(wednesday_heights)/len(wednesday_heights)
    a_thu = sum(thursday_heights)/len(thursday_heights)
    a_fri = sum(friday_heights)/len(friday_heights)
    a_sat = sum(saturday_heights)/len(saturday_heights)
    a_sun = sum(sunday_heights)/len(sunday_heights)
    averages_by_day = [a_mon, a_tue, a_wed, a_thu, a_fri, a_sat, a_sun]
    weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    last_dictionairy = {day: averages_by_day[index] for index, day in enumerate(weekday_names)}
    print(averages_by_day)
    print(weekday_names)
    print(last_dictionairy)


def nested_comprehension():
    from statistics import mean
    homework_1 = []
    homework_dict = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                     'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                     'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                     'River': {'Homework 1': 85, 'Homework 2': 91},
                     }
#    homework_grades = [value[1] for value in homework_dict.items()]
    for key, value in homework_dict.items():
        homework_1.append(value['Homework 1'])
    average = sum(homework_1)/len(homework_1)
    return(average)
