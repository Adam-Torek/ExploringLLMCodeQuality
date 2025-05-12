"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""

def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True

assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([2,1,4,3,6,7,6,4]) == False
assert odd_position([2,1,4,3,6,7,6,5]) == False
assert odd_position([2,1,4,3,6,7,6,7]) == False
assert odd_position([2,1,4,3,6,7,6,9]) == True
assert odd_position([2,1,4,3,6,7,6,1]) == False
assert odd_position([2,1,4,3,6,7,6,2]) == False
assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([2,1,4,3,6,7,6,5]) == False
assert odd_position([2,1,4,3,6,7,6,7]) == False
assert odd_position([2,1,4,3,6,7,6,9]) == True
assert odd_position([2,1,4,3,6,7,6,1]) == False
assert odd_position([2,1,4,3,6,7,6,2]) == False
assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([2,1,4,3,6,7,6,5]) == False
assert odd_position([2,1,4,3,6,7,6,7]) == False
assert odd_position([2,1,4,3,6,7,6,9]) == True
assert odd_position([2,1,4,3,6,7,6,1]) == False
assert odd_position([2,1,4,3,6,7,6,2]) == False
assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([2,1,4,3,6,7,6,5]) == False
assert odd_position([2,1,4,3,6,7,6,7]) == False
assert odd_position([2,1,4,3,6,7,6,9]) == True
assert odd_position([2,1,4,3,6,7,6,1]) == False
assert odd_position([2,1,4,3,6,7,6,2]) == False
assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([2,1,4,3,6,7,6,5]) == False
assert odd_position([2,1,4,3,6,7,6,7]) == False
assert odd_position([2,1,4,3,6,7,6,9]) == True
assert odd_position([2,1,4,3,6,7,6,1]) == False
assert odd_position([2,1,4,3,6,7,6,2]) == False
assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([2,1,4,3,6,7,6,5]) == False
assert odd_position([2,1,4,3,6,7,6,7]) == False
assert odd_position([2,1,4,3,6,7,6,9]) == True
assert odd_position([2,1,4,3,6