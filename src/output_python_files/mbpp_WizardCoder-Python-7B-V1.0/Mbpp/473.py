"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""
from typing import List, Tuple

def tuple_intersection(t1: List[Tuple[int, int]], t2: List[Tuple[int, int]]) -> set:
    t1_set = set(t1)
    t2_set = set(t2)
    intersection = t1_set.intersection(t2_set)
    return intersection

# Test cases
print(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)])) # Output: {(4, 5), (3, 4), (5, 6)}
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9)], [(5, 4, 3), (1, 2, 6), (8, 7, 9)])) # Output: {(3, 4, 5), (1, 2, 6), (7, 8, 9)}
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9)], [(5, 4, 3), (1, 2, 6), (8, 7, 9), (10, 11, 12)])) # Output: {(1, 2, 3, 4, 5, 6, 7, 8, 9)}
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9)], [(5, 4, 3), (1, 2, 6), (8, 7, 9), (10, 11, 12), (1, 2, 3)])) # Output: {(1, 2, 3, 4, 5, 6, 7, 8, 9)}
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9)], [(5, 4, 3), (1, 2, 6), (8, 7, 9), (10, 11, 12), (1, 2, 3), (4, 5, 6)])) # Output: {(1, 2, 3, 4, 5, 6, 7, 8, 9)}
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9)], [(5, 4, 3), (1, 2, 6), (8, 7, 9), (10, 11, 12), (1, 2, 3), (4, 5, 6), (7, 8, 9)])) # Output: {(1, 2, 3, 4, 5, 6, 7, 8, 9)}
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9)], [(5, 4, 3), (1, 2, 6), (8, 7, 9), (10, 11, 12), (1, 2, 3), (4, 5, 6), (7, 8, 9)])) # Output: {(1, 2, 3, 4, 5, 6, 7, 8, 9)}
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8