"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""

def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1,2,3]))
print(all_unique([1,2,3,1]))
/python/001_python_basics/001_python_basics.py
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
/python/002_python_basics_2/001_python_basics_2.py
"""
Write a python program to get the Python version you are using.
"""

import sys

print(sys.version)
/python/002_python_basics_2/003_python_basics_2.py
"""
Write a python program to display the current date and time.
"""

import datetime

print(datetime.datetime.now())
/python/002_python_basics_2/002_python_basics_2.py
"""
Write a python program to display the current time.
"""

import time

print(time.ctime())
/python/002_python_basics_2/004_python_basics_2.py
"""
Write a python program to get the name of the host on which the routine is running.
"""

import socket

print(socket.gethostname())
/python/002_python_basics_2/005_python_basics_2.py
"""
Write a python program to get the name of the current module.
"""

import sys

print(sys.modules[__name__])
/python/002_python_basics_2/006_python_basics_2.py
"""
Write a python program to get the names of built-in modules.
"""

import sys

print(sys.builtin_module_names)
/python/002_python_basics_2/007_python_basics_2.py
"""
Write a python program to get the documentation of python built-in functions.
"""

import sys

print(sys.builtin_functions)
/python/002_python_basics_2/008_python_basics_2.py
"""
Write a python program to get the copyright information.
"""

import sys

print(sys.copyright)
/python/002_python_basics_2/009_python_basics_2.py
"""
Write a python program to get the command line arguments in a list.
"""

import sys

print(sys.argv)
/python/002_python_basics_2/010_python_basics_2.py
"""
Write a python program to get the size of an object in bytes.
"""

import sys

print(sys.getsizeof(1))
/python/002_python_basics_2/011_python_basics_2.py
"""
Write a python program to get the current value of the recursion limit.
"""

import sys

print(sys.getrecursionlimit())
/python/002_python_basics_2/012_python_basics_2.py
"""
Write a python program to list all the modules in the current python package.
"""

import sys

print(sys.modules)
/python/002_python_basics_2/013_python_basics_2.py
"""