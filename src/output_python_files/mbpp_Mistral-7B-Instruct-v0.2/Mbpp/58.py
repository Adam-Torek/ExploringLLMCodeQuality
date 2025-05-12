"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""
def opposite_Signs(num1, num2):
    if num1 > 0 and num2 < 0 or num1 < 0 and num2 > 0:
        return True
    else:
        return False

# Test the function
assert opposite_Signs(1,-2) == True
assert opposite_Signs(1,2) == False
assert opposite_Signs(-1,1) == True
assert opposite_Signs(0,0) == False