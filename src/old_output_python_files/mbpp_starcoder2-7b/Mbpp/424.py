"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r','s']
"""

def extract_rear(tup):
    return [x[-1] for x in tup]

print(extract_rear(('Mers', 'for', 'Vers')))
<file_sep>/python/00001_python_basics/00001_python_basics.py
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
<file_sep>/python/00002_python_basics_2/00002_python_basics_2.py
"""
Write a Python program to get the Python version you are using.
"""

import sys

print(sys.version)
<file_sep>/python/00003_python_basics_3/00003_python_basics_3.py
"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime

print(datetime.datetime.now())
<file_sep>/python/00004_python_basics_4/00004_python_basics_4.py
"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

import math

r = float(input("Enter radius: "))

print("Area = " + str(math.pi * r * r))
<file_sep>/python/00005_python_basics_5/00005_python_basics_5.py
"""
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(last_name + " " + first_name)
<file_sep>/python/00006_python_basics_6/00006_python_basics_6.py
"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3','5','7','23']
Tuple : ('3','5','7','23')
"""

numbers = input("Enter comma-separated numbers: ")

print("List: " + str(numbers.split(",")))
print("Tuple: " + str(tuple(numbers.split(","))))
<file_sep>/python/00007_python_basics_7/00007_python_basics_7.py
"""
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White","Black"]
"""

color_list = ["Red","Green","White","Black"]

print(color_list[0] + " " + color_list[-1])
<file_sep>/python/00008_python_basics_8/00008_python_basics_8.py
"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_