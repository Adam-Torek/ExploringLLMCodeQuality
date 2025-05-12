"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""
def check_type(t):
    if len(set(map(type, t))) == 1:
        return True
    else:
        return False<|endoftext|>