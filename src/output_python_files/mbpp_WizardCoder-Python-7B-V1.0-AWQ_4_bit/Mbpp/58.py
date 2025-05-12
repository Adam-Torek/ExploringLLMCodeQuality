"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""

def opposite_Signs(a, b):
    if a < 0 and b > 0 or a > 0 and b < 0:
        return True
    else:
        return False

print(opposite_Signs(1, -2)) # True
print(opposite_Signs(3, 4)) # False
print(opposite_Signs(-5, 6)) # True
print(opposite_Signs(7, -8)) # True
print(opposite_Signs(0, 0)) # False
print(opposite_Signs(-10, 10)) # False
print(opposite_Signs(10, -10)) # False
print(opposite_Signs(-10, -10)) # False
print(opposite_Signs(0, 10)) # False
print(opposite_Signs(10, 0)) # False
print(opposite_Signs(-10, -10)) # False
print(opposite_Signs(-10, 10)) # False
print(opposite_Signs(10, -10)) # False
print(opposite_Signs(0, -10)) # False
print(opposite_Signs(-10, 0)) # False
print(opposite_Signs(0, 10) # False

# All test cases should return True for the given input.