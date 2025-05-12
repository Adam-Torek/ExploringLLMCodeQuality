def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(10**(n-1):10**n):
        if i % 10 == 1 or i // 10**(n-1) == 1:
            count += 1
    return count



def test_count_ones():
    assert count_ones(1) == 9
    assert count_ones(2) == 90
    assert count_ones(3) == 900
    assert count_ones(4) == 9000
    assert count_ones(5) == 90000
    assert count_ones(6) == 900000
    assert count_ones(7) == 9000000
    assert count_ones(8) == 90000000
    assert count_ones(9) == 900000000
    assert count_ones(10) == 9000000000
    assert count_ones(11) == 90000000000
    assert count_ones(12) == 900000000000
    assert count_ones(13) == 9000000000000
    assert count_ones(14) == 90000000000000
    assert count_ones(15) == 900000000000000
    assert count_ones(16) == 9000000000000000
    assert count_ones(17) == 90000000000000000
    assert count_ones(18) == 900000000000000000
    assert count_ones(19) == 900000000000000000
    assert count_ones(20) == 9000000000000000000



def test_count_ones_one_ends():
    assert count_ones_one_ends(1) == 1
    assert count_ones_one_ends(2) == 10
    assert count_ones_one_ends(3) == 100
    assert count_ones_one_ends(4) == 1000
    assert count_ones_one_ends(5) == 10000
    assert count_ones_one_ends(6) == 100000
    assert count_ones_one_ends(7) == 1000000
    assert count_ones_one_ends(8) == 10000000
    assert count_ones_one_ends(9) == 100000000
    assert count_ones_one_ends(10) == 1000000000
    assert count_ones_one_ends(11) == 10000000000
    assert count_ones_one_ends(12) == 100000000000
    assert count_ones_one_ends(13) == 1000000000000
    assert count_ones_one_ends(14) == 10000000000000
    assert count_ones_one_ends(15) == 100000000000000
    assert count_ones_one_ends(16) == 1000000000000000
    assert count_ones_one_ends(17) == 10000000000000000
    assert count_ones_one_ends(18) == 1000000000000000