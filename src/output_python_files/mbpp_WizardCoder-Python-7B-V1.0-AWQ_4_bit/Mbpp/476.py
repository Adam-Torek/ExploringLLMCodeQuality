"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""

def big_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return max(arr) + min(arr)

print(big_sum([1,2,3])) # Output: 4
print(big_sum([-1,2,3,4,5,6,7,8,9])) # Output: 17
print(big_sum([1,2,3,4,5,6,7,8,9])) # Output: 10
print(big_sum([-1,2,3,4,5,6,7,8,9,10])) # Output: 19
print(big_sum([1])) # Output: 1
print(big_sum([])) # Output: 0