"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""


def median_numbers(num1, num2, num3):
    """
    Write a function to find the median of three numbers.
    assert median_numbers(25,55,65)==55.0
    """
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 == num2:
        return (num1 + num2) / 2
    else:
        return num2


if __name__ == '__main__':
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))
    print(median_numbers(25, 55, 65))