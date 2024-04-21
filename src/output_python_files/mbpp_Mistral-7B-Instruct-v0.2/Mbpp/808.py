"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""
def check_K(tuple_list, k):
    for i in tuple_list:
        if k in i:
            return True
    return False

# Test case
assert check_K((10, 4, 5, 6, 8), 6) == True
assert check_K((1, 2, 3, 4, 5), 6) == False</s>