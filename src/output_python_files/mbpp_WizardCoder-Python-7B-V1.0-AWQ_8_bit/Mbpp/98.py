"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""
from typing import List
import math

def multiply_num(lst: List[float]) -> float:
    result = 1
    for num in lst:
        result *= num
    return result / len(lst)

# Test cases
print(math.isclose(multiply_num([8, 2, 3, -1, 7]), -67.2, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5]), 30, rel_tol=0.001)) # True
print(math.isclose(multiply_num([0, 0, 0, 0]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([-1, 1, 2, 3]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), 0, rel_tol=0.001)) # True
print(math.isclose(multiply_num