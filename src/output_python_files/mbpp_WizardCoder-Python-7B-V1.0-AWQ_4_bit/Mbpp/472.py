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

# Test cases
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
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10]) # False
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11]) # True
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12]) # False
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13]) # True
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) # False
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # True
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) # False
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) # True
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) # False
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) # True
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) # False
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) # True
print(check_Consecutive([1,2,3,4,5,6,7,8,9,10,