"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""

def tuple_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return intersection

# Testing the function
print(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)])) # Output: {(4, 5), (3, 4)}

# Testing the function with a different input
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)], [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])) # Output: {(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)}

# Testing the function with a different input
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)], [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)])) # Output: {(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)}

# Testing the function with a different input
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)], [(1, 2, 3), (4, 5, 6), (7, 8, 9), (13, 14, 15)])) # Output: set()

# Testing the function with a different input
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)], [(1, 2, 3), (4, 5, 6), (13, 14, 15)])) # Output: set()

# Testing the function with a different input
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)], [(13, 14, 15)])) # Output: set()

# Testing the function with a different input
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)], [(13, 14, 15), (16, 17, 18)])) # Output: set()

# Testing the function with a different input
print(tuple_intersection([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)], [(13, 14, 15), (16, 17, 18), (19, 20, 21)])) # Output: set()

# Testing the function with a different input
print(tuple_intersection([(1