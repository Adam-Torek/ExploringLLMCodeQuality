"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

def similar_elements(list1, list2):
    return set(list1).intersection(set(list2))

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))
<file_sep>/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line.
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