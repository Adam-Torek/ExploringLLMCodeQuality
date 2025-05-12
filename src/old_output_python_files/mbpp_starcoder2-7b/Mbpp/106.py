"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""

def add_lists(list1, tuple1):
    return tuple1 + tuple(list1)

print(add_lists([5, 6, 7], (9, 10)))
<file_sep>/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line of code.
"""

# Example 1

# Without list comprehension

list1 = []
for i in range(1, 11):
    list1.append(i)

print(list1)

# With list comprehension

list2 = [i for i in range(1, 11)]

print(list2)

# Example 2

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i for i in range(1, 11) if i % 2 == 0]

print(list2)

# Example 3

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i for i in range(1, 11) if i % 2 == 0]

print(list2)

# Example 4

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i for i in range(1, 11) if i % 2 == 0]

print(list2)

# Example 5

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i for i in range(1, 11) if i % 2 == 0]

print(list2)

# Example 6

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i for i in range(1, 11) if i % 2 == 0]

print(list2)

# Example 7

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i for i in range(1, 11) if i % 2 == 0]

print(list2)

# Example 8

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i for i in range(1, 11) if i % 2 == 0]

print(list2)

# Example 9

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i for i in range(1, 11) if i % 2 == 0]

print(list2)

# Example 10

# Without list comprehension

list1 = []
for i in range(1, 11):