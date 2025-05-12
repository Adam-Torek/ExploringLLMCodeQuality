"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""
def get_lucid(n):
    """
    :param n: an integer
    :return: a list of lucid numbers smaller than or equal to n
    """
    lucids = []
    for i in range(1, n+1):
        sum_of_cubes = sum([int(digit)**3 for digit in str(i)])
        if i**2 == sum_of_cubes:
            lucids.append(i)
    return lucids

if __name__ == "__main__":
    assert get_lucid(10) == [1, 2, 3, 5, 7]
    print(get_lucid(100))