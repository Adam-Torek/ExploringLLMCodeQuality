"""
Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""

def min_k(lst, k):
    """
    :type lst: List[Tuple[str, int]]
    :type k: int
    :rtype: List[Tuple[str, int]]
    """
    if k > len(lst):
        return []
    else:
        return sorted(lst, key=lambda x: x[1])[:k]


if __name__ == '__main__':
    print(min_k(["('Manjeet', 10)", "('Akshat', 4)", "('Akash', 2)", "('Nikhil', 8)"], 2))