"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""

def check_none(tup):
    for i in tup:
        if i is None:
            return True
    return False

# Test cases
print(check_none((10, 4, 5, 6, None)) == True) # True
print(check_none((10, 4, 5, 6, 7)) == False) # False
print(check_none((None, None, None)) == True) # True
print(check_none((1, 2, 3, 4, 5) == False) # False
print(check_none((1, None, 3, 4, 5) == True) # True
print(check_none((1, 2, 3, 4, 5) == False) # False
print(check_none((1, 2, 3, 4, 5, None) == True) # True
print(check_none((1, 2, 3, 4, 5, 6) == False) # False
print(check_none((1, 2, None, 4, 5) == True) # True
print(check_none((1, 2, 3, None, 5) == True) # True
print(check_none((1, 2, 3, 4, None) == True) # True
print(check_none((1, None, 3, 4, 5) == True) # True
print(check_none((None, 2, 3, 4, 5) == True) # True
print(check_none((1, 2, None, 4, None) == True) # True
print(check_none((1, None, 3, None, 5) == True) # True
print(check_none((None, None, None, None) == True) # True
print(check_none((None, None, None, None, None) == True) # True
print(check_none((1, 2, 3, 4, 5) == False) # False
print(check_none((1, 2, 3, 4, 5, None) == True) # True
print(check_none((1, 2, 3, 4, None) == True) # True
print(check_none((1, None, 3, 4, None) == True) # True
print(check_none((None, 2, 3, 4, None) == True) # True
print(check_none((1, None, 3, None, 5) == True) # True
print(check_none((None, None, None, None) == True) # True
print(check_none((1, 2, 3, 4, 5) == False) # False
print(check_none((1, 2, 3, 4, 5, None) == True) # True
print(check_none((1, 2, 3, 4, None) == True) # True
print(check_none((1, None, 3, None, 5) == True) # True
print(check_none((None, None, None, None) == True) # True
print(check_none((None, None, None, None, None) == True) # True
print(check_none((1, 2, 3, 4, 5) == False) # False
print(check_none((1, 2, 3, 4, 5, None) == True) # True
print(check_none((1, 2, 3, 4, None) == True) # True
print(check_none((1, None, 3, None, 5) == True) # True
print(check_none((None, 2, 3, None, None) == True) # True
print(check