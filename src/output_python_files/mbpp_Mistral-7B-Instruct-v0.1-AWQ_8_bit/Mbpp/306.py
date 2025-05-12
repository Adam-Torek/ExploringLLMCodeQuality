"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""

def max_sum_increasing_subseq(arr, i, k, n):
    """
    :param arr: list of integers
    :param i: index of prefix
    :param k: index of kth element
    :param n: length of array
    :return: max sum of increasing subsequence
    """
    if i == k:
        return arr[i]
    elif k > i:
        return max(arr[i], max_sum_increasing_subseq(arr, i, k, n))
    else:
        return max(arr[i], max_sum_increasing_subseq(arr, i, k, n) + arr[k])


if __name__ == '__main__':
    arr = [1, 101, 2, 3, 100, 4, 5]
    i = 7
    k = 4
    n = len(arr)
    print(max_sum_increasing_subseq(arr, i, k, n))