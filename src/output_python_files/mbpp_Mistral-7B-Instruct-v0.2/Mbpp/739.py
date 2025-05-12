"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""
from math import ceil, sqrt

def find_Index(n):
    """
    :param n: int
    :return: int
    """
    triangular_number = 1
    while len(str(triangular_number)) < n:
        triangular_number += 1

    row = ceil(sqrt(8 * triangular_number + 1))
    column = (triangular_number - (row - 1) * (row - 1) // 2) + 1

    return int(str(triangular_number)[column - 1])

if __name__ == "__main__":
    assert find_Index(2) == 4
    assert find_Index(3) == 13
    assert find_Index(4) == 21
    assert find_Index(5) == 32
    assert find_Index(6) == 43
    assert find_Index(7) == 55
    assert find_Index(8) == 69
    assert find_Index(9) == 83
    assert find_Index(10) == 97
    assert find_Index(11) == 111
    assert find_Index(12) == 125
    assert find_Index(13) == 139
    assert find_Index(14) == 153
    assert find_Index(15) == 167
    assert find_Index(16) == 181
    assert find_Index(17) == 195
    assert find_Index(18) == 209
    assert find_Index(19) == 223
    assert find_Index(20) == 237
    assert find_Index(21) == 251
    assert find_Index(22) == 265
    assert find_Index(23) == 279
    assert find_Index(24) == 293
    assert find_Index(25) == 307
    assert find_Index(26) == 321
    assert find_Index(27) == 335
    assert find_Index(28) == 349
    assert find_Index(29) == 363
    assert find_Index(30) == 377
    assert find_Index(31) == 391
    assert find_Index(32) == 405
    assert find_Index(33) == 419
    assert find_Index(34) == 433
    assert find_Index(35) == 447
    assert find_Index(36) == 461
    assert find_Index(37) == 475
    assert find_Index(38) == 489
    assert find_Index(39) == 503
    assert find_Index(40) == 517
    assert find_Index(41) == 531
    assert find_Index(42) == 545
    assert find_Index(43) == 559
    assert find_Index(44) == 573
    assert find_Index(45) == 587
    assert find_Index(46) == 601
    assert find_Index(47) == 615
    assert find_Index(48) == 629
    assert find_Index(49) == 643
    assert find_Index(50) == 657
    assert find_Index(51) == 671
    assert find_Index(52) == 685
    assert find_Index(53) == 699
    assert find_Index(54) == 71