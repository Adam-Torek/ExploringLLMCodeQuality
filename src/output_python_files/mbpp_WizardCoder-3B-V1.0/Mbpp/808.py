"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""

def check_K(lst, k):
    return k in lst

# Test cases
print(check_K((10, 4, 5, 6, 8), 6)) # True
print(check_K((10, 4, 5, 6, 8), 7)) # False<|endoftext|>