"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""

def cube_sum(n):
    """
    :param n: int
    :return: int
    """
    return sum([i**3 for i in range(2, n+1)])


if __name__ == '__main__':
    assert cube_sum(2) == 72
    print(cube_sum(2))