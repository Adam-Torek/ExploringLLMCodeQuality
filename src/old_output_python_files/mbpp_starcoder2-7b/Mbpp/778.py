"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""

def pack_consecutive_duplicates(lst):
    result = []
    for i in range(len(lst)):
        if i == 0:
            result.append([lst[i]])
        elif lst[i] == lst[i-1]:
            result[-1].append(lst[i])
        else:
            result.append([lst[i]])
    return result

print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
<file_sep>/python/python_101/002_lists/002_list_comprehensions.py
"""
List comprehensions are a way to create lists in a concise way.

The general syntax is:

[expression for item in list if conditional]

The expression is the result of the operation, the item is the element of the list, and the conditional is the if statement.

The following example creates a list of the first 10 square numbers:
"""

squares = [x**2 for x in range(10)]
print(squares)

"""
The following example creates a list of the first 10 square numbers that are even:
"""

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

"""
The following example creates a list of the first 10 square numbers that are even and less than 100:
"""

even_squares = [x**2 for x in range(10) if x % 2 == 0 and x**2 < 100]
print(even_squares)

"""
The following example creates a list of the first 10 square numbers that are even and less than 100, but only if the number is greater than 10:
"""

even_squares = [x**2 for x in range(10) if x % 2 == 0 and x**2 < 100 if x > 10]
print(even_squares)

"""
The following example creates a list of the first 10 square numbers that are even and less than 100, but only if the number is greater than 10, and the number is not a multiple of 5:
"""

even_squares = [x**2 for x in range(10) if x % 2 == 0 and x**2 < 100 if x > 10 if x % 5!= 0]
print(even_squares)

"""
The following example creates a list of the first 10 square numbers that are even and less than 100, but only if the number is greater than 10, and the number is not a multiple of 5, and the number is not a multiple of 3:
"""

even_squares = [x**2 for x in range(10) if x % 2 == 0 and x**2 < 100 if x > 10 if x % 5!= 0 if x % 3!= 0]
print(even_squares)

"""
The following example creates a list of the first 10 square numbers that are even and less than 100, but only if the number is greater than 10, and the number is not a multiple of 5, and the number is not a multiple of 3, and the number is not a multiple of 7:
"""

even_squares = [x**2 for x in range(10) if x % 2 == 0 and x**2 < 100 if x > 10 if x % 5!= 0 if x % 3!= 0 if x % 7!= 0]
print(even_squares)

"""
The following example creates a list of the first 1