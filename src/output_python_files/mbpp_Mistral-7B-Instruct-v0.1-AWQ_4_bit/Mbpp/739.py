"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""

def find_Index(n):
    """
    :type n: int
    :rtype: int
    """
    # 1. Find the number of digits in n
    digits = len(str(n))
    # 2. Find the smallest triangular number with n digits
    smallest_triangular_number = 1
    for i in range(1, digits + 1):
        smallest_triangular_number *= i
    # 3. Find the index of the smallest triangular number with n digits
    index = 0
    while True:
        index += 1
        if smallest_triangular_number < n:
            break
        smallest_triangular_number += index
    return index


if __name__ == '__main__':
    assert find_Index(2) == 4
    assert find_Index(3) == 6
    assert find_Index(4) == 10
    assert find_Index(5) == 15
    assert find_Index(6) == 21
    assert find_Index(7) == 28
    assert find_Index(8) == 36
    assert find_Index(9) == 45
    assert find_Index(10) == 55
    assert find_Index(11) == 66
    assert find_Index(12) == 78
    assert find_Index(13) == 91
    assert find_Index(14) == 105
    assert find_Index(15) == 121
    assert find_Index(16) == 138
    assert find_Index(17) == 155
    assert find_Index(18) == 172
    assert find_Index(19) == 190
    assert find_Index(20) == 209
    assert find_Index(21) == 228
    assert find_Index(22) == 247
    assert find_Index(23) == 266
    assert find_Index(24) == 285
    assert find_Index(25) == 304
    assert find_Index(26) == 323
    assert find_Index(27) == 342
    assert find_Index(28) == 361
    assert find_Index(29) == 380
    assert find_Index(30) == 400
    assert find_Index(31) == 410
    assert find_Index(32) == 420
    assert find_Index(33) == 430
    assert find_Index(34) == 440
    assert find_Index(35) == 450
    assert find_Index(36) == 460
    assert find_Index(37) == 470
    assert find_Index(38) == 480
    assert find_Index(39) == 490
    assert find_Index(40) == 500
    assert find_Index(41) == 510
    assert find_Index(42) == 520
    assert find_Index(43) == 530
    assert find_Index(44) == 540
    assert find_Index(45) == 550
    assert find_Index(46) == 560
    assert find_Index(47) == 570
    assert find_Index(48) == 580
    assert find_Index(49) == 590
    assert find_Index(50) == 600
    assert find_Index(51) == 610
    assert find_Index(52) == 6