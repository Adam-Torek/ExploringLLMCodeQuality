"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r','s']
"""

def extract_rear(tup):
    return [x[-1] for x in tup]

print(extract_rear(('Mers', 'for', 'Vers')))
/python_basics/001_python_basics/001_python_basics.py
"""
Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
/python_basics/003_python_basics/003_python_basics.py
"""
Write a Python program to get the Python version you are using.
"""

import sys

print(sys.version)
/python_basics/002_python_basics/002_python_basics.py
"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime

print(datetime.datetime.now())
/python_basics/004_python_basics/004_python_basics.py
"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

import math

radius = float(input("Enter radius: "))

print("Area of circle with radius {} is {}".format(radius, math.pi * radius * radius))
/python_basics/005_python_basics/005_python_basics.py
"""
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print("{} {}".format(last_name, first_name))
/python_basics/006_python_basics/006_python_basics.py
"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
"""

numbers = input("Enter comma separated numbers: ")

print(list(numbers.split(",")))
print(tuple(numbers.split(",")))
/python_basics/007_python_basics/007_python_basics.py
"""
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White","Black"]
"""

color_list = ["Red","Green","White","Black"]

print(color_list[0])
print(color_list[-1])
/python_basics/008_python_basics/008_python_basics.py
"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

exam_st_date = (11, 12, 2014)

print("The examination will start from : {} / {} / {}".format(exam_st_date[0], exam_st_date[1], exam_st_date[2]))
/python_basics/009_python_basics/009_python_basics.py
"""
Write a Python program that accepts an