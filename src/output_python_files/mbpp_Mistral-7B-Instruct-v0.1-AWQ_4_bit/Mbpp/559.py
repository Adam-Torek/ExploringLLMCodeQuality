"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def max_sub_array_sum(numbers, k):
    """
    :param numbers: list of integers
    :param k: sum of sublist
    :return: sum of largest contiguous sublist
    """
    if not numbers:
        return 0
    max_sum = numbers[0]
    current_sum = numbers[0]
    for i in range(1, len(numbers)):
        current_sum = max(numbers[i], current_sum + numbers[i])
        if current_sum >= k:
            max_sum = max(max_sum, current_sum)
            current_sum = numbers[i]
    return max_sum


if __name__ == '__main__':
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7