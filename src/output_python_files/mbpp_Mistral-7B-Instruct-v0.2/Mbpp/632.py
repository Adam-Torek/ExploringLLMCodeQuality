"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""
def move_zero(numbers):
    """
    Function to move all zeroes to the end of the given list.
    :param numbers: list of numbers
    :return: list with all zeroes at the end
    """
    # Initialize two pointers, i and j
    i = 0
    j = len(numbers) - 1

    # While i is less than j
    while i < j:
        # If the number at index i is zero
        if numbers[i] == 0:
            # Swap the number at index i with the number at index j
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # Decrement j to move to the next zero
            j -= 1
        # Increment i to move to the next number
        i += 1

    return numbers

# Test the function
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
assert move_zero([0,1,2,0,3,4]) == [1,2,3,4,0,0]
assert move_zero([0,0,1,2,3,4]) == [1,2,3,4,0,0]
assert move_zero([]) == []
assert move_zero([5,5,5]) == [5,5,5]</s>