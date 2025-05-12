"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""

def Diff(li1, li2):
    return [x for x in li1 if x not in li2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a python program to print the following string in a specific format (see the output).
"""

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a python program to get the Python version you are using.
"""

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a python program to display the current date and time.
"""

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a python program which accepts the radius of a circle from the user and compute the area.
"""

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a python program which takes two inputs from user and print them addition.
"""

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

sum = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a python program which takes two inputs from user and print them addition.
"""

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

sum = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a python program to display the first and last colors from the following list.
color_list = ["Red","Green","White","Black"]
"""

color_list = ["Red","Green","White","Black"]
print(color_list[0], color_list[-1])
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_9.py
"""
Write a python program to get the Python version you are using.
"""

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_10.