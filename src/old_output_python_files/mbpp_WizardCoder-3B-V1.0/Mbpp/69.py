"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""

def is_sublist(lst, sublist):
    if len(sublist) > len(lst):
        return False
    for i in range(len(lst)-len(sublist)+1):
        if lst[i:i+len(sublist)] == sublist:
            return True
    return False

# Test cases
print(is_sublist([2,4,3,5,7],[3,7])) # False
print(is_sublist([2,4,3,5,7],[2,4,3])) # True
print(is_sublist([2,4,3,5,7],[2,4,3,5,7])) # True<|endoftext|>