"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""

def find_literals(string, pattern):
    """
    >>> find_literals('The quick brown fox jumps over the lazy dog.', 'fox')
    ('fox', 16, 19)
    """
    start = 0
    end = 0
    while start < len(string):
        end = string.find(pattern, start)
        if end == -1:
            return None
        else:
            return (pattern, start, end)
        start += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt1/python_fundamentals_pt1.py
"""
Python Fundamentals

Part 1

"""

# 1.
def print_list(list):
    """
    >>> print_list([1, 2, 3, 4, 5])
    1 2 3 4 5
    """
    for i in list:
        print i,

# 2.
def print_list_reverse(list):
    """
    >>> print_list_reverse([1, 2, 3, 4, 5])
    5 4 3 2 1
    """
    for i in reversed(list):
        print i,

# 3.
def print_list_length(list):
    """
    >>> print_list_length([1, 2, 3, 4, 5])
    5
    """
    print len(list)

# 4.
def print_list_max(list):
    """
    >>> print_list_max([1, 2, 3, 4, 5])
    5
    """
    print max(list)

# 5.
def print_list_min(list):
    """
    >>> print_list_min([1, 2, 3, 4, 5])
    1
    """
    print min(list)

# 6.
def print_list_sum(list):
    """
    >>> print_list_sum([1, 2, 3, 4, 5])
    15
    """
    print sum(list)

# 7.
def print_list_avg(list):
    """
    >>> print_list_avg([1, 2, 3, 4, 5])
    3.0
    """
    print float(sum(list)) / len(list)

# 8.
def print_list_median(list):
    """
    >>> print_list_median([1, 2, 3, 4, 5])
    3.0
    """
    list.sort()
    if len(list) % 2 == 0:
        print float(list[len(list) / 2] + list[len(list) / 2 - 1]) / 2
    else:
        print list[len(list) / 2]

# 9.
def print_list_mode(list):
    """
    >>> print_list_mode([1, 2, 3, 4, 5])
    1
    """
    list.sort()
    count = 0
    mode = 0
    for i in list:
        if list.count(i) > count:
            count = list.count(i)
            mode = i
    print mode

# 10.
def print_list_range(list):
    """
    >>> print_list_range([1, 2, 3, 4, 5])
    4
    """
    print max(list) - min(list)

# 11.
def print_list_variance(list):
    """
    >>> print_list_variance([1, 2, 3, 4, 5])
    2.0
    """
    list.sort()
    mean = float(sum(list)) / len(list)
    variance = 0
    for i in list:
        variance += (i - mean) ** 2
    print variance / len(list)

# 12.
def print_list_std_dev(list):
    """
    >>> print_list_std_dev([1, 2, 3, 4, 5])
    1.4142135623