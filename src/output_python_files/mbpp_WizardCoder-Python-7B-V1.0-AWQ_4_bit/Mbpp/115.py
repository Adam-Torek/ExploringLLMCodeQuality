"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""

def empty_dict(lst):
    for i in lst:
        if i:
            return False
    return True

print(empty_dict([{},{},{}])==True) #True
print(empty_dict([{1:2},{3:4},{}])==False #False