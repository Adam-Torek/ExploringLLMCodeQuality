def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2 == 0 and y % 2 == 0:
        return max(x, y)
    else:
        return -1


def test_choose_num():
    """This function tests the choose_num function"""
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(10, 18) == -1
    assert choose_num(16, 20) == 16
    assert choose_num(11, 17) == -1
    assert choose_num(19, 21) == -1
    assert choose_num(22, 25) == 22
    assert choose_num(24, 23) == 24
    assert choose_num(26, 29) == 26
    assert choose_num(28, 27) == 28


if __name__ == '__main__':
    test_choose_num()