"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""


def find_Index(n):
    """
    Find the index of smallest triangular number with n digits.
    """
    # Write your code here
    if n == 1:
        return 1
    else:
        return 1 + find_Index(n - 1)


if __name__ == '__main__':
    print("Example:")
    print(find_Index(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_Index(2) == 4
    assert find_Index(3) == 7
    assert find_Index(4) == 10
    assert find_Index(5) == 13
    assert find_Index(6) == 16
    assert find_Index(7) == 19
    assert find_Index(8) == 22
    assert find_Index(9) == 25
    assert find_Index(10) == 28
    assert find_Index(11) == 31
    assert find_Index(12) == 34
    assert find_Index(13) == 37
    assert find_Index(14) == 40
    assert find_Index(15) == 43
    assert find_Index(16) == 46
    assert find_Index(17) == 49
    assert find_Index(18) == 52
    assert find_Index(19) == 55
    assert find_Index(20) == 58
    assert find_Index(21) == 61
    assert find_Index(22) == 64
    assert find_Index(23) == 67
    assert find_Index(24) == 70
    assert find_Index(25) == 73
    assert find_Index(26) == 76
    assert find_Index(27) == 79
    assert find_Index(28) == 82
    assert find_Index(29) == 85
    assert find_Index(30) == 88
    assert find_Index(31) == 91
    assert find_Index(32) == 94
    assert find_Index(33) == 97
    assert find_Index(34) == 100
    assert find_Index(35) == 103
    assert find_Index(36) == 106
    assert find_Index(37) == 109
    assert find_Index(38) == 112
    assert find_Index(39) == 115
    assert find_Index(40) == 118
    assert find_Index(41) == 121
    assert find_Index(42) == 124
    assert find_Index(43) == 127
    assert find_Index(44) == 130
    assert find_Index(45) == 133
    assert find_Index(46) == 136
    assert find_Index(47) == 139
    assert find_Index(48) == 142
    assert find_Index(49) == 145
    assert find_Index(50) == 148
    assert find_Index(51) == 151
    assert find_Index(52) == 154
    assert find_Index(53) == 157
    assert find_Index(54) == 160
    assert find_Index(55) == 163
    assert find_Index(56) == 166
    assert find_Index(57) == 169
    assert find_Index