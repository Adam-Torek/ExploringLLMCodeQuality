"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def max_sub_array_sum(numbers, target):
    """
    :param numbers: list of integers
    :param target: integer
    :return: integer
    """
    max_sum = 0
    current_sum = 0
    for num in numbers:
        current_sum = max(num, current_sum + num)
        if current_sum >= target:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
    return max_sum


if __name__ == '__main__':
    print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))