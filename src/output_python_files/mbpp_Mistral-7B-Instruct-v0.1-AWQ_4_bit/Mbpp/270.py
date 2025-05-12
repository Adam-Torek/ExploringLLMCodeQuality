"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""

def sum_even_and_even_index(lst):
    """
    :param lst: list of integers
    :return: sum of even numbers at even positions
    """
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            sum += lst[i]
    return sum

# assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
# assert sum_even_and_even_index([1, 2, 3, 4, 5, 6]) == 0
# assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30