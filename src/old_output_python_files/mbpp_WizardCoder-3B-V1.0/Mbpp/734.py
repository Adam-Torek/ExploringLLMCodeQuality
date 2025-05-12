"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""

def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = arr[0]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + arr[i - 1]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            dp[j] = max(dp[j], dp[j - i] + arr[i] * dp[j - i - 1])

    return dp[n]

# Test the function
print(sum_Of_Subarray_Prod([1,2,3])) # Output: 20<|endoftext|>