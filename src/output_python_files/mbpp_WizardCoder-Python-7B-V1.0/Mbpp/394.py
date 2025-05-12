"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""

def check_distinct(tup):
    return len(tup) == len(set(tup))

# Test cases
print(check_distinct((1, 4, 5, 6, 1, 4)) == False) # True
print(check_distinct((1, 2, 3, 4, 5, 6)) == True) # True
print(check_distinct((1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)) == False) # False
print(check_distinct((1, 2, 3, 4, 5, 6, 7)) == True) # True
print(check_distinct((1, 2, 3, 4, 5, 6, 7, 8)) == True) # True
print(check_distinct((1, 2, 3, 4, 5, 6, 7, 8, 9)) == True) # True
print(check_distinct((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == True) # True
print(check_distinct((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == True) # True