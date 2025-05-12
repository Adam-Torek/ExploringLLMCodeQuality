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
    assert starts_one_ends(4) == 5832
    assert starts_one_ends(5) == 46536
    assert starts_one_ends(6) == 39