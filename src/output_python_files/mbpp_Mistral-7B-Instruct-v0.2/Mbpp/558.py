"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""
def digit_distance_nums(num1, num2):
    """
    This function takes two integers as arguments and returns the sum of the per-digit differences between them.
    """
    num1_str = str(num1)
    num2_str = str(num2)
    if len(num1_str) != len(num2_str):
        raise ValueError("Both integers must have the same number of digits.")

    sum = 0
    for i in range(len(num1_str)):
        digit_diff = abs(int(num1_str[i]) - int(num2_str[i]))
        sum += digit_diff

    return sum

# Test cases
assert digit_distance_nums(1, 2) == 1
assert digit_distance_nums(10, 11) == 1
assert digit_distance_nums(123, 456) == 33
assert digit_distance_nums(123, 321) == 31
assert digit_distance_nums(123, 213) == 10
assert digit_distance_nums(123, 123) == 0
assert digit_distance_nums(123, 111) == 18
assert digit_distance_nums(123, 312) == 21
assert digit_distance_nums(123, 321) == 31
assert digit_distance_nums(123, 3210) == 103
assert digit_distance_nums(123, 32100) == 1030
assert digit_distance_nums(123, 321000) == 10300
assert digit_distance_nums(123, 3210000) == 1030000
assert digit_distance_nums(123, 32100000) == 10300000
assert digit_distance_nums(123, 321000000) == 103000000
assert digit_distance_nums(123, 3210000000) == 1030000000
assert digit_distance_nums(123, 32100000000) == 10300000000
assert digit_distance_nums(123, 321000000000) == 103000000000
assert digit_distance_nums(123, 3210000000000) == 1030000000000
assert digit_distance_nums(123, 32100000000000) == 10300000000000
assert digit_distance_nums(123, 321000000000000) == 103000000000000
assert digit_distance_nums(123, 3210000000000000) == 1030000000000000
assert digit_distance_nums(123, 32100000000000000) == 10300000000000000
assert digit_distance_nums(123, 321000000000000000) == 103000000000000000
assert digit_distance_nums(123, 3210000000000000000) == 103000