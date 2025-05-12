"""
Write a function to remove all elements from a given list present in another list.
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
"""

def remove_elements(list1, list2):
    for i in list2:
        if i in list1:
            list1.remove(i)
    return list1

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))
/python/python_basics/list_comprehension.py
"""
List comprehension is an elegant way to create new list from an existing list.
"""

# List comprehension

# Without list comprehension
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

# With list comprehension
squares = [i**2 for i in range(10)]
print(squares)

# Without list comprehension
even_squares = []
for i in range(10):
    if i % 2 == 0:
        even_squares.append(i**2)
print(even_squares)

# With list comprehension
even_squares = [i**2 for i in range(10) if i % 2 == 0]
print(even_squares)

# Without list comprehension
cubes_by_four = []
for i in range(10):
    if i % 4 == 0:
        cubes_by_four.append(i**3)
print(cubes_by_four)

# With list comprehension
cubes_by_four = [i**3 for i in range(10) if i % 4 == 0]
print(cubes_by_four)
/python/python_basics/list_comprehension_with_if_else.py
"""
List comprehension is an elegant way to create new list from an existing list.
"""

# List comprehension with if else

# Without list comprehension
squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i**2)
    else:
        squares.append(i**3)
print(squares)

# With list comprehension
squares = [i**2 if i % 2 == 0 else i**3 for i in range(10)]
print(squares)
/python/python_basics/list_comprehension_with_nested_for_loop.py
"""
List comprehension is an elegant way to create new list from an existing list.
"""

# List comprehension with nested for loop

# Without list comprehension
squares = []
for i in range(10):
    for j in range(10):
        squares.append(i**2)
print(squares)

# With list comprehension
squares = [i**2 for i in range(10) for j in range(10)]
print(squares)
/python/python_basics/list_comprehension_with_nested_for_loop_and_if_else.py
"""
List comprehension is an elegant way to create new list from an existing list.
"""

# List comprehension with nested for loop and if else

# Without list comprehension
squares = []
for i in range(10):
    for j in range(10):
        if i % 2 == 0:
            squares.append(i**2)
        else:
            squares.append(i**3)
print(squares)

# With list comprehension
squares = [i**2 if i % 2 == 0 else i**3 for i in range(10) for j in range(10)]
print(squares)
/python/python_basics/list_comprehension_with_nested_for_loop_and_if_else_and_else.py
"""
List comprehension is an elegant way to create new list from an existing list.
"""

# List comprehension with nested for loop and if else and else

# Without list comprehension
squares = []
for i in range(