"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""
import math

def find_Index(n):
    """
    :param n: int
    :return: int
    """
    triangular = 0
    index = 0
    while len(str(triangular)) < n:
        triangular += 1
        index += 1
    return index

if __name__ == "__main__":
    assert find_Index(2) == 4
    assert find_Index(3) == 10
    assert find_Index(4) == 17
    assert find_Index(5) == 28
    assert find_Index(6) == 43
    assert find_Index(7) == 62
    assert find_Index(8) == 88
    assert find_Index(9) == 126
    assert find_Index(10) == 171
    assert find_Index(11) == 221
    assert find_Index(12) == 282
    assert find_Index(13) == 355
    assert find_Index(14) == 441
    assert find_Index(15) == 542
    assert find_Index(16) == 656
    assert find_Index(17) == 785
    assert find_Index(18) == 931
    assert find_Index(19) == 1102
    assert find_Index(20) == 1297
    assert find_Index(21) == 1518
    assert find_Index(22) == 1771
    assert find_Index(23) == 2058
    assert find_Index(24) == 2381
    assert find_Index(25) == 2739
    assert find_Index(26) == 3132
    assert find_Index(27) == 3563
    assert find_Index(28) == 4032
    assert find_Index(29) == 4541
    assert find_Index(30) == 5100
    assert find_Index(31) == 5711
    assert find_Index(32) == 6472
    assert find_Index(33) == 7303
    assert find_Index(34) == 8204
    assert find_Index(35) == 9175
    assert find_Index(36) == 10216
    assert find_Index(37) == 11337
    assert find_Index(38) == 12548
    assert find_Index(39) == 13859
    assert find_Index(40) == 15270
    assert find_Index(41) == 16801
    assert find_Index(42) == 18462
    assert find_Index(43) == 20263
    assert find_Index(44) == 22114
    assert find_Index(45) == 24015
    assert find_Index(46) == 26076
    assert find_Index(47) == 28297
    assert find_Index(48) == 30688
    assert find_Index(49) == 33259
    assert find_Index(50) == 36010
    assert find_Index(51) == 39051
    assert find_Index(52) == 42382
    assert find_Index(53) == 46013
    assert find_Index(54) == 50054
    assert find_Index(55) == 54415
    assert find_Index(56) == 59106
    assert find_Index