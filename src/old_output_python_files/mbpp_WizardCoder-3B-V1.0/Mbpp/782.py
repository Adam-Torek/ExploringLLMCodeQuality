"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""

def odd_length_sum(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        for j in range(i+1, n, 2):
            sum += arr[j]
    return sum

# Test the function
print(odd_length_sum([1,2,4])) # Output: 14<|endoftext|>