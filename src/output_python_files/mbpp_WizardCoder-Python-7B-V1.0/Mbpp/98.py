"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""
from typing import List
import math

def multiply_num(lst: List[int]) -> float:
    product = 1
    for num in lst:
        product *= num
    return product / len(lst)

# Test cases
print(math.isclose(multiply_num([8, 2, 3, -1, 7]), -67.2, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5]), 3.2, rel_tol=0.001))
print(math.isclose(multiply_num([-1, -2, -3, -4, -5]), -3.2, rel_tol=0.001))
print(math.isclose(multiply_num([0, 0, 0, 0, 0]), 0, rel_tol=0.001))
print(math.isclose(multiply_num([1]), 1, rel_tol=0.001))
print(math.isclose(multiply_num([-1]), -1, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9]), 54, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 56, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 57, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 58, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 59, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 60, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 61, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), 62, rel_tol=0.001))
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1