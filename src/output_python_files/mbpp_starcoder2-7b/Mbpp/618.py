"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""

def div_list(a,b):
    return [a[i]/b[i] for i in range(len(a))]

print(div_list([4,5,6],[1, 2, 3]))
/python/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line.
"""

# Example 1

# Without list comprehension

list1 = []
for i in range(1,11):
    list1.append(i)
print(list1)

# With list comprehension

list2 = [i for i in range(1,11)]
print(list2)

# Example 2

# Without list comprehension

list1 = []
for i in range(1,11):
    if i%2==0:
        list1.append(i)
print(list1)

# With list comprehension

list2 = [i for i in range(1,11) if i%2==0]
print(list2)

# Example 3

# Without list comprehension

list1 = []
for i in range(1,11):
    list1.append(i**2)
print(list1)

# With list comprehension

list2 = [i**2 for i in range(1,11)]
print(list2)

# Example 4

# Without list comprehension

list1 = []
for i in range(1,11):
    if i%2==0:
        list1.append(i**2)
print(list1)

# With list comprehension

list2 = [i**2 for i in range(1,11) if i%2==0]
print(list2)

# Example 5

# Without list comprehension

list1 = []
for i in range(1,11):
    if i%2==0:
        list1.append(i**2)
    else:
        list1.append(i)
print(list1)

# With list comprehension

list2 = [i**2 if i%2==0 else i for i in range(1,11)]
print(list2)

# Example 6

# Without list comprehension

list1 = []
for i in range(1,11):
    if i%2==0:
        list1.append(i**2)
    else:
        list1.append(i)
print(list1)

# With list comprehension

list2 = [i**2 if i%2==0 else i for i in range(1,11)]
print(list2)

# Example 7

# Without list comprehension

list1 = []
for i in range(1,11):
    if i%2==0:
        list1.append(i**2)
    else:
        list1.append(i)
print(list1)

# With list comprehension

list2 = [i**2 if i%2==0 else i for i in range(1,11)]
print(list2)

# Example 8

# Without list comprehension

list1 = []
for i in range(1,11):
    if i%2==0:
        list1.append(i**2)
    else:
        list1.append(i)
print(list1)

# With list comprehension

list2 = [i**2 if i%2==0 else i for i in range(1,11)]
print(list2)

# Example 9

# Without list comprehension

list1 = []
for i in range(1,11):
    if i%2==0:
        list1.append(i**2)
    else:
        list1.append(i)
print(list1)

# With list comprehension

list2 = [i**2 if i%2==0 else i for i in range(1,11)]
print(list2)

# Example 10

# Without