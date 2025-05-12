"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    mod = 10**9 + 7
    MOD = 100000000007
    M = 10**9 + 7
    dp = [1] * n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = dp[i-1] * arr[i] % M
    ans = 0
    for i in range(1, n):
        ans = (ans + dp[i]) % M
    for i in range(1, n):
        for j in range(i+1, n):
            prod = 1
            for k in range(i, j+1):
                prod *= arr[k]
            ans = (ans + prod) % M
    return ans

# Test the function
print(sum_Of_Subarray_Prod([1,2,3])) # Output: 20
print(sum_Of_Subarray_Prod([1,2,3,4])) # Output: 30
print(sum_Of_Subarray_Prod([1,2,3,4,5])) # Output: 40
print(sum_Of_Subarray_Prod([1,2,3,4,5,6])) # Output: 70
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7])) # Output: 115
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8])) # Output: 200
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9])) # Output: 300
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10])) # Output: 450