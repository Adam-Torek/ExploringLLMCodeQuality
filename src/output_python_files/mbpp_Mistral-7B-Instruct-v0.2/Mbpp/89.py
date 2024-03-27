"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""

def closest_num(n):
    """
    :param n: int
    :return: int
    """
    smaller = float('inf')
    for i in range(n):
        if i < n and i < smaller:
            smaller = i
    return smaller

if __name__ == '__main__':
    assert closest_num(11) == 10
    assert closest_num(5) == 4
    assert closest_num(1) == 0
    assert closest_num(100) == 99
    assert closest_num(1000) == 999
    assert closest_num(float('inf')) == float('inf')
    assert closest_num(-1) == -2
    assert closest_num(-10) == -11
    assert closest_num(-100) == -101
    assert closest_num(-1000) == -1001
    assert closest_num(-float('inf')) == -float('inf')</s>