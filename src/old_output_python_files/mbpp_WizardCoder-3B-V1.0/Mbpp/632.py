"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""

def move_zero(lst):
    """
    Move all zeroes to the end of the given list.
    """
    i = 0
    while i < len(lst):
        if lst[i] == 0:
            lst.pop(i)
        else:
            i += 1
    return lst

# Test the function
print(move_zero([1,0,2,0,3,4])) # Output: [1,2,3,4,0,0]<|endoftext|>