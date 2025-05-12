"""
Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""

def min_k(lst, k):
    return sorted(lst, key=lambda x: x[1])[:k]

# Test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 10), ('F', 5), ('G', 3)], 3) == [('C', 2), ('B', 4), ('F', 5)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 10), ('F', 5), ('G', 3)], 4) == [('C', 2), ('B', 4), ('F', 5), ('A', 10)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 10), ('F', 5), ('G', 3)], 5) == [('C', 2), ('B', 4), ('F', 5), ('A', 10), ('E', 10)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 10), ('F', 5), ('G', 3)], 6) == [('C', 2), ('B', 4), ('F', 5), ('A', 10), ('E', 10), ('D', 8)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 10), ('F', 5), ('G', 3)], 1) == [('A', 10]