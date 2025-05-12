"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""
def opposite_Signs(a,b):
    if a*b < 0:
        return True
    else:
        return False