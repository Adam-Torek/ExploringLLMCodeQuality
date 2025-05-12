"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""
def is_sublist(lst, sublst):
    if len(sublst) > len(lst):
        return False
    for i in range(len(lst) - len(sublst) + 1):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False

# Test cases
print(is_sublist([2,4,3,5,7],[3,7])) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3])) # True
print(is_sublist([1,2,3,4,5,6,7],[4,5,6])) # True
print(is_sublist([1,2,3,4,5,6,7],[7,8])) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7])) # True
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8])) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9])) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10])) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10,11]) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10,11,12]) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10,11,12,13]) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10,11,12,13,14]) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) # False
print(is_sublist([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) # False
print(is_sub