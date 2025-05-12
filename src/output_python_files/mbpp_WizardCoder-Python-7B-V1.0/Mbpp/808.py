"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""

def check_K(tup, k):
    return k in tup

# Test cases
print(check_K((10, 4, 5, 6, 8), 6)) # True
print(check_K((10, 4, 5, 6, 8), 7)) # False
print(check_K((10, 4, 5, 6, 8), 8)) # True
print(check_K((10, 4, 5, 6, 8), 10)) # True
print(check_K((10, 4, 5, 6, 8), 11)) # False
print(check_K((10, 4, 5, 6, 8), 5)) # True
print(check_K((10, 4, 5, 6, 8), 4)) # True
print(check_K((10, 4, 5, 6, 8), 3)) # False
print(check_K((10, 4, 5, 6, 8), 9)) # False
print(check_K((10, 4, 5, 6, 8), 5)) # True
print(check_K((10, 4, 5, 6, 8), 1)) # False
print(check_K((10, 4, 5, 6, 8), 0)) # False
print(check_K((10, 4, 5, 6, 8), 8)) # True
print(check_K((10, 4, 5, 6, 8), 9)) # False
print(check_K((10, 4, 5, 6, 8), 11)) # False
print(check_K((10, 4, 5, 6, 8), 12)) # False
print(check_K((10, 4, 5, 6, 8), 5)) # True
print(check_K((10, 4, 5, 6, 8), 10)) # True
print(check_K((10, 4, 5, 6, 8), 1)) # False
print(check_K((10, 4, 5, 6, 8), 0)) # False
print(check_K((10, 4, 5, 6, 8), 9)) # False
print(check_K((10, 4, 5, 6, 8), 11)) # False
print(check_K((10, 4, 5, 6, 8), 12)) # False
print(check_K((10, 4, 5, 6, 8), 5)) # True
print(check_K((10, 4, 5, 6, 8), 10)) # True
print(check_K((10, 4, 5, 6, 8), 1)) # False
print(check_K((10, 4, 5, 6, 8), 0)) # False
print(check_K((10, 4, 5, 6, 8), 9)) # False
print(check_K((10, 4, 5, 6, 8), 11)) # False
print(check_K((10, 4, 5, 6, 8), 12)) # False
print(check_K((10, 4, 5, 6, 8), 5)) # True
print(check_K((10, 4, 5, 6, 8), 10)) # True
print(check_K((10, 4, 5, 6, 8), 1)) # False
print(check_K((10, 4, 5, 6, 8), 0)) # False
print(check_K((10, 4, 5,