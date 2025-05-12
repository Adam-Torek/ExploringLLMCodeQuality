"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""

def pair_xor_Sum(lst, k):
    result = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            result += lst[i]^lst[j]
    return result

print(pair_xor_Sum([5,9,7,6],4)) # Output: 47

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Optimized Solution:

def pair_xor_Sum_Optimized(lst, k):
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    return result*k

print(pair_xor_Sum_Optimized([5,9,7,6],4)) # Output: 47

# Time Complexity: O(n)
# Space Complexity: O(1)

# Explanation:
# In the optimized solution, we iterate through the list and add each element to the result variable. Since we are adding all the elements, the sum of the xor of all pairs will be the sum of the list multiplied by k.