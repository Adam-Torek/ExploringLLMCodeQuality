"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""

def count_Occurrence(tuple, list):
    count = 0
    for i in list:
        for j in tuple:
            if i == j:
                count += 1
    return count

assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
/python/python_basics/python_basics_001.py
"""
Write a python function to print the following pattern.

*
**
***
****
*****
"""

def print_pattern():
    for i in range(1,6):
        print("*"*i)

print_pattern()
/python/python_basics/python_basics_002.py
"""
Write a python function to print the following pattern.

*****
****
***
**
*
"""

def print_pattern():
    for i in range(5,0,-1):
        print("*"*i)

print_pattern()
/python/python_basics/python_basics_003.py
"""
Write a python function to print the following pattern.

*
**
***
****
*****
****
***
**
*
"""

def print_pattern():
    for i in range(1,6):
        print("*"*i)
    for i in range(5,0,-1):
        print("*"*i)

print_pattern()
/python/python_basics/python_basics_004.py
"""
Write a python function to print the following pattern.

*
**
***
****
*****
****
***
**
*
"""

def print_pattern():
    for i in range(1,6):
        print("*"*i)
    for i in range(5,0,-1):
        print("*"*i)

print_pattern()

def print_pattern_2():
    for i in range(1,6):
        print("*"*i)
    for i in range(5,0,-1):
        print("*"*i)

print_pattern_2()
/python/python_basics/python_basics_005.py
"""
Write a python function to print the following pattern.

*
**
***
****
*****
****
***
**
*
"""

def print_pattern():
    for i in range(1,6):
        print("*"*i)
    for i in range(5,0,-1):
        print("*"*i)

print_pattern()

def print_pattern_2():
    for i in range(1,6):
        print("*"*i)
    for i in range(5,0,-1):
        print("*"*i)

print_pattern_2()

def print_pattern_3():
    for i in range(1,6):
        print("*"*i)
    for i in range(5,0,-1):
        print("*"*i)

print_pattern_3()
/python/python_basics/python_basics_006.py
"""
Write a python function to print the following pattern.

*
**
***
****
*****
****
***
**
*
"""

def print_pattern():
    for i in range(1,6):
        print("*"*i)
    for i in range(5,0,-1):
        print("*"*i)

print_pattern()

def print_pattern_2():
    for i in range(1,6):
        print("*"*i)
    for i in range(5,0,-1):
        print("*"*i)

print_pattern_2()

def print_pattern_3():
    for i in range(1,6):
        print("*"*i)
    for i in range(5,0,-1):
        print("*"*i)

print_pattern_3()

def print_pattern_4():
    for i in range(1,6):
        print("*"*i)
    for i in range(5,0,-1):
        print("*"*i)

print