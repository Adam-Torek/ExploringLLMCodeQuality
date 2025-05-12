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
print(opposite_Signs(-1, 2)) # True
print(opposite_Signs(1, 2)) # False
print(opposite_Signs(0, 0)) # False
print(opposite_Signs(-1, -2)) # False
print(opposite_Signs(0, 1)) # False
print(opposite_Signs(-1, 0)) # False
print(opposite_Signs(1, 0)) # False
print(opposite_Signs(0, -1)) # False
print(opposite_Signs(0, 0)) # False
print(opposite_Signs(-1, 1)) # False
print(opposite_Signs(2, -2)) # True
print(opposite_Signs(-2, 2)) # True
print(opposite_Signs(-1, 1)) # False
print(opposite_Signs(1, -1)) # False
print(opposite_Signs(-2, -1)) # False
print(opposite_Signs(2, 1)) # False
print(opposite_Signs(1, 2)) # False
print(opposite_Signs(-2, -1)) # False
print(opposite_Signs(-1, -2)) # False
print(opposite_Signs(1, 1)) # False
print(opposite_Signs(-1, -1)) # False
print(opposite_Signs(2, 2)) # False
print(opposite_Signs(-2, -2)) # False
print(opposite_Signs(0, 1)) # False
print(opposite_Signs(1, 0)) # False
print(opposite_Signs(-1, 0)) # False
print(opposite_Signs(0, -1)) # False
print(opposite_Signs(0, 0)) # False
print(opposite_Signs(2, 0)) # False
print(opposite_Signs(0, 2)) # False
print(opposite_Signs(-2, 0)) # False
print(opposite_Signs(0, -2)) # False
print(opposite_Signs(-2, 0)) # False
print(opposite_Signs(0, 0)) # False
print(opposite_Signs(1, 0)) # False
print(opposite_Signs(0, 1)) # False
print(opposite_Signs(-1, 0)) # False
print(opposite_Signs(0, -1)) # False
print(opposite_Signs(0, 0)) # False
print(opposite_Signs(2, 0)) # False
print(opposite_Signs(0, 2)) # False
print(opposite_Signs(-2, 0)) # False
print(opposite_Signs(0, -2)) # False
print(opposite_Signs(0, 0)) # False
print(opposite_Signs(-2, 0)) # False
print(opposite_Signs(0, -2)) # False
print(opposite_Signs(0, 0) # False