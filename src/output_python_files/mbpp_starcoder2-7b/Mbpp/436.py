"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""

def neg_nos(nums):
    return [num for num in nums if num < 0]

print(neg_nos([-1,4,5,-6]))
<file_sep>/python/python_basics/01_python_basics/01_python_basics.py
"""
Write a python program to print the following string in a specific format (see the output).

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky.

Twinkle, twinkle, little star, 
	How I wonder what you are
"""

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.")
<file_sep>/python/python_basics/02_python_basics/02_python_basics.py
"""
Write a python program to get the Python version you are using.
"""

import sys

print(sys.version)
<file_sep>/python/python_basics/03_python_basics/03_python_basics.py
"""
Write a python program to display the current date and time.
"""

import datetime

print(datetime.datetime.now())
<file_sep>/python/python_basics/04_python_basics/04_python_basics.py
"""
Write a python program which accepts the radius of a circle from the user and compute the area.
"""

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius * radius

print("Area of the circle is: ", area)
<file_sep>/python/python_basics/05_python_basics/05_python_basics.py
"""
Write a python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(last_name + " " + first_name)
<file_sep>/python/python_basics/06_python_basics/06_python_basics.py
"""
Write a python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
"""

nums = input("Enter the numbers separated by comma: ")

list = nums.split(",")
tuple = tuple(list)

print("List: ", list)
print("Tuple: ", tuple)
<file_sep>/python/python_basics/07_python_basics/07_python_basics.py
"""
Write a python program which takes two inputs from user and print them addition.
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Addition of the two numbers is: ", num1 + num2)
<file_sep>/python/python_basics/08_python_basics/08_python_basics.py
"""
Write a python program to display the first and last colors from the following list.

color_list = ["Red","Green","White","Black"]
"""

color_list = ["Red","Green","White","Black"]

print("First color: ", color_list[0])
print("Last color: ", color_list[-1])
<file_sep>/python/python_basics/09_python_basics/09_python_basics.py
"""
Write a python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)
"""

exam_st_date = (11, 12, 2014)

print("The examination will start from: %i / %i / %i" %exam_st_date)
<file_sep>/python/python_basics/10_python_basics/10_python_basics.py
"""
Write a python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""

n = int(input("Enter the number: "))

print("The value of n