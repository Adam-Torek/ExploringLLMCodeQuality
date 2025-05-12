"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
from typing import List


def largest_subset(numbers: List[int]) -> int:
    """
    Find the size of the largest subset of a list of numbers so that every pair is divisible.

    :param numbers: List of integers
    :return: The size of the largest subset
    """
    # Find the greatest common divisor of all pairs
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    # Create a set to store the numbers in the subset
    subset = set()

    # Find the largest subset
    while numbers:
        num = numbers.pop(0)
        for n in numbers:
            if gcd(num, n) != 1:
                subset.add(num)
                subset.add(n)
                break

    return len(subset)


if __name__ == "__main__":
    assert largest_subset([1, 3, 6, 13, 17, 18]) == 4
    assert largest_subset([1, 2, 3, 4, 5, 6]) == 6
    assert largest_subset([1, 2, 3, 4, 5, 6, 7]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 8]) == 7
    assert largest_subset([1, 2, 3, 4, 5, 6, 9]) == 7
    assert largest_subset([1, 2, 3, 4, 5, 6, 10]) == 11
    assert largest_subset([1, 2, 3, 4, 5, 6, 11]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 12]) == 12
    assert largest_subset([1, 2, 3, 4, 5, 6, 13]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 14]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 15]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 16]) == 16
    assert largest_subset([1, 2, 3, 4, 5, 6, 17]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 18]) == 18
    assert largest_subset([1, 2, 3, 4, 5, 6, 19]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 20]) == 20
    assert largest_subset([1, 2, 3, 4, 5, 6, 21]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 22]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 23]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 24]) == 24
    assert largest_subset([1, 2, 3, 4, 5, 6, 25]) == 25
    assert largest_subset([1, 2, 3, 4, 5, 6, 26]) == 26
    assert largest_subset([1, 2, 3, 4, 5, 6, 27]) == 27
    assert largest_subset([1, 2, 3, 4, 5,