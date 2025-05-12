"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""

def sum_even_and_even_index(lst):
    sum = 0
    for i in range(0, len(lst), 2):
        sum += lst[i]
    return sum

assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6]) == 0
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8]) == 16
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 32
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 44
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 60
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 84
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 120
assert sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62,