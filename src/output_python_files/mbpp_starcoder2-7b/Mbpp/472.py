"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""

def check_Consecutive(list):
    for i in range(len(list)-1):
        if list[i+1] - list[i]!= 1:
            return False
    return True

assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,2,3,4,6]) == False
assert check_Consecutive([1,2,3,4,5,6]) == False
assert check_Consecutive([1,2,3,4,5,6,7]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,