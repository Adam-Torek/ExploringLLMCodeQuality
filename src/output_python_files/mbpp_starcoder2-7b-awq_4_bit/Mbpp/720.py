"""
Write a function to add a dictionary to the tuple. The output should be a tuple.
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""

def add_dict_to_tuple(tup, dict):
    return tup + (dict,)

print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ))
/python_basics/python_basics_1.py
"""
Write a function to find the maximum of three numbers.
assert find_max(1, 2, 3) == 3
assert find_max(3, 2, 1) == 3
assert find_max(1, 1, 1) == 1
"""

def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(find_max(1, 2, 3))
print(find_max(3, 2, 1))
print(find_max(1, 1, 1))
/python_basics/python_basics_10.py
"""
Write a function to find the maximum of three numbers.
assert find_max(1, 2, 3) == 3
assert find_max(3, 2, 1) == 3
assert find_max(1, 1, 1) == 1
"""

def find_max(a, b, c):
    return max(a, b, c)

print(find_max(1, 2, 3))
print(find_max(3, 2, 1))
print(find_max(1, 1, 1))
/python_basics/python_basics_11.py
"""
Write a function to find the maximum of three numbers.
assert find_max(1, 2, 3) == 3
assert find_max(3, 2, 1) == 3
assert find_max(1, 1, 1) == 1
"""

def find_max(a, b, c):
    return max(a, b, c)

print(find_max(1, 2, 3))
print(find_max(3, 2, 1))
print(find_max(1, 1, 1))

def find_max(a, b, c):
    return max(a, b, c)

print(find_max(1, 2, 3))
print(find_max(3, 2, 1))
print(find_max(1, 1, 1))
/python_basics/python_basics_12.py
"""
Write a function to find the maximum of three numbers.
assert find_max(1, 2, 3) == 3
assert find_max(3, 2, 1) == 3
assert find_max(1, 1, 1) == 1
"""

def find_max(a, b, c):
    return max(a, b, c)

print(find_max(1, 2, 3))
print(find_max(3, 2, 1))
print(find_max(1, 1, 1))

def find_max(a, b, c):
    return max(a, b, c)

print(find_max(1, 2, 3))
print(find_max(3, 2, 1))
print(find_max(1, 1, 1))

def find_max(a, b, c):
    return max(a, b, c)

print(find_max(1, 2, 3))
print(find_max(3, 2, 1))
print(find_max(1, 1,