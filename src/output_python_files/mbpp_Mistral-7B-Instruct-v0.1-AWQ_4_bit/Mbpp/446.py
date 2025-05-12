"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""

def count_Occurrence(tuple_list, list_to_count):
    count = 0
    for item in list_to_count:
        count += tuple_list.count(item)
    return count

assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3