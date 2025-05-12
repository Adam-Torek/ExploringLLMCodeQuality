"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""


def all_unique(lst):
    return len(lst) == len(set(lst))


if __name__ == '__main__':
    print(all_unique([1, 2, 3]))
    print(all_unique([1, 2, 3, 1]))
    print(all_unique([1, 2, 3, 4]))
    print(all_unique([1, 2, 3, 4, 5]))
    print(all_unique([1, 2, 3, 4, 5, 6]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))
    print(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9,