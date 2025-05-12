"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""

def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True

print(even_position([3,2,1])) # False
print(even_position([4,2,6,8,1])) # True
print(even_position([1,2,3,4,6,8])) # False
print(even_position([4,2,6,8,10])) # True
print(even_position([1,3,5,7,9])) # True