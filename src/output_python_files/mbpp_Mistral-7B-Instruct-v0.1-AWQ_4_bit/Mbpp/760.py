"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""

def unique_Element(lst):
    # Using set to remove duplicates from list
    # If length of set is equal to length of list then means all elements are unique
    return len(set(lst)) == len(lst)

# Testing the function
assert unique_Element([1,1,1]) == True
assert unique_Element([1,2,3,4,5]) == True
assert unique_Element([1,2,3,4,5,6,7,8,9,9]) == False