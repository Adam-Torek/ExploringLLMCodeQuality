"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""


def digit_distance_nums(num1, num2):
    """
    :param num1: int
    :param num2: int
    :return: int
    """
    num1_str = str(num1)
    num2_str = str(num2)
    if len(num1_str) != len(num2_str):
        return 0
    else:
        return sum([abs(int(num1_str[i]) - int(num2_str[i])) for i in range(len(num1_str))])


if __name__ == '__main__':
    print(digit_distance_nums(1, 2))
    print(digit_distance_nums(12, 23))
    print(digit_distance_nums(123, 234))
    print(digit_distance_nums(1234, 2345))
    print(digit_distance_nums(12345, 23456))
    print(digit_distance_nums(123456, 234567))
    print(digit_distance_nums(1234567, 2345678))
    print(digit_distance_nums(12345678, 23456789))
    print(digit_distance_nums(123456789, 234567890))
    print(digit_distance_nums(1234567890, 2345678901))
    print(digit_distance_nums(12345678901, 23456789012))
    print(digit_distance_nums(123456789012, 23456789013))
    print(digit_distance_nums(1234567890123, 234567890124))
    print(digit_distance_nums(12345678901234, 2345678901235))
    print(digit_distance_nums(123456789012345, 23456789012346))
    print(digit_distance_nums(1234567890123456, 234567890123457))
    print(digit_distance_nums(12345678901234567, 2345678901234568))
    print(digit_distance_nums(123456789012345678, 23456789012345679))
    print(digit_distance_nums(1234567890123456789, 234567890123456790))
    print(digit_distance_nums(12345678901234567890, 2345678901234567891))
    print(digit_distance_nums(123456789012345678901, 23456789012345678902))
    print(digit_distance_nums(1234567890123456789012, 234567890123456789013))
    print(digit_distance_nums(1234567890123456789012