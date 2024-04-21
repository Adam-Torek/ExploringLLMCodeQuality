"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""
def sum_of_digits(numbers):
    return sum(int(digit) for digit in str(numbers))

# Test the function
print(sum_of_digits([10,2,56])) # Output: 14<|endoftext|>