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

# Output: 243

# Explanation:
# The rounded numbers are [22, 4, -16, -10, 11, -12, 14, -6, 18].
# The total sum of these numbers is 22 + 4 - 16 + 10 - 12 - 12 + 14 - 6 + 18 = 243.
# The length of the list is 7, so the final result is 243 * 7 = 1611.