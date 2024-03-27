"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""
def multiple_to_single(numbers):
    """
    :param numbers: list of integers
    :return: single integer
    """
    return int(''.join(map(str, numbers)))

assert multiple_to_single([11, 33, 50]) == 113350</s>