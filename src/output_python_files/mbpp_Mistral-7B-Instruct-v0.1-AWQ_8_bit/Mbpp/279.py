"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""

def is_num_decagonal(n):
    """
    Check if a number is decagonal
    """
    if n < 10 or n % 10 != 0:
        return False
    else:
        return True

def nth_decagonal_number(n):
    """
    Find the nth decagonal number
    """
    if n < 1 or n % 10 != 0:
        return None
    else:
        return (n * (n + 1)) // 2


if __name__ == '__main__':
    assert is_num_decagonal(3) == 27
    assert nth_decagonal_number(3) == 27
    assert nth_decagonal_number(4) == 45
    assert nth_decagonal_number(5) == 75
    assert nth_decagonal_number(6) == 120
    assert nth_decagonal_number(7) == 189
    assert nth_decagonal_number(8) == 288
    assert nth_decagonal_number(9) == 390
    assert nth_decagonal_number(10) == 500
    assert nth_decagonal_number(11) == 630
    assert nth_decagonal_number(12) == 787
    assert nth_decagonal_number(13) == 964
    assert nth_decagonal_number(14) == 1161
    assert nth_decagonal_number(15) == 1388
    assert nth_decagonal_number(16) == 1645
    assert nth_decagonal_number(17) == 1932
    assert nth_decagonal_number(18) == 2250
    assert nth_decagonal_number(19) == 2598
    assert nth_decagonal_number(20) == 3076
    assert nth_decagonal_number(21) == 3584
    assert nth_decagonal_number(22) == 4122
    assert nth_decagonal_number(23) == 4689
    assert nth_decagonal_number(24) == 5296
    assert nth_decagonal_number(25) == 5943
    assert nth_decagonal_number(26) == 6620
    assert nth_decagonal_number(27) == 7327
    assert nth_decagonal_number(28) == 8064
    assert nth_decagonal_number(29) == 8831
    assert nth_decagonal_number(30) == 9628
    assert nth_decagonal_number(31) == 10455
    assert nth_decagonal_number(32) == 11212
    assert nth_decagonal_number(33) == 11999
    assert nth_decagonal_number(34) == 12726
    assert nth_decagonal_number(35) == 13483
    assert nth_decagonal_number(36) == 14260
    assert nth_decagonal_number(37) == 14967
    assert nth_decagonal_number(38) == 15694
    assert nth_decagonal_number(39) == 16441
    assert nth_decagonal_number(40) == 17118
    assert nth_decagonal_number(41) == 17725
    assert nth_decagonal_number(42) == 18362
    assert nth_decagonal_number(43) == 18929
    assert nth_decagonal_number(44) == 19426
    assert nth