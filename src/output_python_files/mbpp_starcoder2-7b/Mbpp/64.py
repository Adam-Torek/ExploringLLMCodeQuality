"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""

def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1])

print(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))
/python_basics/01_python_basics/01_python_basics.py
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
/python_basics/03_python_basics/03_python_basics.py
"""
Write a Python program to get the Python version you are using.
"""

import sys

print(sys.version)
/python_basics/02_python_basics/02_python_basics.py
"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime

print(datetime.datetime.now())
/python_basics/04_python_basics/04_python_basics.py
"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

import math

radius = float(input("Enter the radius of the circle: "))

print("Area of the circle is: ", math.pi * radius * radius)
/python_basics/05_python_basics/05_python_basics.py
"""
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(last_name + " " + first_name)
/python_basics/06_python_basics/06_python_basics.py
"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
"""

numbers = input("Enter comma separated numbers: ")

list = numbers.split(",")
tuple = tuple(list)

print("List: ", list)
print("Tuple: ", tuple)
/python_basics/07_python_basics/07_python_basics.py
"""
Write a Python program to accept a filename from the user and print the extension of that.
"""

filename = input("Enter the filename: ")

print("Extension of the file is: ", filename.split(".")[-1])
/python_basics/08_python_basics/08_python_basics.py
"""
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White","Black"]
"""

color_list = ["Red","Green","White","Black"]

print("First color: ", color_list[0])
print("Last color: ", color_list[-1])
/python_basics/09_python_basics/09_python_basics.py
"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date