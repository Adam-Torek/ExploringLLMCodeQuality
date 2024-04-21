"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""

def count_first_elements(t):
    count = 0
    for i in range(len(t)):
        if isinstance(t[i], tuple):
            count += count_first_elements(t[i])
        else:
            break
    return count

assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3<|endoftext|>