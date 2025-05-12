"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""

def sum_negativenum(numbers):
    """
    :param numbers: list of numbers
    :return: sum of negative numbers
    """
    sum_neg = 0
    for number in numbers:
        if number < 0:
            sum_neg += number
    return sum_neg

#assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
#print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))