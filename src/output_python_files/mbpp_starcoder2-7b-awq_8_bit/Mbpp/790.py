"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""

def even_position(lst):
    for i in range(0,len(lst),2):
        if lst[i]%2!= 0:
            return False
    return True

print(even_position([3,2,1]))
print(even_position([2,4,6,8]))
/python_basics/list_comprehension.py
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
#     if i%2 == 0:
#         lst.append(i)
# print(lst)

# With list comprehension

# lst = [i for i in range(10) if i%2 == 0]
# print(lst)

# Example 3

# Without list comprehension

# lst = []
# for i in range(10):
#     if i%2 == 0:
#         lst.append(i**2)
# print(lst)

# With list comprehension

# lst = [i**2 for i in range(10) if i%2 == 0]
# print(lst)

# Example 4

# Without list comprehension

# lst = []
# for i in range(10):
#     if i%2 == 0:
#         lst.append(i**2)
#     else:
#         lst.append(i)
# print(lst)

# With list comprehension

# lst = [i**2 if i%2 == 0 else i for i in range(10)]
# print(lst)

# Example 5

# Without list comprehension

# lst = []
# for i in range(10):
#     if i%2 == 0:
#         lst.append(i**2)
#     else:
#         lst.append(i)
# print(lst)

# With list comprehension

# lst = [i**2 if i%2 == 0 else i for i in range(10)]
# print(lst)

# Example 6

# Without list comprehension

# lst = []
# for i in range(10):
#     if i%2 == 0:
#         lst.append(i**2)
#     else:
#         lst.append(i)
# print(lst)

# With list comprehension

# lst = [i**2 if i%2 == 0 else i for i in range(10)]
# print(lst)

# Example 7

# Without list comprehension

# lst = []
# for i in range(10):
#     if i%2 == 0:
#         lst.append(i**2)
#     else:
#         lst.append(i)
# print(lst)

# With list comprehension

# lst = [i**2 if i%2 == 0 else i for i in range(10)]
# print(lst)

# Example 8

# Without list comprehension

# lst = []
# for i in range(10):
#     if i%2 == 0:
#         lst.append(i**2)
#     else:
#         lst.append(i)
# print(lst)

# With list comprehension

# lst = [i**2 if i%2 == 0 else i for i in range(10)]
# print(lst)

# Example 9

# Without list comprehension

# lst = []
# for i in range(10):
#     if i%2 == 0:
#         lst.append(i**2)
#     else:
#         lst.append(i)
# print(lst)

#