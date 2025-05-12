"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""

def second_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        return sorted(lst)[1]

# Test the function
print(second_smallest([1, 2, -8, -2, 0, -2])) # Output: -2<|endoftext|>