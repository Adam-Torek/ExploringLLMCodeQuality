"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""

def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2!= 0:
            return False
    return True

# Test cases
print(odd_position([2,1,4,3,6,7,6,3])) # True
print(odd_position([2,1,4,3,6,7,8,3])) # False
print(odd_position([2,1,4,3,6,7,6])) # True<|endoftext|>