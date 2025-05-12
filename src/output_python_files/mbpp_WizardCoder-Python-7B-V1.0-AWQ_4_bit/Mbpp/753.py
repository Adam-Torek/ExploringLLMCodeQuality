"""
Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""

def min_k(lst, k):
    return sorted(lst, key=lambda x: x[1])[:k]

# Test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8)], 2) == [('C', 2), ('B', 4)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 5), ('F', 3)], 3) == [('C', 2), ('B', 4), ('A', 10)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 5), ('F', 3), ('G', 6)], 4) == [('C', 2), ('B', 4), ('A', 10), ('F', 3)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 5), ('F', 3), ('G', 6), ('H', 7)], 5) == [('C', 2), ('B', 4), ('A', 10), ('F', 3), ('E', 5)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 5), ('F', 3), ('G', 6), ('H', 7), ('I', 9)], 6) == [('C', 2), ('B', 4), ('A', 10), ('F', 3), ('E', 5), ('H', 7)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 5), ('F', 3), ('G', 6), ('H', 7), ('I', 9), ('J', 1)], 7) == [('C', 2), ('B', 4), ('A', 10), ('F', 3), ('E', 5), ('H', 7), ('J', 1)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 5), ('F', 3), ('G', 6), ('H', 7), ('I', 9), ('J', 1), ('K', 0)], 8) == [('C', 2), ('B', 4), ('A', 10), ('F', 3), ('E', 5), ('H', 7), ('J', 1), ('K', 0)]
assert min_k([('A', 10), ('B', 4), ('C', 2), ('D', 8), ('E', 5), ('F', 3), ('G', 6), ('H', 7), ('I', 9), ('J', 1), ('K', 0), ('L', 10)], 9) == [('C', 2), ('B', 4), ('A', 10), ('F', 3), ('E', 5), ('H', 7), ('J', 1), ('K', 0), ('L', 10)]
assert min_k([('A', 10), ('B', 4), ('