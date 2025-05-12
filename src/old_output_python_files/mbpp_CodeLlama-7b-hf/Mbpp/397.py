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
    if num2 == num3:
        return num2
    if num1 == num2:
        return num1
    if num1 == num3:
        return num1
    if num2 == num3:
        return num2
    if num1 < num2 < num3:
        return num2
    if num1 < num3 < num2:
        return num3
    if num2 < num1 < num3:
        return num1
    if num2 < num3 < num1:
        return num3
    if num3 < num1 < num2:
        return num1
    if num3 < num2 < num1:
        return num2


if __name__ == '__main__':
    print(median_numbers(25, 55, 65))
    print(median_numbers(1, 2, 3))
    print(median_numbers(1, 2, 3, 4))
    print(median_numbers(1, 2, 3, 4, 5))
    print(median_numbers(1, 2, 3, 4, 5, 6))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    print(median_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,