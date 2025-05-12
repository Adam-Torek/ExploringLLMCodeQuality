"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""


def find_star_num(n):
    """
    Find the n'th star number.
    """
    if n == 1:
        return 1
    else:
        return find_star_num(n-1) + find_star_num(n-2)


def test_find_star_num():
    """
    Test find_star_num.
    """
    assert find_star_num(1) == 1
    assert find_star_num(2) == 2
    assert find_star_num(3) == 37
    assert find_star_num(4) == 137
    assert find_star_num(5) == 443
    assert find_star_num(6) == 1407
    assert find_star_num(7) == 4817
    assert find_star_num(8) == 16007
    assert find_star_num(9) == 50007
    assert find_star_num(10) == 170007
    assert find_star_num(11) == 540007
    assert find_star_num(12) == 180007
    assert find_star_num(13) == 580007
    assert find_star_num(14) == 200007
    assert find_star_num(15) == 620007
    assert find_star_num(16) == 220007
    assert find_star_num(17) == 660007
    assert find_star_num(18) == 700007
    assert find_star_num(19) == 740007
    assert find_star_num(20) == 780007
    assert find_star_num(21) == 820007
    assert find_star_num(22) == 860007
    assert find_star_num(23) == 900007
    assert find_star_num(24) == 940007
    assert find_star_num(25) == 980007
    assert find_star_num(26) == 1020007
    assert find_star_num(27) == 1060007
    assert find_star_num(28) == 1100007
    assert find_star_num(29) == 1140007
    assert find_star_num(30) == 1180007
    assert find_star_num(31) == 1220007
    assert find_star_num(32) == 1260007
    assert find_star_num(33) == 1300007
    assert find_star_num(34) == 1340007
    assert find_star_num(35) == 1380007
    assert find_star_num(36) == 1420007
    assert find_star_num(37) == 1460007
    assert find_star_num(38) == 1500007
    assert find_star_num(39) == 1540007
    assert find_star_num(40) == 1580007
    assert find_star_num(41) == 1620007
    assert find_star_num(42) == 1660007
    assert find_star_num(43) == 1700007
    assert find_star_num(44) == 1740007
    assert find_