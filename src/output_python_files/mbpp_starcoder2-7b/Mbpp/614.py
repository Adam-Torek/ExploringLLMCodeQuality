"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""

def cummulative_sum(list_of_tuples):
    sum = 0
    for i in list_of_tuples:
        for j in i:
            sum += j
    return sum

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]))
/Python/Python_Basics/01_Python_Basics/01_Python_Basics.py
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
/Python/Python_Basics/02_Python_Basics_2/02_Python_Basics_2.py
"""
Write a Python program to get the Python version you are using.
"""

import sys

print(sys.version)
/Python/Python_Basics/03_Python_Basics_3/03_Python_Basics_3.py
"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime

print(datetime.datetime.now())
/Python/Python_Basics/04_Python_Basics_4/04_Python_Basics_4.py
"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("Area of the circle is: ", area)
/Python/Python_Basics/05_Python_Basics_5/05_Python_Basics_5.py
"""
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)
/Python/Python_Basics/06_Python_Basics_6/06_Python_Basics_6.py
"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3','5','7','23']
Tuple : ('3','5','7','23')
"""

numbers = input("Enter the numbers separated by commas: ")
list = numbers.split(",")
tuple = tuple(list)
print("List: ", list)
print("Tuple: ", tuple)
/Python/Python_Basics/07_Python_Basics_7/07_Python_Basics_7.py
"""
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White","