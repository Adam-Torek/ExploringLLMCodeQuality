"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""

def tuple_to_int(tup):
    return int(''.join(map(str,tup)))

print(tuple_to_int((1,2,3)))
/python/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line of code.
"""

# Example 1

# Without list comprehension

# list_1 = []
# for i in range(10):
#     list_1.append(i)

# print(list_1)

# With list comprehension

# list_2 = [i for i in range(10)]
# print(list_2)

# Example 2

# Without list comprehension

# list_1 = []
# for i in range(10):
#     if i%2==0:
#         list_1.append(i)

# print(list_1)

# With list comprehension

# list_2 = [i for i in range(10) if i%2==0]
# print(list_2)

# Example 3

# Without list comprehension

# list_1 = []
# for i in range(10):
#     if i%2==0:
#         list_1.append(i**2)

# print(list_1)

# With list comprehension

# list_2 = [i**2 for i in range(10) if i%2==0]
# print(list_2)

# Example 4

# Without list comprehension

# list_1 = []
# for i in range(10):
#     if i%2==0:
#         list_1.append(i**2)
#     else:
#         list_1.append(i)

# print(list_1)

# With list comprehension

# list_2 = [i**2 if i%2==0 else i for i in range(10)]
# print(list_2)

# Example 5

# Without list comprehension

# list_1 = []
# for i in range(10):
#     if i%2==0:
#         list_1.append(i**2)
#     else:
#         list_1.append(i)
#     if i%3==0:
#         list_1.append(i**3)

# print(list_1)

# With list comprehension

# list_2 = [i**2 if i%2==0 else i for i in range(10)]
# list_2.extend([i**3 for i in range(10) if i%3==0])
# print(list_2)

# Example 6

# Without list comprehension

# list_1 = []
# for i in range(10):
#     if i%2==0:
#         list_1.append(i**2)
#     else:
#         list_1.append(i)
#     if i%3==0:
#         list_1.append(i**3)
#     if i%5==0:
#         list_1.append(i**5)

# print(list_1)

# With list comprehension

# list_2 = [i**2 if i%2==0 else i for i in range(10)]
# list_2.extend([i**3 for i in range(10) if i%3==0])
# list_2.extend([i**5 for i in range(10) if i%5==0])
# print(list_2)

# Example 7

# Without list comprehension

# list_1 = []
# for i in range(10):
#     if i%2==0: