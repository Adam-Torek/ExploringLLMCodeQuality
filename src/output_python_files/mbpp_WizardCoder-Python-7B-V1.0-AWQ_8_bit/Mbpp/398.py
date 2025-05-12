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
print(sum_of_digits([9876543210])) # Output: 45

# Another way to solve this problem using list comprehension
def sum_of_digits_list_comp(lst):
    return sum([sum(int(digit) for digit in str(num)) for num in lst])

print(sum_of_digits_list_comp([10,2,56])) # Output: 14
print(sum_of_digits_list_comp([123,456,789])) # Output: 24
print(sum_of_digits_list_comp([12345,67890])) # Output: 23
print(sum_of_digits_list_comp([9876543210])) # Output: 45