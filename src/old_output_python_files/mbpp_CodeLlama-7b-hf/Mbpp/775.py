"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""


def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True


if __name__ == '__main__':
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(odd_position([2, 1, 4, 3, 6, 7, 6, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1