"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""

def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True

assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([2,1,4,3,6,7,6,4]) == False
/python/list_comprehension.py
"""
Write a python function to create a list of numbers from 1 to 100 using list comprehension.
"""

def list_comprehension():
    return [i for i in range(1, 101)]

print(list_comprehension())
/python/list_comprehension_2.py
"""
Write a python function to create a list of numbers from 1 to 100 using list comprehension.
"""

def list_comprehension():
    return [i for i in range(1, 101) if i % 2 == 0]

print(list_comprehension())
/python/list_comprehension_3.py
"""
Write a python function to create a list of numbers from 1 to 100 using list comprehension.
"""

def list_comprehension():
    return [i for i in range(1, 101) if i % 2!= 0]

print(list_comprehension())
/python/list_comprehension_4.py
"""
Write a python function to create a list of numbers from 1 to 100 using list comprehension.
"""

def list_comprehension():
    return [i for i in range(1, 101) if i % 2 == 0 and i % 3 == 0]

print(list_comprehension())
/python/list_comprehension_5.py
"""
Write a python function to create a list of numbers from 1 to 100 using list comprehension.
"""

def list_comprehension():
    return [i for i in range(1, 101) if i % 2!= 0 and i % 3 == 0]

print(list_comprehension())
/python/list_comprehension_6.py
"""
Write a python function to create a list of numbers from 1 to 100 using list comprehension.
"""

def list_comprehension():
    return [i for i in range(1, 101) if i % 2 == 0 and i % 3!= 0]

print(list_comprehension())
/python/list_comprehension_7.py
"""
Write a python function to create a list of numbers from 1 to 100 using list comprehension.
"""

def list_comprehension():
    return [i for i in range(1, 101) if i % 2!= 0 and i % 3!= 0]

print(list_comprehension())
/python/list_comprehension_8.py
"""
Write a python function to create a list of numbers from 1 to 100 using list comprehension.
"""

def list_comprehension():
    return [i for i in range(1, 101) if i % 2 == 0 or i % 3 == 0]

print(list_comprehension())
/python/list_comprehension_9.py
"""
Write a python function to create a list of numbers from 1 to 100 using list comprehension.
"""

def list_comprehension():
    return [i for i in range(1, 101) if i % 2!= 0 or i % 3 == 0]

print(list_