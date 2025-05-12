"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""

def wind_chill(wind_velocity, temperature):
    if wind_velocity < 1 or temperature < -58 or temperature > 41:
        return "Invalid input"
    else:
        return round(13.12 + 0.6215 * temperature - 11.37 * wind_velocity ** 0.16 + 0.3965 * temperature * wind_velocity ** 0.16)

print(wind_chill(120,35))
/python/python_basics/01_variables/01_variables.py
"""
Create a variable called name and assign your name to it.
"""

name = ""

print(name)
/python/python_basics/02_data_types/02_data_types.py
"""
Create a variable called age and assign your age to it.
"""

age = 23

print(age)
/python/python_basics/03_operators/03_operators.py
"""
Create a variable called x and assign it the value of 10.
Create a variable called y and assign it the value of 5.
Create a variable called z and assign it the value of x + y.
"""

x = 10
y = 5
z = x + y

print(z)
/python/python_basics/04_functions/04_functions.py
"""
Write a function that takes a number as an argument and returns the square of that number.
assert square(5)==25
"""

def square(number):
    return number ** 2

print(square(5))
/python/python_basics/05_conditionals/05_conditionals.py
"""
Write a function that takes a number as an argument and returns whether the number is even or odd.
assert even_or_odd(5)=="odd"
"""

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

print(even_or_odd(5))
/python/python_basics/06_lists/06_lists.py
"""
Create a list called numbers and assign the values 1, 2, 3, 4, 5 to it.
"""

numbers = [1, 2, 3, 4, 5]

print(numbers)
/python/python_basics/07_loops/07_loops.py
"""
Write a function that takes a list of numbers as an argument and returns the sum of all the numbers in the list.
assert sum_of_numbers([1,2,3,4,5])==15
"""

def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_of_numbers([1,2,3,4,5]))
/python/python_basics/08_dictionaries/08_dictionaries.py
"""
Create a dictionary called person and assign the values "", 23, "male" to it.
"""

person = {
    "name": "",
    "age": 23,
    "gender": "male"
}

print(person)
/python/python_basics/09_classes/09_classes.py
"""
Create a class called Person with the attributes name, age and gender.
"""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person = Person("", 23, "male")

print(person)
/python/python_basics/04_functions/04_functions_2.py
"""
Write a function that takes a list of numbers as an argument and returns the average of all the numbers in the list.
assert average([1,2,3,4,5])==3
"""

def average(numbers):
    total = 0
    for number in numbers:
        total += number