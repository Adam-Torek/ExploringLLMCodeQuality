"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""

def check_greater(arr, num):
    for i in arr:
        if i > num:
            return True
    return False

# Test cases
print(check_greater([1, 2, 3, 4, 5], 4)) # False
print(check_greater([1, 2, 3, 4, 5], 6)) # True<|endoftext|>