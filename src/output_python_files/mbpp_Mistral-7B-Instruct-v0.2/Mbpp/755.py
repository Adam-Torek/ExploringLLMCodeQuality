"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""
def second_smallest(numbers):
    """
    :param numbers: list of numbers
    :return: second smallest number in the list
    """
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("List must have at least 2 elements")
    return numbers[1]

if __name__ == "__main__":
    assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
    assert second_smallest([1, 2, 3, 4, 5]) == 2
    assert second_smallest([-2, -1, 0]) == 0
    assert second_smallest([-2, -1]) == -1
    assert second_smallest([-2]) == TracebackError("List must have at least 2 elements")