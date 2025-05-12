"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""

def count_Occurrence(tup,lst):
    count = 0
    for i in lst:
        count += tup.count(i)
    return count

print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'])) # Output: 3