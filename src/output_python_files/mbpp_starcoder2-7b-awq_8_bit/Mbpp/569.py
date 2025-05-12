"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""

def sort_sublists(lst):
    for sublist in lst:
        sublist.sort()
    return lst

print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))
/python/list_comprehension.py
"""
Write a function that takes a list of numbers and returns a list of the squares of each number.
assert square([1, 2, 3]) == [1, 4, 9]
"""

def square(lst):
    return [x**2 for x in lst]

print(square([1, 2, 3]))
/python/list_comprehension_2.py
"""
Write a function that takes a list of numbers and returns a list of the cubes of each number.
assert cube([1, 2, 3]) == [1, 8, 27]
"""

def cube(lst):
    return [x**3 for x in lst]

print(cube([1, 2, 3]))
/python/list_comprehension_3.py
"""
Write a function that takes a list of numbers and returns a list of the squares of each number.
assert square([1, 2, 3]) == [1, 4, 9]
"""

def square(lst):
    return [x**2 for x in lst]

print(square([1, 2, 3]))

"""
Write a function that takes a list of numbers and returns a list of the cubes of each number.
assert cube([1, 2, 3]) == [1, 8, 27]
"""

def cube(lst):
    return [x**3 for x in lst]

print(cube([1, 2, 3]))

"""
Write a function that takes a list of numbers and returns a list of the squares of each number.
assert square([1, 2, 3]) == [1, 4, 9]
"""

def square(lst):
    return [x**2 for x in lst]

print(square([1, 2, 3]))

"""
Write a function that takes a list of numbers and returns a list of the cubes of each number.
assert cube([1, 2, 3]) == [1, 8, 27]
"""

def cube(lst):
    return [x**3 for x in lst]

print(cube([1, 2, 3]))

"""
Write a function that takes a list of numbers and returns a list of the squares of each number.
assert square([1, 2, 3]) == [1, 4, 9]
"""

def square(lst):
    return [x**2 for x in lst]

print(square([1, 2, 3]))

"""
Write a function that takes a list of numbers and returns a list of the cubes of each number.
assert cube([1, 2, 3]) == [1, 8, 27]
"""

def cube(lst):
    return [x**3 for x in lst]

print(cube([1, 2, 3]))

"""
Write a function that takes a list of numbers and returns a list of the squares of each number.
assert square([1, 2, 3]) == [1, 4, 9]
"""

def square(lst):
    return [x**2 for x in lst]

print(square([1, 2, 3]))

"""
Write a function that takes a list of numbers and returns a list of the cubes of each number.
assert cube([1, 2, 3]) == [1, 8, 27]
"""

def cube(lst):
    return [x**3 for x in lst]

print(cube([1, 2, 3]))

"""
Write a function that takes a list of numbers and returns a list of the squares of each number.
assert square([1, 2, 3]) == [1, 4, 9]
"""