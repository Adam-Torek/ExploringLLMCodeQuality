"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""

def count_Occurrence(tup, lst):
    count = 0
    for i in tup:
        if i in lst:
            count += 1
    return count

print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'])) # Output: 3
print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'c'])) # Output: 2
print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['b', 'c'])) # Output: 2
print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['e', 'f'])) # Output: 0

# Note: The function should return 0 if the element is not present in the tuple.