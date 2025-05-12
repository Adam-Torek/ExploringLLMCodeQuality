"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""

def second_smallest(nums):
    """
    :param nums: list of numbers
    :return: second smallest number
    """
    # TODO: implement this function
    return None


def test_second_smallest():
    assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
    assert second_smallest([1, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert second_smallest([1, 2, 2, 2, 2, 2, 2, 2, 2, 2,