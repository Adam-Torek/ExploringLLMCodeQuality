"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""
def sum_of_digits(lst):
    sum = 0
    for i in lst:
        sum += sum(int(digit) for digit in str(i))
    return sum

# assert sum_of_digits([10,2,56])==14
print(sum_of_digits([10,2,56]))