"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""
def find_lucas(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return find_lucas(n-1) + find_lucas(n-2)