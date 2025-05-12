"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""
def check_Consecutive(numbers):
    """
    :param numbers: list of integers
    :return: True if the list contains consecutive numbers, False otherwise
    """
    if len(numbers) < 2:
        return True

    diff = numbers[1] - numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] != diff:
            return False
    return True

# Test cases
assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,2,3,5,6]) == False
assert check_Consecutive([1,2,3,4,5,6]) == True
assert check_Consecutive([1,2,3,5,7]) == False
assert check_Consecutive([1,2,3,4,5,6,7]) == True
assert check_Consecutive([1,2,3,4,5,6,7,8]) == True
assert check_Consecutive([1,2,3,4,5,6,7,9,10]) == True
assert check_Consecutive([1,2,3,4,5,6,7,9,11]) == False