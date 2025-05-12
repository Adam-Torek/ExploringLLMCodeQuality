"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""

def is_sublist(lst, sublst):
    if len(lst) < len(sublst):
        return False
    for i in range(len(lst) - len(sublst) + 1):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False

# Test cases
print(is_sublist([2,4,3,5,7],[3,7])) # False
print(is_sublist([1,2,3,4,5,6,7,8,9],[2,4,3,5])) # True
print(is_sublist([1,2,3,4,5,6,7,8,9],[2,4,3,5,7])) # False
print(is_sublist([1,2,3,4,5,6,7,8,9],[2,4,3,5,7,8,9])) # True
print(is_sublist([1,2,3,4,5,6,7,8,9],[2,4,3,5,7,8,9,10])) # False
print(is_sublist([1,2,3,4,5,6,7,8,9],[2,4,3,5,7,8,9,10,11]) # False

# Edge cases
print(is_sublist([],[])) # True
print(is_sublist([1],[1])) # True
print(is_sublist([1,2,3,4,5],[1,2,3,4,5]) # True
print(is_sublist([1,2,3,4,5],[1,2,3,4,6]) # False
print(is_sublist([1,2,3,4,5],[1,2,3,4,5,6]) # False
print(is_sublist([1,2,3,4,5],[1,2,3,4,5,6,7]) # False
print(is_sublist([1,2,3,4,5],[1,2,3,4,5,6,7,8]) # False
print(is_sublist([1,2,3,4,5],[1,2,3,4,5,6,7,8,9]) # False
print(is_sublist([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10]) # False
print(is_sublist([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11]) # False
print(is_sublist([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11]) # False
print(is_sublist([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12]) # False

# Negative cases
print(is_sublist([1,2,3,4,5,6,7,8,9],[2,4,3,5,7,8,9,10,11]) # False
print(is_sublist([1,2,3,4,5,6,7,8,9],[2,4,3,5,7,8,9,10,11]) # False
print(is_sublist([1,2,3,4,5,6,7,8,9],[2,4,3,5,7,8,9,10,11,12]) # False
print(is_sublist([1,2,3,4,5,6,7,8,9],[2,4,3,5,7,8,9,10,11,12]) # False
print(is_sublist([1,2,3,4,5,6,7,8,9],[2,4,3,5,7,8,9,10,11,12]) # False