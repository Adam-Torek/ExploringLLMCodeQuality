"""
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
"""

def round_and_sum(numbers):
    total = 0
    for num in numbers:
        total += round(num)
    return total * len(numbers)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])) # should return 243

# Test cases
print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])) # should return 243
print(round_and_sum([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0])) # should return 100
print(round_and_sum([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1])) # should return 100
print(round_and_sum([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1, 11.2])) # should return 100
print(round_and_sum([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1, 11.2, 12.3])) # should return 100
print(round_and_sum([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1, 11.2, 12.3, 13.4])) # should return 100
print(round_and_sum([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1, 11.2, 12.3, 13.4, 14.5])) # should return 100
print(round_and_sum([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1, 11.2, 12.3, 13.4, 14.5, 15.6])) # should return 100
print(round_and_sum([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1, 11.2, 12.3, 13.4, 14.5, 15.6, 16.7])) # should return 100
print(round_and_sum([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1, 11.2, 12.3, 13.4, 14.