"""
Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""

def min_k(lst, k):
    return sorted(lst, key=lambda x: x[1])[:k]

assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 3) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 4) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 5) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 6) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 7) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 8) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 9) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 10) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 11) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 12) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 13) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]
assert min_k([('Manjeet', 10), ('