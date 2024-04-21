"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""

def pos_count(lst):
    count = 0
    for num in lst:
        if num > 0:
            count += 1
    return count

# Test the function
print(pos_count([1,-2,3,-4])) # Output: 2<|endoftext|>