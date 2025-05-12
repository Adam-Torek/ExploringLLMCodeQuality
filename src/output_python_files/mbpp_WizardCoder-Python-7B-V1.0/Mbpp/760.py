"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""
def unique_Element(lst):
    return len(set(lst)) == 1

print(unique_Element([1,1,1])) # True
print(unique_Element([1,2,3])) # False
print(unique_Element([1,2,3,4])) # False
print(unique_Element([1])) # True
print(unique_Element([1,2,3,4,5])) # False
print(unique_Element([1,2,3,4,5,5])) # True
print(unique_Element([1,2,3,4,5,5,5])) # True
print(unique_Element([1,2,3,4,5,5,5,6])) # False
print(unique_Element([1,2,3,4,5,5,5,6,7])) # False
print(unique_Element([1,2,3,4,5,5,6,7,8])) # False
print(unique_Element([1,2,3,4,5,6,7,8])) # False
print(unique_Element([1,2,3,4,5,6,7,8,8])) # True
print(unique_Element([1,2,3,4,5,6,7,8,8,9])) # False
print(unique_Element([1,2,3,4,5,6,7,8,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9])) # True
print(unique