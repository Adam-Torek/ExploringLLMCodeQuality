"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def max_sub_array_sum(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    # TODO: Write your code here
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum and sum <= k:
                max_sum = sum
    return max_sum

def max_sub_array_sum_2(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    # TODO: Write your code here
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum and sum <= k:
                max_sum = sum
    return max_sum

def max_sub_array_sum_3(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    # TODO: Write your code here
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum and sum <= k:
                max_sum = sum
    return max_sum

def max_sub_array_sum_4(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    # TODO: Write your code here
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum and sum <= k:
                max_sum = sum
    return max_sum

def max_sub_array_sum_5(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    # TODO: Write your code here
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum and sum <= k:
                max_sum = sum
    return max_sum

def max_sub_array_sum_6(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    # TODO: Write your code here
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum and sum <= k:
                max_sum = sum
    return max_sum

def max_sub_array_sum_7(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    # TODO: Write your code here
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum and sum <= k:
                max_sum = sum
    return max_sum

def max_sub_array_sum_8(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    # TODO: Write your code here
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum and sum <= k:
                max_sum = sum
    return max_sum

def max_sub_array_sum_9(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: integer
    """
    # TODO: Write your code here
    max_sum = 0
    for i in range(len(arr)):
        sum =