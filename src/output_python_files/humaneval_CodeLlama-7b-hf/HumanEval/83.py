def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(int(str(i)[0]) == 1 or int(str(i)[-1]) == 1 for i in range(10**n))


def test_starts_one_ends():
    assert starts_one_ends(1) == 10
    assert starts_one_ends(2) == 91
    assert starts_one_ends(3) == 730
    assert starts_one_ends(4) == 5462
    assert starts_one_ends(5) == 40582
    assert starts_one_ends(6) == 295238
    assert starts_one_ends(7) == 2102400
    assert starts_one_ends(8) == 14972560
    assert starts_one_ends(9) == 108348800
    assert starts_one_ends(10) == 803040730
    assert starts_one_ends(11) == 5842653760
    assert starts_one_ends(12) == 42282880160
    assert starts_one_ends(13) == 304932457280
    assert starts_one_ends(14) == 2218975680000
    assert starts_one_ends(15) == 16050843200000
    assert starts_one_ends(16) == 114131280000000
    assert starts_one_ends(17) == 8462412800000000
    assert starts_one_ends(18) == 60416800000000000
    assert starts_one_ends(19) == 429071280000000000
    assert starts_one_ends(20) == 3027024000000000000
    assert starts_one_ends(21) == 22020480000000000000
    assert starts_one_ends(22) == 162948400000000000000
    assert starts_one_ends(23) == 1187888000000000000000
    assert starts_one_ends(24) == 8821600000000000000000
    assert starts_one_ends(25) == 63023200000000000000000
    assert starts_one_ends(26) == 443680000000