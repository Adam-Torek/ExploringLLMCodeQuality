def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    if k == 0:
        return []
    if k == 1:
        return [max(arr)]
    if k == len(arr):
        return sorted(arr)
    if k == 2:
        return sorted([max(arr), min(arr)])

    # find the median of the array
    median = find_median(arr)

    # divide the array into two parts
    left = [x for x in arr if x <= median]
    right = [x for x in arr if x > median]

    # calculate the number of elements in each part
    n_left = len(left)
    n_right = len(right)

    # calculate the number of elements in the left part that should be in the result
    k_left = k // 2
    k_right = k - k_left

    # calculate the number of elements in the right part that should be in the result
    if n_left > k_left:
        k_right = k_right + 1
    elif n_left < k_left:
        k_left = k_left - n_left

    # recursively find the maximum k_left elements in the left part
    left_max = maximum_k_numbers(left, k_left)

    # recursively find the maximum k_right elements in the right part
    right_max = maximum_k_numbers(right, k_right)

    # combine the two parts
    return left_max + right_max

def find_median(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]

def maximum_k_numbers(arr, k):
    if k == 0:
        return []
    if k == 1:
        return [max(arr)]
    if k == len(arr):
        return sorted(arr)
    if k == 2:
        return sorted([max(arr), min(arr)])

    # find the median of the array
    median = find_median(arr)

    # divide the array into two parts
    left = [x for x in arr if x <= median]
    right = [x for x in arr if x > median]

    # calculate the number of elements in each part
    n_left = len(left)
    n_right = len(right)

    # calculate the number of elements in the left part that should be in the result
    k_left = k // 2
    k_right = k - k_left

    # calculate the number of elements in the right part that should be in the result
    if n_left > k_left:
        k_right = k_right + 1
    elif n_left < k_left:
        k_left = k_left - n_left

    # recursively find the maximum k_left elements in the left part
    left_max = maximum_k_numbers(left, k_left)

    # recursively find the maximum k_right elements in the right part
    right_max = maximum_k_numbers(right, k_right)

    # combine the two parts
    return left