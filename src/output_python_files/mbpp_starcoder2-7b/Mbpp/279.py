"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""

def is_num_decagonal(n):
    return (10*n**2 - 10*n + 21) % 30 == 0

def nth_decagonal(n):
    if is_num_decagonal(n):
        return (10*n**2 - 10*n + 21) // 30
    else:
        return None

def test_nth_decagonal():
    assert nth_decagonal(1) == 1
    assert nth_decagonal(2) == 10
    assert nth_decagonal(3) == 27
    assert nth_decagonal(4) == 58
    assert nth_decagonal(5) == 95
    assert nth_decagonal(6) == 138
    assert nth_decagonal(7) == 187
    assert nth_decagonal(8) == 242
    assert nth_decagonal(9) == 303
    assert nth_decagonal(10) == 370
    assert nth_decagonal(11) == 443
    assert nth_decagonal(12) == 522
    assert nth_decagonal(13) == 607
    assert nth_decagonal(14) == 698
    assert nth_decagonal(15) == 795
    assert nth_decagonal(16) == 900
    assert nth_decagonal(17) == 1011
    assert nth_decagonal(18) == 1128
    assert nth_decagonal(19) == 1251
    assert nth_decagonal(20) == 1380
    assert nth_decagonal(21) == 1515
    assert nth_decagonal(22) == 1656
    assert nth_decagonal(23) == 1803
    assert nth_decagonal(24) == 1956
    assert nth_decagonal(25) == 2115
    assert nth_decagonal(26) == 2280
    assert nth_decagonal(27) == 2451
    assert nth_decagonal(28) == 2628
    assert nth_decagonal(29) == 2811
    assert nth_decagonal(30) == 3000
    assert nth_decagonal(31) == 3195
    assert nth_decagonal(32) == 3396
    assert nth_decagonal(33) == 3603
    assert nth_decagonal(34) == 3816
    assert nth_decagonal(35) == 4035
    assert nth_decagonal(36) == 4260
    assert nth_decagonal(37) == 4491
    assert nth_decagonal(38) == 4728
    assert nth_decagonal(39) == 4971
    assert nth_decagonal(40) == 5220
    assert nth_decagonal(41) == 5475
    assert nth_decagonal(42) == 5736
    assert nth_decagonal(43) == 6003
    assert nth_decagonal(44) == 6276
    assert nth_decagonal(45) == 6555
    assert nth_decagonal(46) == 6840
    assert nth_decagonal(47) == 7131
    assert nth_decagonal(48) == 7428
    assert nth_decagonal(4