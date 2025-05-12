"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""


def even_position(lst):
    """
    :param lst: list
    :return: bool
    """
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True


if __name__ == '__main__':
    print(even_position([3, 2, 1]))
    print(even_position([3, 2, 4]))
    print(even_position([3, 2, 4, 6]))
    print(even_position([3, 2, 4, 6, 8]))
    print(even_position([3, 2, 4, 6, 8, 10]))
    print(even_position([3, 2, 4, 6, 8, 10, 12]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]))
    print(even_position([3, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]))
    print(even_position([3, 2, 4, 6, 8,