"""
Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""

def min_k(lst, k):
    return sorted(lst, key=lambda x: x[1])[:k]

# Test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
assert min_k([('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Manjeet', 10)], 2) == [('Akash', 2), ('Akshat', 4)]
assert min_k([('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Manjeet', 10), ('Komal', 5)], 3) == [('Akash', 2), ('Akshat', 4), ('Nikhil', 8)]
assert min_k([('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Manjeet', 10), ('Komal', 5), ('Rohit', 3)], 3) == [('Akash', 2), ('Akshat', 4), ('Nikhil', 8)]
assert min_k([('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Manjeet', 10), ('Komal', 5), ('Rohit', 3), ('Sunny', 1)], 3) == [('Akash', 2), ('Sunny', 1), ('Akshat', 4)]
assert min_k([('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Manjeet', 10), ('Komal', 5), ('Rohit', 3), ('Sunny', 1), ('Kamal', 6)], 3) == [('Akash', 2), ('Sunny', 1), ('Kamal', 6)]
assert min_k([('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Manjeet', 10), ('Komal', 5), ('Rohit', 3), ('Sunny', 1), ('Kamal', 6), ('Priya', 7)], 3) == [('Akash', 2), ('Sunny', 1), ('Kamal', 6)]
assert min_k([('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Manjeet', 10), ('Komal', 5), ('Rohit', 3), ('Sunny', 1), ('Kamal', 6), ('Priya', 7), ('Kavya', 9)], 4) == [('Akash', 2), ('Sunny', 1), ('Kamal', 6), ('Priya', 7)]
assert min_k([('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Manjeet', 10), ('Komal', 5), ('Rohit', 3), ('Sunny', 1), ('Kamal', 6), ('Priya', 7), ('Kavya', 9), ('Kanika', 10)], 4) == [('Akash', 2), ('Sunny', 1), ('Kamal', 6), ('Kavya', 9)]
assert