"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""

def empty_dict(lst):
    for i in lst:
        if i:
            return False
    return True

# assert empty_dict([{},{},{}])==True
# assert empty_dict([{'a':1},{'b':2}])==False