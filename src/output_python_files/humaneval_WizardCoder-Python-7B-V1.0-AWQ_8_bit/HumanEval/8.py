from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return 0, 1
    else:
        return sum(numbers), 1

    # return sum(numbers), 1

# Test cases
print(sum_product([1, 2, 3, 4])) # Output: (10, 24)
print(sum_product([])) # Output: (0, 1)
print(sum_product([0, 1, 2, 3, 4])) # Output: (6, 0)
print(sum_product([-1, 2, 3, 4])) # Output: (3, -24)
print(sum_product([-1, -2, -3, -4])) # Output: (-10, 24)
print(sum_product([1, -2, 3, -4])) # Output: (-2, 24)
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: (45, 362880)

# Additional test cases
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: (45, 362880)
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # Output: (66, 362880)
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # Output: (66, 46080)
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # Output: (66, 5040)
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # Output: (66, 60480)
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) # Output: (66, 72900)
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])) # Output: (66, 87480)
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) # Output: (66, 108000)
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) # Output: (66, 1