"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""

def count_integer(lst):
    count = 0
    for item in lst:
        if isinstance(item, int):
            count += 1
    return count

# Test cases
assert count_integer([1,2,'abc',1.2]) == 2<|endoftext|>