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
assert digit_distance_nums(123, 321) == 31
assert digit_distance_nums(123, 3210) == 111
assert digit_distance_nums(123, 021) == 21
assert digit_distance_nums(123, -123) == 0
assert digit_distance_nums(123, -1230) == 111
assert digit_distance_nums(123, -321) == 434
assert digit_distance_nums(123, -3210) == 1441
assert digit_distance_nums(123, -32100) == 14411
assert digit_distance_nums(123, -321000) == 144111
assert digit_distance_nums(123, -3210000) == 1441111
assert digit_distance_nums(123, -32100000) == 14411111
assert digit_distance_nums(123, -321000000) == 144111111
assert digit_distance_nums(123, -3210000000) == 1441111111
assert digit_distance_nums(123, -32100000000) == 14411111111
assert digit_distance_nums(123, -321000000000) == 144111111111
assert digit_distance_nums(123, -3210000000000) == 1441111111111
assert digit_distance_nums(123, -32100000000000) == 14411111111111
assert digit_distance_nums(123, -321000000000000) == 144111111111111
assert digit_distance_nums(123, -3210000000000000) == 1441111111111111
assert digit_distance_nums(123, -32100000000000000) == 144111111111111