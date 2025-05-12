"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""

def check_Consecutive(lst):
    for i in range(len(lst)-1):
        if lst[i] + 1!= lst[i+1]:
            return False
    return True

assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,2,3,4,6]) == False
assert check_Consecutive([1,2,3,4,5,6]) == True
assert check_Consecutive([1,2,3,4,5,7]) == False
assert check_Consecutive([1,2,3,4,5,6,7]) == True
assert check_Consecutive([1,2,3,4,5,6,8]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8]) == True
assert check_Consecutive([1,2,3,4,5,6,7,9]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,10]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,11]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,11]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,12]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,13]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,14]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,15]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18]) == False
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12