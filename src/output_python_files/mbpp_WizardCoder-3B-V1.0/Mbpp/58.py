"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""

def opposite_Signs(a, b):
    return (a * b) < 0

# Test cases
print(opposite_Signs(1,-2)) # True
print(opposite_Signs(0,0)) # True
print(opposite_Signs(1,1)) # False<|endoftext|>