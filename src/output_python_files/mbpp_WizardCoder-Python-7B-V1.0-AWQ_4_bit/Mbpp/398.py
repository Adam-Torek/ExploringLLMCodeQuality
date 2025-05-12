"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""

def sum_of_digits(lst):
    total = 0
    for num in lst:
        while num > 0:
            total += num % 10
            num //= 10
    return total

print(sum_of_digits([10,2,56])) # Output: 14
print(sum_of_digits([123,456,789])) # Output: 24
print(sum_of_digits([12345,67890])) # Output: 23