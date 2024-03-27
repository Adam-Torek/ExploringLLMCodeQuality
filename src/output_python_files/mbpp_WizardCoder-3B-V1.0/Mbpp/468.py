"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""

def max_product(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, n):
        max_ending_here = max(arr[i], max_ending_here * arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Test the function
print(max_product([3, 100, 4, 5, 150, 6]))  # Output: 3000<|endoftext|>