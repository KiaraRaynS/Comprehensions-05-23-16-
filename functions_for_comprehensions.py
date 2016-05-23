

def read_water_data():
    with open("water_data.txt") as opened_file:
        water_data = opened_file.readlines()
        return [list.split(',') for list in water_data]


def remove_vowels():
    letter_list = list("List Comprehensions are the Greatest!")
    end_list = [letter for letter in letter_list if letter not in ('a', 'e', 'i', 'o', 'u')]
    print(end_list)


def temp_string_to_float():
    water_data = read_water_data()
    water_temps = [item[4] for item in water_data]
    water_temps = ' '.join(water_temps)
    for item in water_temps:
        item = float(item)
    water_temps_float = [item for item in water_temps]
    print(water_temps)

temp_string_to_float()


def water_temperatures():
    water_data = read_water_data()
    water_temps = [item[4] for item in water_data]
    fahrenheit_temperature = [temp for temp in water_temps]
    print(fahrenheit_temperature)


water_temperatures()


def water_dates_height_dictionairy():
    water_data = read_water_data()
    dates = []
    height = []
    dates_height_dict = {}

