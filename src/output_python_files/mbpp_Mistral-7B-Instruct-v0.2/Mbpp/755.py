"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""
def second_smallest(numbers):
    """
    :param numbers: list of numbers
    :return: second smallest number in the list
    """
    if len(numbers) < 2:
        raise ValueError("List should have at least 2 elements")

    smallest = min(numbers)
    second_smallest = None

    for number in numbers:
        if number < smallest and second_smallest is None:
            second_smallest = smallest
            smallest = number
        elif number < smallest and second_smallest is not None:
            second_smallest = number

    if second_smallest is None:
        raise ValueError("There is no second smallest number in the list")

    return second_smallest

if __name__ == "__main__":
    assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
    assert second_smallest([1, 2, 3, 4, 5]) == 2
    assert second_smallest([1, 2, 3]) == 1
    assert second_smallest([-2, -2, -2]) == -2
    assert second_smallest([-2, -2, -1]) == -2
    assert second_smallest([-2, -2]) = None
    assert second_smallest([]) = None
    assert second_smallest([-1]) = None
    assert second_smallest([-1, 0]) = 0
    assert second_smallest([0, 0]) = 0
    assert second_smallest([0, 0, 0]) = 0
    assert second_smallest([1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 1
    assert second_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,