"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""
def sum_negativenum(lst):
    return sum(num for num in lst if num < 0)

# Test the function with the given example
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32<|endoftext|>