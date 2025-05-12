"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""


def multiple_to_single(nums):
    """
    :param nums: list of integers
    :return: integer
    """
    return int(''.join(map(str, nums)))


if __name__ == '__main__':
    print(multiple_to_single([11, 33, 50]))
    print(multiple_to_single([11, 33, 50, 200]))
    print(multiple_to_single([11, 33, 50, 200, 400]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800, 900]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800, 900, 1000]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800, 900, 1000, 1200]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800, 900, 1000, 1200, 1400]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800, 900, 1000, 1200, 1400, 1600]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800, 900, 1000, 1200, 1400, 1600, 1800]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2200]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400]))
    print(multiple_to_single([11, 33, 50, 200, 400, 600, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]))
    print(multiple_to_single([11, 33, 50, 200, 40