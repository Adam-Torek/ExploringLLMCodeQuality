"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""

def common_element(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

# Test cases
print(common_element([1,2,3,4,5], [5,6,7,8,9])) # True
print(common_element([1,2,3,4], [6,7,8,9])) # False
print(common_element([1,2,3,4], [4,5,6,7])) # True
print(common_element([1,2,3], [1,2,3])) # True
print(common_element([1,2,3], [4,5,6])) # False
print(common_element([], [4,5,6])) # False
print(common_element([1,2,3], [])) # False

# Edge cases
print(common_element([], [])) # False
print(common_element([1], [1])) # True
print(common_element([1,2,3], [2,3,4])) # True
print(common_element([1,2,3], [4,5,6])) # False
print(common_element([1,2,3], [1,2,3,4])) # True
print(common_element([1,2,3,4], [1,2,3,4])) # True
print(common_element([1,2,3,4], [1,2,3,4,5])) # True
print(common_element([1,2,3,4,5], [5,6,7,8,9])) # True
print(common_element([1,2,3,4,5], [6,7,8,9])) # False
print(common_element([1,2,3,4,5], [1,2,3,4,5])) # True
print(common_element([1,2,3,4,5], [1,2,3,4,5,6])) # True
print(common_element([1,2,3,4,5], [1,2,3,4,5,6,7,8,9])) # True
print(common_element([1,2,3,4,5], [6,7,8,9,10]) # False

# Test case with empty lists
print(common_element([], [])) # False

# Test case with duplicate elements
print(common_element([1,2,3,4,5], [5,5,5,5,5])) # True
print(common_element([1,2,3,4,5], [5,5,5,5,6])) # True
print(common_element([1,2,3,4,5], [6,6,6,6,6])) # False
print(common_element([1,2,3,4,5], [1,1,1,1,1]) # True
print(common_element([1,2,3,4,5], [1,1,1,1,2]) # True

# Test case with lists of different length
print(common_element([1,2,3,4,5], [6,7,8,9])) # False
print(common_element([1,2,3,4,5], [5,6,7,8,9,10])) # True
print(common_element([1,2,3,4,5], [1,2,3,4,5,6,7,8,9])) # True
print(common_element([1,2,3,4,5], [1,2,3,4,5,6,7,8,9,10])) # True
print(common_element([1,2,3,4,5], [1,2,3,4,5,6,7,8,9,10,11]) # True
print(common_element([1,2,3,4,5], [1,2,3,4,5,6,7,8