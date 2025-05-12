"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""
def sum_even_and_even_index(numbers):
    """
    This function takes a list of numbers as an argument and returns the sum of even numbers at even positions.

    :param numbers: list of numbers
    :return: int, the sum of even numbers at even positions
    """
    sum = 0
    index = 0
    while index < len(numbers):
        if index % 2 == 0 and numbers[index] % 2 == 0:
            sum += numbers[index]
        index += 1
    return sum

# Test the function
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6]) == 12
assert sum_even_and_even_index([1, 3, 5, 7, 9, 11]) == 0
assert sum_even_and_even_index([10, 11, 12, 13, 14, 15]) == 30
assert sum_even_and_even_index([]) == 0
assert sum_even_and_even_index([0]) == 0
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 22
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 34
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 22
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 36
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 48
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 60
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 72
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == 84
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 96
assert sum_even_and_even_index([1, 2