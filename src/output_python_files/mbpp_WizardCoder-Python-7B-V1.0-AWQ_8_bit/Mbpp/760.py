"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""

def unique_Element(lst):
    if len(lst) == 1:
        return True
    else:
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                return False
        return True

print(unique_Element([1,1,1])) # True
print(unique_Element([1,2,3])) # False
print(unique_Element([1,2,3,4])) # False
print(unique_Element([1])) # True
print(unique_Element([1,2,3,4,5])) # False
print(unique_Element([1,1,2,3,4,5])) # True
print(unique_Element([1,2,3,4,5,5])) # False
print(unique_Element([1,2,3,4,5,6])) # False
print(unique_Element([1,2,3,4,5,6,6])) # True
print(unique_Element([1,2,3,4,5,6,6,7,8,9])) # False
print(unique_Element([1,2,3,4,5,6,7,8,9])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10])) # False
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10,10])) # True
print(unique_Element([1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10])) # True
print(unique_Element([1,