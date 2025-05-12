"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""

def check_Consecutive(lst):
    """
    This function checks whether the given list contains consecutive numbers or not.
    """
    if len(lst) > 1:
        for i in range(1,len(lst)):
            if lst[i] - lst[i-1] != 1:
                return False
    return True

# Test cases
assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,2,3,4,6]) == False
assert check_Consecutive([1,2,3,4,5,6]) == False
assert check_Consecutive([1,2,3,4,5,6,7]) == True