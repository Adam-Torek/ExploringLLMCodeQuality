"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""

def max_sum_increasing_subseq(arr, k, i, dp):
    """
    Helper function to find the maximum sum of increasing subsequence from prefix until i and also including kth element
    :param arr: list of integers
    :param k: index of kth element
    :param i: index of current element
    :param dp: memoization table
    :return: maximum sum of increasing subsequence from prefix until i and also including kth element
    """
    if i > k:
        return dp[k]

    if dp[i] > dp[k] + arr[i]:
        dp[i] = dp[k] + arr[i]

    dp[i] = max(dp[i], dp[i - 1])
    dp[i] = max(dp[i], dp[k] + arr[i])

    return dp[i]

def max_sum_increasing_subseq_prefix(arr, k):
    """
    Function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element
    :param arr: list of integers
    :param k: index of kth element
    :return: maximum sum of increasing subsequence from prefix until ith index and also including kth element
    """
    n = len(arr)
    dp = [0] * (n + 1)

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 1] + arr[i])

    return max_sum_increasing_subseq(arr, k, i, dp)

if __name__ == "__main__":
    arr = [1, 101, 2, 3, 100, 4, 5]
    k = 4
    i = 6
    print(max_sum_increasing_subseq_prefix(arr, k))</s>