def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 for i in range(10**(n-1), 10**n) if str(i)[0] == '1' or str(i)[-1] == '1')


def test_starts_one_ends():
    assert starts_one_ends(1) == 10
    assert starts_one_ends(2) == 91
    assert starts_one_ends(3) == 730
    assert starts_one_ends(4) == 5462
    assert starts_one_ends(5) == 40582
    assert starts_one_ends(6) == 283776
    assert starts_one_ends(7) == 1964184
    assert starts_one_ends(8) == 13632456
    assert starts_one_ends(9) == 98577368
    assert starts_one_ends(10) == 703057768
    assert starts_one_ends(11) == 4862274384
    assert starts_one_ends(12) == 32951280096
    assert starts_one_ends(13) == 227103488096
    assert starts_one_ends(14) == 1594305443200
    assert starts_one_ends(15) == 10488080000000
    assert starts_one_ends(16) == 662271040000000
    assert starts_one_ends(17) == 4052739520000000
    assert starts_one_ends(18) == 23860928000000000
    assert starts_one_ends(19) == 148148192000000000
    assert starts_one_ends(20) == 846246800000000000
    assert starts_one_ends(21) == 5128480000000000000
    assert starts_one_ends(22) == 30800000000000000000
    assert starts_one_ends(23) == 198416000000000000000
    assert starts_one_ends(24) == 1286720000000000000000
    assert starts_one_ends(25) == 8235439040000000000000
    assert starts_one_ends(26) == 48888800000000000000000
    assert starts_one_ends(27) == 288006710400000000000000
    assert starts_one_ends(28) == 1679616000000000000000000
    assert starts_one_ends(29) == 9843200000000000000000000
    assert starts_one_ends(30) == 58640000000000000000000000
    assert starts_one_ends(31) == 304480000000000000000000000
    assert starts_one_ends(32) == 1680720000000000000000000