"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""
def move_zero(numbers):
    """
    Function to move all zeroes to the end of the given list
    :param numbers: list of numbers
    :return: list with all zeroes at the end
    """
    index = 0
    while index < len(numbers):
        if numbers[index] != 0:
            numbers[index], numbers[0] = numbers[0], numbers[index]
            index += 1
        else:
            index += 1
            numbers.pop()
    return numbers

if __name__ == "__main__":
    assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
    assert move_zero([0,0,0,0,0,0]) == [0]
    assert move_zero([1,2,3,4]) == [1,2,3,4]
    assert move_zero([]) == []
    assert move_zero([0]) == [0]
    assert move_zero([-1,0,1]) == [-1,1,0]
    assert move_zero([1,0,1,0,1,0]) == [1,1,1,0,0,0]
    assert move_zero([1,0,1,0,1,0,0]) == [1,1,1,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0]) == [1,1,1,0,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0,0]) == [1,1,1,0,0,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0,0,0]) == [1,1,1,0,0,0,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0,0,0,0]) == [1,1,1,0,0,0,0,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0,0,0,0,0]) == [1,1,1,0,0,0,0,0,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0,0,0,0,0,0]) == [1,1,1,0,0,0,0,0,0,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0,0,0,0,0,0,0]) == [1,1,1,0,0,0,0,0,0,0,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0,0,0,0,0,0,0,0]) == [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0]) == [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]) == [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    assert move_zero([1,0,1,0,1,0,0,0,