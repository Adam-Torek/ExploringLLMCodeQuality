"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(list_of_lists):
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            list_of_lists[i][j] = float(list_of_lists[i][j])
    return list_of_lists

print(list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]))
<file_sep>/python_basics/03_lists/03_list_comprehension.py
"""
List comprehension is a way to create lists in a single line.

The general syntax is:

[expression for item in list]

The expression can be any Python expression, including another list comprehension.

The following example creates a list of the first letters of each word in the string "Hello World":
"""

print([word[0] for word in "Hello World".split()])

"""
The following example creates a list of two-letter strings from the words in the string "Hello World":
"""

print([word[:2] for word in "Hello World".split()])

"""
The following example creates a list of the squares of the numbers from 0 to 9:
"""

print([num ** 2 for num in range(10)])

"""
The following example creates a list of two-tuples where the first tuple item is an even number from 0 to 9 and the second tuple item is the square of the first tuple item:
"""

print([(num, num ** 2) for num in range(10) if num % 2 == 0])

"""
The following example creates a list of two-tuples where the first tuple item is an even number from 0 to 9 and the second tuple item is the square of the first tuple item. The expression is enclosed in parentheses so that it is treated as a single Python expression:
"""

print(list((num, num ** 2) for num in range(10) if num % 2 == 0))

"""
The following example creates a list of two-tuples where the first tuple item is an even number from 0 to 9 and the second tuple item is the square of the first tuple item. The expression is enclosed in parentheses so that it is treated as a single Python expression. The expression is enclosed in parentheses so that it is treated as a single Python expression:
"""

print(list((num, num ** 2) for num in range(10) if num % 2 == 0))

"""
The following example creates a list of two-tuples where the first tuple item is an even number from 0 to 9 and the second tuple item is the square of the first tuple item. The expression is enclosed in parentheses so that it is treated as a single Python expression:
"""

print(list((num, num ** 2) for num in range(10) if num % 2 == 0))

"""
The following example creates a list of two-tuples where the first tuple item is an even number from 0 to 9 and the second tuple item is the square of the first tuple item. The expression is enclosed in parentheses so that it is treated as a single Python expression:
"""

print(list((num, num ** 2) for num in range(10) if num % 2 == 0))

"""
The following example creates a list of two-tuples where the first tuple item is an even number from 0 to 9 and the second tuple item is the square of the first tuple item. The expression is enclosed in parentheses so that it is treated as a single Python expression:
"""

print(list((num, num ** 2) for num in range(10) if num % 2 == 0))

"""
The following example creates a list of two-tuples where the first tuple item is an even number from 0 to 9 and the second tuple item is the square of the first tuple item. The expression