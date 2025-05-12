"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""

def mul_even_odd(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even = even*i
        else:
            odd = odd*i
    return even*odd

print(mul_even_odd([1,3,5,7,4,1,6,8]))
/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line.
"""

# Example 1

# Without list comprehension
lst = []
for i in range(1,11):
    lst.append(i)
print(lst)

# With list comprehension
lst = [i for i in range(1,11)]
print(lst)

# Example 2

# Without list comprehension
lst = []
for i in range(1,11):
    if i%2==0:
        lst.append(i)
print(lst)

# With list comprehension
lst = [i for i in range(1,11) if i%2==0]
print(lst)

# Example 3

# Without list comprehension
lst = []
for i in range(1,11):
    if i%2==0:
        lst.append(i)
    else:
        lst.append(i*2)
print(lst)

# With list comprehension
lst = [i if i%2==0 else i*2 for i in range(1,11)]
print(lst)

# Example 4

# Without list comprehension
lst = []
for i in range(1,11):
    if i%2==0:
        lst.append(i)
    else:
        lst.append(i*2)
print(lst)

# With list comprehension
lst = [i if i%2==0 else i*2 for i in range(1,11)]
print(lst)

# Example 5

# Without list comprehension
lst = []
for i in range(1,11):
    if i%2==0:
        lst.append(i)
    else:
        lst.append(i*2)
print(lst)

# With list comprehension
lst = [i if i%2==0 else i*2 for i in range(1,11)]
print(lst)

# Example 6

# Without list comprehension
lst = []
for i in range(1,11):
    if i%2==0:
        lst.append(i)
    else:
        lst.append(i*2)
print(lst)

# With list comprehension
lst = [i if i%2==0 else i*2 for i in range(1,11)]
print(lst)

# Example 7

# Without list comprehension
lst = []
for i in range(1,11):
    if i%2==0:
        lst.append(i)
    else:
        lst.append(i*2)
print(lst)

# With list comprehension
lst = [i if i%2==0 else i*2 for i in range(1,11)]
print(lst)

# Example 8

# Without list comprehension
lst = []
for i in range(1,11):
    if i%2==0:
        lst.append(i)
    else:
        lst.append(i*2)
print(lst)

# With list comprehension
lst = [i if i%2==0 else i*2 for i in range(1,11)]
print(lst)

# Example 9

# Without list comprehension
lst = []
for i in range(1,11):
    if i%2==0:
        lst.append(i)
    else:
        lst.append(i*2)
print(lst)

# With list comprehension
lst = [i if i%2==0 else i*2 for i in range(1,11)]
print(lst)

# Example 10

# Without list comprehension
lst = []
for i in range(1,11):
    if i%