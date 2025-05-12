"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""

def digit_distance_nums(num1, num2):
    """
    Find the sum of the per-digit difference between two integers.
    """
    num1_str = str(num1)
    num2_str = str(num2)
    sum_distance = 0
    for i in range(len(num1_str)):
        sum_distance += abs(int(num1_str[i]) - int(num2_str[i]))
    return sum_distance


if __name__ == '__main__':
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(10,12) == 2
    assert digit_distance_nums(100,120) == 6
    assert digit_distance_nums(1000,1200) == 10