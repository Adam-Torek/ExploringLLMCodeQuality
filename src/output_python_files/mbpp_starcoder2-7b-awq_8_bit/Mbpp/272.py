"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""

def rear_extract(lst):
    return [x[-1] for x in lst]

print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))
/python/list_comprehension.py
"""
List comprehension is a way to create a list in a single line of code.
"""

# Example 1

# Without list comprehension

# lst = []
# for i in range(10):
#     lst.append(i)

# print(lst)

# With list comprehension

# lst = [i for i in range(10)]
# print(lst)

# Example 2

# Without list comprehension

# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(i)

# print(lst)

# With list comprehension

# lst = [i for i in range(10) if i % 2 == 0]
# print(lst)

# Example 3

# Without list comprehension

# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(i)
#     else:
#         lst.append(i * 2)

# print(lst)

# With list comprehension

# lst = [i if i % 2 == 0 else i * 2 for i in range(10)]
# print(lst)

# Example 4

# Without list comprehension

# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(i)
#     else:
#         lst.append(i * 2)
#     if i % 3 == 0:
#         lst.append(i * 3)

# print(lst)

# With list comprehension

# lst = [i if i % 2 == 0 else i * 2 for i in range(10)]
# lst = [i * 3 for i in lst if i % 3 == 0]
# print(lst)

# Example 5

# Without list comprehension

# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(i)
#     else:
#         lst.append(i * 2)
#     if i % 3 == 0:
#         lst.append(i * 3)
#     if i % 5 == 0:
#         lst.append(i * 5)

# print(lst)

# With list comprehension

# lst = [i if i % 2 == 0 else i * 2 for i in range(10)]
# lst = [i * 3 for i in lst if i % 3 == 0]
# lst = [i * 5 for i in lst if i % 5 == 0]
# print(lst)

# Example 6

# Without list comprehension

# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(i)
#     else:
#         lst.append(i * 2)
#     if i % 3 == 0:
#         lst.append(i * 3)
#     if i % 5 == 0:
#         lst.append(i * 5)
#     if i % 7 == 0:
#         lst.append(i * 7)

# print(lst)

# With list comprehension

# lst = [i if i % 2 == 0 else i * 2 for i in range(10)]
# lst = [i * 3 for i in lst if i % 3 == 0