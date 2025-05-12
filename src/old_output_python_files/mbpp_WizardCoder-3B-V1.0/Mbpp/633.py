"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""

def pair_xor_Sum(lst, n):
    xor_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            xor_sum += lst[i] ^ lst[j]
    return xor_sum

# Test case
assert pair_xor_Sum([5,9,7,6],4) == 47<|endoftext|>