"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""
def perfect_squares(start, end):
    """
    :param start: int, the lower limit
    :param end: int, the upper limit
    :return: list, a list of perfect squares between start and end
    """
    result = []
    for i in range(start, end+1):
        if i**0.5.is_integer():
            result.append(i)
    return result

if __name__ == "__main__":
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    print(perfect_squares(1,30))