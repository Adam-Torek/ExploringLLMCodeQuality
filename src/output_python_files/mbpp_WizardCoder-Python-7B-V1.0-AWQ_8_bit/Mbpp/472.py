"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""

def check_Consecutive(lst):
    for i in range(len(lst)-1):
        if lst[i+1]-lst[i] == 1:
            continue
        else:
            return False
    return True

print(check_Consecutive([1,2,3,4,5])) # True
print(check_Consecutive([1,2,4,5,6])) # False
print(check_Consecutive([1,2,3,5,6])) # False
print(check_Consecutive([1,2,3,4,6])) # False
print(check_Consecutive([1,2,3,4,5,6])) # False
print(check_Consecutive([1,2,3,4,5,6,7])) # True
print(check_Consecutive([1,2,3,4,5,6,8])) # False
print(check_Consecutive([1,2,3,4,5,6,7,8])) # False
print(check_Consecutive([1,2,3,4,5,6,7,8,9])) # True
print(check_Consecutive([1,2,3,4,5,6,7,8,10]) # False

# Time Complexity: O(n)
# Space Complexity: O(1)

# Alternate Solution:
def check_Consecutive(lst):
    return all(lst[i+1]-lst[i] == 1 for i in range(len(lst)-1))

print(check_Consecutive([1,2,3,4,5])) # True
print(check_Consecutive([1,2,4,5,6])) # False
print(check_Consecutive([1,2,3,5,6])) # False
print(check_Consecutive([1,2,3,4,6]) # False
print(check_Consecutive([1,2,3,4,5,6]) # False
print(check_Consecutive([1,2,3,4,5,7]) # True
print(check_Consecutive([1,2,3,4,6,8]) # False
print(check_Consecutive([1,2,3,4,5,6,8]) # False
print(check_Consecutive([1,2,3,4,5,6,9]) # True
print(check_Consecutive([1,2,3,4,5,6,10]) # False