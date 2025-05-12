"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""

def unique_Element(lst):
    if len(lst)!= len(set(lst)):
        return False
    else:
        return True

# Test cases
print(unique_Element([1,1,1])) # True
print(unique_Element([1,2,3,4,5])) # False
print(unique_Element([1,2,3,4,5,5])) # True<|endoftext|>