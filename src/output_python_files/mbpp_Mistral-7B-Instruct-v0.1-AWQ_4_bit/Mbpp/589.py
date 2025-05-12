"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""

def perfect_squares(start, end):
    """
    Function to find perfect squares between two given numbers
    :param start: start number
    :param end: end number
    :return: list of perfect squares between start and end
    """
    result = []
    for i in range(start, end+1):
        if i**2 == i:
            result.append(i)
    return result

assert perfect_squares(1,30)==[1, 4, 9, 16, 25]