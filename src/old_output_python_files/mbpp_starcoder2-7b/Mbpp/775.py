"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""

def odd_position(lst):
    for i in range(1,len(lst),2):
        if lst[i]%2 == 0:
            return False
    return True

print(odd_position([2,1,4,3,6,7,6,3]))
<file_sep>/python_basics/01_python_basics/01_python_basics.py
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
<file_sep>/python_basics/02_python_basics/02_python_basics.py
"""
Write a python program to get the Python version you are using.
"""

import sys

print(sys.version)
<file_sep>/python_basics/03_python_basics/03_python_basics.py
"""
Write a python program to display the current date and time.
"""

import datetime

print(datetime.datetime.now())
<file_sep>/python_basics/04_python_basics/04_python_basics.py
"""
Write a python program which accepts the radius of a circle from the user and compute the area.
"""

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
print(area)
<file_sep>/python_basics/05_python_basics/05_python_basics.py
"""
Write a python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)
<file_sep>/python_basics/06_python_basics/06_python_basics.py
"""
Write a python program which accepts an integer (n) and computes the value of n+nn+nnn.
"""

n = int(input("Enter an integer: "))
print(n + (n*11) + (n*111))
<file_sep>/python_basics/07_python_basics/07_python_basics.py
"""
Write a python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
"""

def difference(n):
    if n > 17:
        return (n - 17) * 2
    else:
        return 17 - n

print(difference(20))
<file_sep>/python_basics/08_python_basics/08_python_basics.py
"""
Write a python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
"""

def sum_three(a,b,c):
    if a == b == c:
        return (a + b + c) * 3
    else:
        return a + b + c

print(sum_three(1,2,3))
<file_sep>/python_basics/09_python_basics/09_python_basics.py
"""
Write a python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
"""

def new_string(string):
    if string[:2] == "Is":
        return string
    else:
        return "Is" + string

print(new_string("Is"))
<file_sep>/python_basics/10_python_basics/10_python_basics.py
"""
Write a python program to get a string which is n (non-negative integer) copies of a given string.
"""

def string_copies(string,n):
    return string * n

print(string_copies("abc