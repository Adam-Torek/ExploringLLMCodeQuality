"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""

def diff_even_odd(lst):
    even_index = 0
    odd_index = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_index = i
            break
    for i in range(len(lst)):
        if lst[i] % 2!= 0:
            odd_index = i
            break
    return lst[even_index] - lst[odd_index]

print(diff_even_odd([1,3,5,7,4,1,6,8]))
/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line of code.
"""

# Example 1

# Without list comprehension
lst = []
for i in range(10):
    lst.append(i)
print(lst)

# With list comprehension
lst = [i for i in range(10)]
print(lst)

# Example 2

# Without list comprehension
lst = []
for i in range(10):
    if i % 2 == 0:
        lst.append(i)
print(lst)

# With list comprehension
lst = [i for i in range(10) if i % 2 == 0]
print(lst)

# Example 3

# Without list comprehension
lst = []
for i in range(10):
    if i % 2 == 0:
        lst.append(i)
    else:
        lst.append(i * 2)
print(lst)

# With list comprehension
lst = [i if i % 2 == 0 else i * 2 for i in range(10)]
print(lst)

# Example 4

# Without list comprehension
lst = []
for i in range(10):
    if i % 2 == 0:
        lst.append(i)
    else:
        lst.append(i * 2)
print(lst)

# With list comprehension
lst = [i if i % 2 == 0 else i * 2 for i in range(10)]
print(lst)

# Example 5

# Without list comprehension
lst = []
for i in range(10):
    if i % 2 == 0:
        lst.append(i)
    else:
        lst.append(i * 2)
print(lst)

# With list comprehension
lst = [i if i % 2 == 0 else i * 2 for i in range(10)]
print(lst)

# Example 6

# Without list comprehension
lst = []
for i in range(10):
    if i % 2 == 0:
        lst.append(i)
    else:
        lst.append(i * 2)
print(lst)

# With list comprehension
lst = [i if i % 2 == 0 else i * 2 for i in range(10)]
print(lst)

# Example 7

# Without list comprehension
lst = []
for i in range(10):
    if i % 2 == 0:
        lst.append(i)
    else:
        lst.append(i * 2)
print(lst)

# With list comprehension
lst = [i if i % 2 == 0 else i * 2 for i in range(10)]
print(lst)

# Example 8

# Without list comprehension
lst = []
for i in range(10):
    if i % 2 == 0:
        lst.append(i)
    else:
        lst.append(i * 2)
print(lst)

# With list comprehension
lst = [i if i % 2 == 0 else i * 2 for i in range(10)]
print(lst)

# Example 9

# Without list comprehension
lst = []
for i in range(10):
    if i % 2 == 0:
        lst.append(i)
    else:
        lst.append(i * 2)