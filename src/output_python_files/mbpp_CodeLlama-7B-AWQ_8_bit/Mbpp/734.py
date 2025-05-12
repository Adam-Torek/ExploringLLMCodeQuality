"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""


def sum_Of_Subarray_Prod(arr):
    """
    :param arr: list of integers
    :return: sum of products of all possible sublists of a given list
    """
    if not arr:
        return 0
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = dp[i - 1] * arr[i]
    ans = dp[n - 1]
    for i in range(n - 1):
        ans += dp[i] * dp[n - 1 - i]
    return ans


if __name__ == '__main__':
    print(sum_Of_Subarray_Prod([1, 2, 3]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(sum_Of_Subarray_