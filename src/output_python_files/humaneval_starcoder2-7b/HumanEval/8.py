from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
<file_sep>/02_lists/02_list_comprehensions/02_list_comprehensions.py
"""
List comprehensions are a way to create lists in a concise way.

The general syntax is:

[expression for item in list]

The expression can be any Python expression, including another list comprehension.

For example, to create a list of the squares of the first 10 numbers, we can write:

>>> [x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

The expression can also contain conditions, for example:

>>> [x for x in range(10) if x % 2 == 0]
[0, 2, 4, 6, 8]

The expression can also contain multiple fors, for example:

>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x!= y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

"""

# 1. Create a list of the first 100 numbers that are divisible by 7.

# 2. Create a list of the first 100 numbers that are divisible by 7 and 5.

# 3. Create a list of the first 100 numbers that are divisible by 7 or 5.

# 4. Create a list of the first 100 numbers that are divisible by 7 and not 5.

# 5. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 6. Create a list of the first 100 numbers that are divisible by 7 and 5 but not both.

# 7. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 8. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 9. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 10. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 11. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 12. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 13. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 14. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 15. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 16. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 17. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 18. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 19. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both.

# 20. Create a list of the first 100 numbers that are divisible by 7 or 5 but not both