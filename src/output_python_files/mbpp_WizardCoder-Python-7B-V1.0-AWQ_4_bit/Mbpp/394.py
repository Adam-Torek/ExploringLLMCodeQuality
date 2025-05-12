"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""

def check_distinct(tup):
    return len(tup) == len(set(tup))

# Test cases
print(check_distinct((1, 4, 5, 6, 1, 4)) == False) # True
print(check_distinct((1, 2, 3, 4, 5, 6)) == True) # True
print(check_distinct((1, 1, 2, 2, 3, 3)) == False) # False
print(check_distinct((1, 2, 3, 4, 5)) == True) # True
print(check_distinct((1, 1, 2, 2, 3, 3, 4, 4, 5, 5)) == False) # False
print(check_distinct((1, 2, 3, 4, 5, 6)) == True) # True
print(check_distinct((1, 2, 3, 4, 5, 6, 7, 8, 9)) == True) # True
print(check_distinct((1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9) == False) # False