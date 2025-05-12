"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""


def digit_distance_nums(num1, num2):
    """
    Write a python function to find the sum of the per-digit difference between two integers.
    assert digit_distance_nums(1,2) == 1
    """
    num1_list = list(str(num1))
    num2_list = list(str(num2))
    sum_list = []
    for i in range(len(num1_list)):
        sum_list.append(abs(int(num1_list[i]) - int(num2_list[i])))
    return sum(sum_list)


if __name__ == '__main__':
    print(digit_distance_nums(1, 2))
    print(digit_distance_nums(123, 456))
    print(digit_distance_nums(1234, 5678))
    print(digit_distance_nums(12345, 67890))
    print(digit_distance_nums(123456, 789012))
    print(digit_distance_nums(1234567, 8901234))
    print(digit_distance_nums(12345678, 90123456))
    print(digit_distance_nums(123456789, 012345678))
    print(digit_distance_nums(1234567890, 123456789))
    print(digit_distance_nums(12345678901, 2345678901))
    print(digit_distance_nums(123456789012, 3456789012))
    print(digit_distance_nums(1234567890123, 4567890123))
    print(digit_distance_nums(12345678901234, 5678901234))
    print(digit_distance_nums(123456789012345, 6789012345))
    print(digit_distance_nums(1234567890123456, 7890123456))
    print(digit_distance_nums(12345678901234567, 8901234567))
    print(digit_distance_nums(123456789012345678, 9012345678))
    print(digit_distance_nums(1234567890123456789, 0123456789))
    print(digit_distance_nums(12345678901234567890, 1234567890))
    print(digit_distance_nums(123456789012345678901, 2345678901))
    print(digit_distance_nums(1234567890123456789012, 3456789012))
    print(digit_distance_nums(12345678901234567890123, 4567890123))
    print(digit_distance_nums(123456789012345678901234, 5678901234))
    print(digit_distance_nums(