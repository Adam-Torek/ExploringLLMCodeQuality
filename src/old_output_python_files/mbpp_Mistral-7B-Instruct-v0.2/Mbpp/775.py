"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""
def odd_position(lst):
    for i in range(len(lst)):
        if i % 2 != 0 and len(list(filter(lambda x: x % 2 != 0, lst[i:]))) % 2 != 0:
            continue
        else:
            return False
    return True

# Test case
assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([1,2,3,4,5,6,7,8]) == True
assert odd_position([1,2,3,4,5,6,7,9]) == True
assert odd_position([1,2,3,4,5,6,6,3]) == False
assert odd_position([1,2,3,4,5,6,7,0]) == False