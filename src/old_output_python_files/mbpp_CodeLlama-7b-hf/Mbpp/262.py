"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
"""

def split_two_parts(lst, L):
    """
    lst: list
    L: int
    returns: tuple
    """
    # Your code here
    return lst[:L], lst[L:]


def test_split_two_parts():
    assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
    assert split_two_parts([1,1,2,3,4,4,5,1],4)==([1, 1, 2, 3], [4, 4, 5, 1])
    assert split_two_parts([1,1,2,3,4,4,5,1],5)==([1, 1, 2, 3, 4], [4, 4, 5, 1])
    assert split_two_parts([1,1,2,3,4,4,5,1],6)==([1, 1, 2, 3, 4, 4], [5, 1])
    assert split_two_parts([1,1,2,3,4,4,5,1],7)==([1, 1, 2, 3, 4, 4, 5], [1])
    assert split_two_parts([1,1,2,3,4,4,5,1],8)==([1, 1, 2, 3, 4, 4, 5, 1], [])
    assert split_two_parts([1,1,2,3,4,4,5,1],9)==([1, 1, 2, 3, 4, 4, 5, 1], [])
    assert split_two_parts([1,1,2,3,4,4,5,1],10)==([1, 1, 2, 3, 4, 4, 5, 1], [])
    assert split_two_parts([1,1,2,3,4,4,5,1],11)==([1, 1, 2, 3, 4, 4, 5, 1], [])
    assert split_two_parts([1,1,2,3,4,4,5,1],12)==([1, 1, 2, 3, 4, 4, 5, 1], [])
    assert split_two_parts([1,1,2,3,4,4,5,1],13)==([1, 1, 2, 3, 4, 4, 5, 1], [])
    assert split_two_parts([1,1,2,3,4,4,5,1],14)==([1, 1, 2, 3, 4, 4, 5, 1], [])
    assert split_two_parts([1,1,2,3,4,4,5,1],15)==([1, 1, 2, 3, 4, 4, 5, 1], [])
    assert split_two_parts([1,1,2,3,4,4,5,1],16)==([1, 1, 2, 3, 4, 4, 5, 1], [])
    assert split_two_parts([1,1,2,3,4,4,5,1],17)==([1, 1, 2, 3, 4, 4, 5, 1], [])
    assert split_two_parts([1,1,2,3,4,4,5,1],18)==([1, 1, 2, 3, 4, 4, 5,