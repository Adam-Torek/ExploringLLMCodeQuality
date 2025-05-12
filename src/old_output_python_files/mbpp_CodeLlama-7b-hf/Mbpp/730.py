"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""


def consecutive_duplicates(lst):
    """
    :param lst: list
    :return: list
    """
    if not lst:
        return []
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        if lst[0] == lst[1]:
            return lst
        else:
            return lst
    if len(lst) > 2:
        if lst[0] == lst[1]:
            return consecutive_duplicates(lst[2:])
        else:
            return [lst[0]] + consecutive_duplicates(lst[1:])


if __name__ == '__main__':
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 4]))
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 4, 4]))
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 4, 4, 4]))
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 4, 4, 4, 4]))
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 4, 4, 4, 4, 4]))
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 4, 4, 4, 4, 4, 4]))
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 4, 4, 4, 4, 4, 4, 4]))
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]))
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]))
    print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6,