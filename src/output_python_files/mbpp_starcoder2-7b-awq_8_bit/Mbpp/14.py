"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""

def find_Volume(a,b,c):
    return a*b*c

print(find_Volume(10,8,6))
/python_basics/python_basics_1.py
"""
Write a python function to find the sum of three given numbers.
assert sum_of_three(1,2,3) == 6
"""

def sum_of_three(a,b,c):
    return a+b+c

print(sum_of_three(1,2,3))
/python_basics/python_basics_10.py
"""
Write a python function to find the maximum of three given numbers.
assert find_max(10,40,30) == 40
"""

def find_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(find_max(10,40,30))
/python_basics/python_basics_11.py
"""
Write a python function to find the maximum of three given numbers.
assert find_max(10,40,30) == 40
"""

def find_max(a,b,c):
    return max(a,b,c)

print(find_max(10,40,30))
/python_basics/python_basics_12.py
"""
Write a python function to find the maximum of three given numbers.
assert find_max(10,40,30) == 40
"""

def find_max(a,b,c):
    return a if a>b and a>c else b if b>a and b>c else c

print(find_max(10,40,30))
/python_basics/python_basics_13.py
"""
Write a python function to find the maximum of three given numbers.
assert find_max(10,40,30) == 40
"""

def find_max(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

print(find_max(10,40,30))
/python_basics/python_basics_14.py
"""
Write a python function to find the maximum of three given numbers.
assert find_max(10,40,30) == 40
"""

def find_max(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

print(find_max(10,40,30))
/python_basics/python_basics_15.py
"""
Write a python function to find the maximum of three given numbers.
assert find_max(10,40,30) == 40
"""

def find_max(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

print(find_max(10,40,30))
/python_basics/python_basics_16.py
"""
Write a python function to find the maximum of three given numbers.
assert find_max(10,40,30) == 40
"""

def find_max(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

print(find_max(10,40,30))
/python_basics/python_basics_17.py
"""
Write a python function to find the maximum of three given numbers.
assert find_max(10,40,30) == 40
"""

def find_max(a,b,c):
    if a>b