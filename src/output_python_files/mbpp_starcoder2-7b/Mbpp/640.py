"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""

def remove_parenthesis(string):
    return string[0:string.index("(")]

print(remove_parenthesis(["python (chrome)"]))/python_basics/list_comprehension.py
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
    list1.append(i**2)

print(list1)

# With list comprehension

list2 = [i**2 for i in range(1, 11)]
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
        list1.append(i**2)

print(list1)

# With list comprehension

list2 = [i**2 for i in range(1, 11) if i % 2 == 0]
print(list2)

# Example 5

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i**2)
    else:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i**2 if i % 2 == 0 else i for i in range(1, 11)]
print(list2)

# Example 6

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i**2)
    else:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i**2 if i % 2 == 0 else i for i in range(1, 11)]
print(list2)

# Example 7

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i**2)
    else:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i**2 if i % 2 == 0 else i for i in range(1, 11)]
print(list2)

# Example 8

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i**2)
    else:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i**2 if i % 2 == 0 else i for i in range(1, 11)]
print(list2)

# Example 9

# Without list comprehension

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i**2)
    else:
        list1.append(i)

print(list1)

# With list comprehension

list2 = [i**2 if