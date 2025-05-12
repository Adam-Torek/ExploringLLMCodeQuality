"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""

def index_multiplication(tuple1, tuple2):
    return tuple(tuple(x * y for x, y in zip(t1, t2)) for t1, t2 in zip(tuple1, tuple2))

assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 30)) == ((6, 21), (12, 45), (2, 9), (7, 30))
/python/python_basics/python_basics_001.py
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
/python/python_basics/python_basics_004.py
"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime

print(datetime.datetime.now())
/python/python_basics/python_basics_003.py
"""
Write a Python program to get the Python version you are using.
Sample Output :
Python version :
3.4.3
"""

import sys

print("Python version :")
print(sys.version)
/python/python_basics/python_basics_002.py
"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime

print("Current date and time :")
print(datetime.datetime.now())
/python/python_basics/python_basics_005.py
"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area is :
3.8013271108436504
"""

import math

radius = float(input("Enter the radius of a circle : "))
area = math.pi * radius * radius
print("Area is :")
print(area)
/python/python_basics/python_basics_006.py
"""
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
Sample Output :
Enter your first name :
Anuj
Enter your last name :
Kumar
Name in reverse order :

"""

first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
print("Name in reverse order :")
print(last_name + " " + first_name)
/python/python_basics/python_basics_007.py
"""
Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array