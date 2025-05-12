"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""

def sum_of_digits(lst):
    result = []
    for num in lst:
        sum = 0
        for digit in str(num):
            sum += int(digit)
        result.append(sum)
    return result

print(sum_of_digits([10,2,56])) # Output: [1, 2, 11]
print(sum_of_digits([123,456,789])) # Output: [6, 15, 24]
print(sum_of_digits([12345,67890])) # Output: [15, 23]