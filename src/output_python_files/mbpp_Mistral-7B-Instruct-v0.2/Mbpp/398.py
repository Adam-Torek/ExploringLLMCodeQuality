"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""
def sum_of_digits(numbers):
    total = 0
    for number in numbers:
        while number > 0:
            digit = number % 10
            total += digit
            number = number // 10
    return total

assert sum_of_digits([10,2,56]) == 14
assert sum_of_digits([1,2,3]) == 6
assert sum_of_digits([100,2,56]) == 112
assert sum_of_digits([]) == 0
assert sum_of_digits([-1,2,3]) == 4
assert sum_of_digits([1000000000]) == 1
assert sum_of_digits([1000000000,1000000000]) == 2
assert sum_of_digits([1000000000,1000000000,1000000000]) == 3
assert sum_of_digits([1000000000,1000000000,1000000000,1000000000]) == 4
assert sum_of_digits([1000000000,1000000000,1000000000,1000000000,1000000000]) == 5
assert sum_of_digits([1000000000,1000000000,1000000000,1000000000,1000000000,1000000000]) == 6
assert sum_of_digits([1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000]) == 7
assert sum_of_digits([1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000]) == 8
assert sum_of_digits([1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000]) == 9
assert sum_of_digits([1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000]) == 10
assert sum_of_digits([1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,1000000000,100