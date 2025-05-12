"""
Write a function to compute the n-th power of each number in a list.
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def nth_nums(lst, n):
    """
    Compute the n-th power of each number in a list.
    """
    return [i**n for i in lst]


if __name__ == '__main__':
    print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))