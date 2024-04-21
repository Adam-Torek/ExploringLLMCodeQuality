"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""
def count_Occurrence(lst, tup):
    count = 0
    for i in lst:
        if i in tup:
            count += 1
    return count

# Test the function
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']) == 3<|endoftext|>