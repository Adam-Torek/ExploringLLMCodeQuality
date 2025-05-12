"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""

def max_product(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    if len(arr) == 0:
        return 0
    else:
        return max(arr[0] * max_product(arr[1:]), arr[0] * arr[1:])


assert max_product([3, 100, 4, 5, 150, 6]) == 3000