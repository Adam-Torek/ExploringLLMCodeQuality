"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""

def check_Consecutive(lst):
    if len(lst) < 2:
        return False
    for i in range(len(lst)-1):
        if lst[i] + 1 == lst[i+1]:
            return True
    return False

# Test cases
print(check_Consecutive([1,2,3,4,5])) # True
print(check_Consecutive([1,2,3,4])) # False
print(check_Consecutive([1,2,3])) # False<|endoftext|>