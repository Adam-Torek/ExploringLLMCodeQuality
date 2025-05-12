"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""

def rear_extract(list_of_tuples):
    return [x[-1] for x in list_of_tuples]

print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))
/python_basics/list_comprehension.py
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
    else:
        list1.append(i * 2)

print(list1)

# With list comprehension

list2 = [i if i % 2 == 0 else i * 2 for i in range(1, 11)]
print(list2)

# Example 4

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)
    else:
        list1.append(i * 2)

print(list1)

# With list comprehension

list2 = [i if i % 2 == 0 else i * 2 for i in range(1, 11)]
print(list2)

# Example 5

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)
    else:
        list1.append(i * 2)

print(list1)

# With list comprehension

list2 = [i if i % 2 == 0 else i * 2 for i in range(1, 11)]
print(list2)

# Example 6

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)
    else:
        list1.append(i * 2)

print(list1)

# With list comprehension

list2 = [i if i % 2 == 0 else i * 2 for i in range(1, 11)]
print(list2)

# Example 7

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)
    else:
        list1.append(i * 2)

print(list1)

# With list comprehension

list2 = [i if i % 2 == 0 else i * 2 for i in range(1, 11)]
print(list2)

# Example 8

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)
    else:
        list1.append(i * 2)

print(list1)

# With list comprehension

list2 = [i if i % 2 == 0 else i * 2 for i