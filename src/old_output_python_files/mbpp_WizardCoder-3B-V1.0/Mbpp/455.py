"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
def check_monthnumb_number(monthnumb):
    if monthnumb in [1,3,5,7,8,10,12]:
        return True
    else:
        return False<|endoftext|>