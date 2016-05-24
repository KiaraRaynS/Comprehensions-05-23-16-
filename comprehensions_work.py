from functions_for_comprehensions import remove_vowels
from functions_for_comprehensions import temp_string_to_float
from functions_for_comprehensions import water_temperatures
from functions_for_comprehensions import water_dates_height_dictionairy
from functions_for_comprehensions import nested_comprehension
from functions_for_comprehensions import average_wave_by_day

print('"List Comprehensions are the Greatest!" Now without Vowels.')
remove_vowels()

print("-------------------------------")
print("Water temperatures as floats: ")
temp_string_to_float()

print('-----------------------------------')
print("Water temperatures in Fahrenheit: ")
water_temperatures()

print('---------------------------------------')
print("Dictionairy of wave heights by dates: ")
water_dates_height_dictionairy()

print('----------------------------------------')
print("Average wave height by day: ")
average_wave_by_day()

print('---------------------------------------')
print("Average Homework 1 grades")
grades = nested_comprehension()

print(grades)
