"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""

def check_type(tup):
    return all(type(tup[0]) == type(i) for i in tup)

print(check_type((5, 6, 7, 3, 5, 6)))
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
print(os.sys.platform)
print(os.sys.release())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a Python program to get the current date.
"""

import datetime

print(datetime.date.today())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a Python program to convert seconds to day, hour, minutes and seconds.
"""

import datetime

seconds = 1000000000

print(datetime.timedelta(seconds=seconds))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a Python program to get the current time in microseconds.
"""

import time

print(time.time())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a Python program to get the current time in milliseconds.
"""

import time

print(time.time() * 1000)
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_9.py
"""
Write a Python program to get the current time in seconds.
"""

import time

print(time.time())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_10.py
"""
Write a Python program to get the current time in milliseconds.
"""

import time

print(time.time() * 1000)
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_11.py
"""
Write a Python program to get the current time in seconds.
"""

import time

print(time.time())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_12.py
"""
Write a Python program to get the current time in milliseconds.
"""

import time

print(time.time() * 1000)
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_13.py
"""
Write a Python program to get the current time in seconds.
"""

import time

print(time.time())
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_14.py
"""
Write a Python program to get the current time in milliseconds.
"""

import time

print(time.time() * 1000)
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_15.py
"""
Write a Python program to get the current time in seconds.
"""

import time

print(time