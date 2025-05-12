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
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8]) == 73440
assert max_product([-1, -2, 3, 4, 5, 6, 7, 8, 9]) == 1267650600228229401496703205376
assert max_product([]) == 0
assert max_product([1]) == 1
assert max_product([1, 1]) == 1
assert max_product([1, 2]) == 2
assert max_product([1, 2, 3]) == 6
assert max_product([1, 2, 3, 4]) == 24
assert max_product([1, 2, 3, 4, 5]) == 120
assert max_product([1, 2, 3, 4, 5, 6]) == 360
assert max_product([1, 2, 3, 4, 5, 6, 7]) == 5040
assert max_product([1, 2, 3, 4, 5, 6, 7, 8]) == 73440
assert max_product([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1267650600228229401496703205376
assert max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 62270208000000000000000000000000000
assert max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 130767436800000000000000000000000000000
assert max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 30414093201713378043612608166064000000000
assert max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 115792089237316195423570985008687907853269984665640564034567882306470721417937131260723485500160615