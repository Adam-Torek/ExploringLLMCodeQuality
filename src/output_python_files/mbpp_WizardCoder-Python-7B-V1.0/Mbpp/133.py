"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""

def sum_negativenum(numbers):
    sum = 0
    for num in numbers:
        if num < 0:
            sum += num
    return sum

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])) # Output: -32