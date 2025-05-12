"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""

def all_unique(lst):
    return len(lst) == len(set(lst))

# Test cases
print(all_unique([1,2,3])) # True
print(all_unique([1,2,3,1])) # False
print(all_unique([1,2,3,4,5])) # True
print(all_unique([1,2,3,4,5,5])) # False
print(all_unique([1,2,3,4,5,6])) # True
print(all_unique([1,2,3,4,5,6,6])) # False
print(all_unique([1,2,3,4,5,6,7])) # True
print(all_unique([1,2,3,4,5,6,7,7])) # False
print(all_unique([1,2,3,4,5,6,7,8])) # True
print(all_unique([1,2,3,4,5,6,7,8,8])) # False
print(all_unique([1,2,3,4,5,6,7,8,9])) # True
print(all_unique([1,2,3,4,5,6,7,8,9,9])) # False
print(all_unique([1,2,3,4,5,6,7,8,9,10])) # True
print(all_unique([1,2,3,4,5,6,7,8,9,10,10])) # False

# Test case for empty list
print(all_unique([])) # True

# Test case for list with duplicate elements
print(all_unique([1,2,3,4,5,6,7,8,9,10,10,10])) # False

# Test case for list with negative numbers
print(all_unique([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10])) # True

# Test case for list with negative and positive numbers
print(all_unique([-1,-2,2,3,4,5,6,7,8,9,10])) # False

# Test case for list with float numbers
print(all_unique([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])) # True

# Test case for list with float and integer numbers
print(all_unique([1.0,2,3,4,5,6,7,8,9,10])) # False

# Test case for list with string elements
print(all_unique(['a','b','c','d','e','f','g','h','i'])) # True

# Test case for list with string and integer elements
print(all_unique(['a',1,2,3,4,5,6,7,8,9,10])) # False

# Test case for list with string and float elements
print(all_unique(['a',1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])) # False

# Test case for list with string, integer and float elements
print(all_unique(['a',1,2,3,4,5,6,7,8,9,10,1.0]) # False

# Test case for list with string, integer and float elements
print(all_unique(['a',1,2,3,4,5,6,7,8,9,10,'a'])) # False

# Test case for list with string, integer and float elements
print(all_unique(['a',1,2,3,4,5,6,7,8,9,10,1.0,1.0]) # False

# Test case for list with string, integer and float elements
print(all_unique(['a',1,2,3,4,5,6,7,8,9,10,1.0,1.0,1.0]) # False

# Test case for list with string, integer and float