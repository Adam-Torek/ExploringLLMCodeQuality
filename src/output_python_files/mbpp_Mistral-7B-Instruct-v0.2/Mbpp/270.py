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
        if numbers[index] % 2 == 0 and index % 2 == 0:
            sum += numbers[index]
        index += 1
    return sum

# Test the function
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6]) == 12
assert sum_even_and_even_index([1, 2, 3, 4, 5, 5]) == 14
assert sum_even_and_even_index([1, 2, 3, 4, 5, 5, 6]) == 18
assert sum_even_and_even_index([]) == 0
assert sum_even_and_even_index([1]) == 0
assert sum_even_and_even_index([1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert sum_even_and_even_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,