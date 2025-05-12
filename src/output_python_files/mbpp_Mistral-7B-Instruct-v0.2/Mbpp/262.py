"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
"""
def split_two_parts(lst, L):
    """
    Splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.

    :param lst: list
    :param L: int
    :return: tuple
    """
    if len(lst) < L:
        return ("Error: List too short", [])
    return (lst[:L], lst[L:])