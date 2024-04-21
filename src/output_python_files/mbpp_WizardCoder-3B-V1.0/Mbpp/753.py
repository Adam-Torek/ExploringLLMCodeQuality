"""
Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""

def min_k(lst, k):
    """
    This function takes a list of tuples and an integer k as input and returns a list of tuples containing the k smallest elements from the list.
    """
    lst.sort(key=lambda x: x[1])
    return lst[:k]

# Test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 3) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 4) == [('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]<|endoftext|>