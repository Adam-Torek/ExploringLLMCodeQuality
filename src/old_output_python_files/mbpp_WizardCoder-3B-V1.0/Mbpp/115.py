"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""
def empty_dit(lst):
    for i in lst:
        if i:
            return False
    return True<|endoftext|>