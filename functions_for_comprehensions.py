

def read_water_data():
    with open("water_data.txt") as opened_file:
        water_data = opened_file
        return water_data


def remove_vowels():
    letter_list = list("List Comprehensions are the Greatest!")
    end_list = [for letter in letter_list if letter != ('a', 'e', 'i', 'o', 'u')]
    print(end_list)


def temp_string_to_float():
    water_data = read_water_data()


def water_temperatures():
    water_data = read_water_data()
    fahrenheit_temperature = [temperature * 32 + 32 for temperature in water_data if index[4::5]]
    print(fahrenheit_temprature)


def water_dates_height_dictionairy():
    water_data = read_water_data()

