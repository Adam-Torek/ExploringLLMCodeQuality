"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""

def check_distinct(t):
    return len(t) == len(set(t))

# Test cases
print(check_distinct((1, 4, 5, 6, 1, 4))) # False
print(check_distinct((1, 2, 3, 4, 5))) # True<|endoftext|>