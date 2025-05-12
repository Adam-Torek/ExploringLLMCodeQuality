"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""

def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True

print(odd_position([2,1,4,3,6,7,6,3])) # True
print(odd_position([2,1,4,3,6,8,3])) # False
print(odd_position([1,3,5,7,9,11,13])) # True
print(odd_position([1,3,5,7,9,10,12])) # False
print(odd_position([1,3,5,7,9,11,13,15])) # False
print(odd_position([1,3,5,7,9,11,13,15,17])) # True
print(odd_position([1,3,5,7,9,11,13,15,17,19])) # True
print(odd_position([1,3,5,7,9,11,13,15,17,20])) # False

# Time Complexity: O(n)
# Space Complexity: O(1)