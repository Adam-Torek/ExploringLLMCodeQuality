"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""

def even_position(lst):
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            return False
    return True

# Test cases
print(even_position([3,2,1])) # False
print(even_position([2,4,6])) # True
print(even_position([1,3,5])) # False