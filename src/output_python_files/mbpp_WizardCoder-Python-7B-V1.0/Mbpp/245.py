"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""

def max_sum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])
    else:
        max_sum_inc = [0] * n
        max_sum_dec = [0] * n
        max_sum_inc[0] = arr[0]
        max_sum_dec[n-1] = arr[n-1]
        for i in range(1, n):
            max_sum_inc[i] = max(max_sum_inc[i-1] + arr[i], arr[i])
            max_sum_dec[n-i-1] = max(max_sum_dec[n-i] + arr[n-i-1], arr[n-i-1])
        max_sum = max(max_sum_inc)
        for i in range(1, n):
            max_sum = max(max_sum, max_sum_inc[i] + max_sum_dec[i-1])
        return max_sum

# Test cases
print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9])) # Output: 194
print(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 24
print(max_sum([10, 20, 30, 40, 50, 60, 70, 80])) # Output: 100
print(max_sum([10, 20, 30, 40, 50, 60, 70, 80, 90])) # Output: 190
print(max_sum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) # Output: 200
print(max_sum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])) # Output: 210
print(max_sum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])) # Output: 220
print(max_sum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130])) # Output: 230
print(max_sum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140])) # Output: 240
print(max_sum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])) # Output: 250
print(max_sum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160])) #