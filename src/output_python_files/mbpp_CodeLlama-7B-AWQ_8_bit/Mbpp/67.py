"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""


def bell_number(n):
    """
    Write a function to find the number of ways to partition a set of Bell numbers.
    assert bell_number(2)==2
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return bell_number(n-1) + bell_number(n-2)


def test_bell_number():
    assert bell_number(2) == 2
    assert bell_number(3) == 3
    assert bell_number(4) == 5
    assert bell_number(5) == 8
    assert bell_number(6) == 13
    assert bell_number(7) == 21
    assert bell_number(8) == 34
    assert bell_number(9) == 55
    assert bell_number(10) == 91
    assert bell_number(11) == 148
    assert bell_number(12) == 241
    assert bell_number(13) == 407
    assert bell_number(14) == 676
    assert bell_number(15) == 1097
    assert bell_number(16) == 1771
    assert bell_number(17) == 2865
    assert bell_number(18) == 4636
    assert bell_number(19) == 7502
    assert bell_number(20) == 12139
    assert bell_number(21) == 19641
    assert bell_number(22) == 31781
    assert bell_number(23) == 51684
    assert bell_number(24) == 83204
    assert bell_number(25) == 135255
    assert bell_number(26) == 218916
    assert bell_number(27) == 354224
    assert bell_number(28) == 573181
    assert bell_number(29) == 927356
    assert bell_number(30) == 1500467
    assert bell_number(31) == 2427852
    assert bell_number(32) == 3928399
    assert bell_number(33) == 6378816
    assert bell_number(34) == 10233415
    assert bell_number(35) == 16777216
    assert bell_number(36) == 26843545
    assert bell_number(37) == 42019663
    assert bell_number(38) == 67989764
    assert bell_number(39) == 108010160
    assert bell_number(40) == 177101072
    assert bell_number(41) == 286291153
    assert bell_number(42) == 465797368
    assert bell_number(43) == 754973221
    assert bell_number(44) == 1227750496
    assert bell_number(45) == 1971458417
    assert bell_number(46) == 3194043490
    assert bell_number(47) == 5162341437
    assert bell_number(48) == 8337153088
    assert bell_number(49) == 13519526113
    assert bell_number(50) == 21783093820
    assert bell_number(51)