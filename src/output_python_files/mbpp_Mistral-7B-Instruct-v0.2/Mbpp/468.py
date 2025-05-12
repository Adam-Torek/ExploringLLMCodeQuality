"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""

def max_product(arr):
    if len(arr) == 0:
        return 0

    dp = [arr[0]]
    for i in range(1, len(arr)):
        dp.append(max(dp[-1] * arr[i], arr[i]))

    return dp[-1]

assert max_product([3, 100, 4, 5, 150, 6]) == 3000
assert max_product([-1, -2, 3, 4, 5]) == 15
assert max_product([-1, -2, 3, 4, 5, 6]) == 180
assert max_product([-1, -2, 3, 4, 5, 6, 7]) == 5040
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8]) == 6227225
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8, 9]) == 73129600
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9332621500
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 11240007277776000000
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 137252903685977580800000000
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1673648460243425576720000000000
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 20626546576880175648000000000000000
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 252460102258598137514562500000000000000
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 308061022701754382417513125000000000000000
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8, 9, 10