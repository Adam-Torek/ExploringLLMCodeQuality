"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""

def mul_even_odd(lst):
    even_list = []
    odd_list = []
    for i in lst:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list[0]*odd_list[0]

print(mul_even_odd([1,3,5,7,4,1,6,8]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a Python program to get the Python version you are using.
"""

import sys

print(sys.version)
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a Python program to display the current date and time.
"""

import datetime

print(datetime.datetime.now())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a Python program to get the current username.
"""

import getpass

print(getpass.getuser())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a Python program to get OS name, platform and release information.
"""

import os

print(os.name)
print(os.uname())
print(os.getlogin())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a Python program to get the current machine local time.
"""

import time

print(time.localtime())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a Python program to get the name of the machine on which the Python interpreter is executing.
"""

import platform

print(platform.node())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a Python program to get the names and versions of the Python modules installed on the system.
"""

import sys

print(sys.modules)
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a Python program to get the system time.
"""

import time

print(time.time())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_9.py
"""
Write a Python program to get the system time.
"""

import time

print(time.ctime())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_10.py
"""
Write a Python program to get the current date.
"""

import datetime

print(datetime.date.today())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_11.py
"""
Write a Python program to get the current time.
"""

import datetime

print(datetime.datetime.now().time())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_12.py
"""
Write a Python program to convert a string to a list.
"""

def string_to_list(string):
    return list(string)

print(string_to_list("Hello World"))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_13.py
"""
Write a Python program to remove the characters which have odd index values of a given string.
"""

def remove_odd_index(string):
    return string[::2]

print(remove_odd_index("Hello World"))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_14.py
"""
Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
"""

def exchange_first_last(string):
    return string[-1]+string[1:-1]+string[0]

print(exchange_first_last("Hello World"))
/Python/Python_Basics/Python_Basics_1