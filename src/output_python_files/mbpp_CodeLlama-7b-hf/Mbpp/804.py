"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""

def is_product_even(numbers):
    """
    Check whether the product of numbers in a list is even or not.
    """
    if len(numbers) == 0:
        return False
    if len(numbers) == 1:
        return True
    if len(numbers) == 2:
        return numbers[0] * numbers[1] % 2 == 0
    if len(numbers) == 3:
        return numbers[0] * numbers[1] * numbers[2] % 2 == 0
    if len(numbers) == 4:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] % 2 == 0
    if len(numbers) == 5:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] % 2 == 0
    if len(numbers) == 6:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] % 2 == 0
    if len(numbers) == 7:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] * numbers[6] % 2 == 0
    if len(numbers) == 8:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] * numbers[6] * numbers[7] % 2 == 0
    if len(numbers) == 9:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] * numbers[6] * numbers[7] * numbers[8] % 2 == 0
    if len(numbers) == 10:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] * numbers[6] * numbers[7] * numbers[8] * numbers[9] % 2 == 0
    if len(numbers) == 11:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] * numbers[6] * numbers[7] * numbers[8] * numbers[9] * numbers[10] % 2 == 0
    if len(numbers) == 12:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] * numbers[6] * numbers[7] * numbers[8] * numbers[9] * numbers[10] * numbers[11] % 2 == 0
    if len(numbers) == 13:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] * numbers[6] * numbers[7] * numbers[8] * numbers[9] * numbers[10] * numbers[11] * numbers[12] % 2 == 0
    if len(numbers) == 14:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] * numbers[6] * numbers[7] * numbers[8] * numbers[9] * numbers[10] * numbers[11] * numbers[12] * numbers[13] % 2 == 0
    if len(numbers) == 15:
        return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] * numbers[6] * numbers[7] * numbers[8] * numbers[9] * numbers[10] * numbers[11] * numbers[12] * numbers[13] * numbers[14] % 2 == 0