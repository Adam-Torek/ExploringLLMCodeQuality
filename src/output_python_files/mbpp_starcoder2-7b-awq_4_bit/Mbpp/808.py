"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""

def check_K(tup, k):
    return k in tup

assert check_K((10, 4, 5, 6, 8), 6) == True
assert check_K((10, 4, 5, 6, 8), 10) == True
assert check_K((10, 4, 5, 6, 8), 11) == False
assert check_K((10, 4, 5, 6, 8), 1) == False
assert check_K((10, 4, 5, 6, 8), 0) == False
assert check_K((10, 4, 5, 6, 8), 100) == False
assert check_K((10, 4, 5, 6, 8), 1000) == False
assert check_K((10, 4, 5, 6, 8), 10000) == False
assert check_K((10, 4, 5, 6, 8), 100000) == False
assert check_K((10, 4, 5, 6, 8), 1000000) == False
assert check_K((10, 4, 5, 6, 8), 10000000) == False
assert check_K((10, 4, 5, 6, 8), 100000000) == False
assert check_K((10, 4, 5, 6, 8), 1000000000) == False
assert check_K((10, 4, 5, 6, 8), 10000000000) == False
assert check_K((10, 4, 5, 6, 8), 100000000000) == False
assert check_K((10, 4, 5, 6, 8), 1000000000000) == False
assert check_K((10, 4, 5, 6, 8), 10000000000000) == False
assert check_K((10, 4, 5, 6, 8), 100000000000000) == False
assert check_K((10, 4, 5, 6, 8), 1000000000000000) == False
assert check_K((10, 4, 5, 6, 8), 10000000000000000) == False
assert check_K((10, 4, 5, 6, 8), 100000000000000000) == False
assert check_K((10, 4, 5, 6, 8), 1000000000000000000) == False
assert check_K((10, 4, 5, 6, 8), 10000000000000000000) == False
assert check_K((10, 4, 5, 6, 8), 100000000000000000000) == False
assert check_K((10, 4, 5, 6, 8), 1000000000000000000000) == False
assert check_K((10, 4, 5, 6, 8), 10000000000000000000000) == False
assert check_K((10, 4, 5, 6, 8), 1000