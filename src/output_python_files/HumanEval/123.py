def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    odd_collatz = []
    while n != 1:
        if n % 2 == 1:
            odd_collatz.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    return odd_collatz


def test_get_odd_collatz():
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(2) == []
    assert get_odd_collatz(3) == [3]
    assert get_odd_collatz(4) == []
    assert get_odd_collatz(6) == [1, 6]
    assert get_odd_collatz(7) == [7]
    assert get_odd_collatz(8) == []
    assert get_odd_collatz(9) == [9]
    assert get_odd_collatz(10) == []
    assert get_odd_collatz(11) == [11]
    assert get_odd_collatz(12) == []
    assert get_odd_collatz(13) == [13]
    assert get_odd_collatz(14) == []
    assert get_odd_collatz(15) == [15]
    assert get_odd_collatz(16) == []
    assert get_odd_collatz(17) == [17]
    assert get_odd_collatz(18) == []
    assert get_odd_collatz(19) == [19]
    assert get_odd_collatz(20) == []
    assert get_odd_collatz(21) == [21]
    assert get_odd_collatz(22) == []
    assert get_odd_collatz(23) == [23]
    assert get_odd_collatz(24) == []
    assert get_odd_collatz(25) == [25]
    assert get_odd_collatz(26) == []
    assert get_odd_collatz(27) == [27]
    assert get_odd_collatz(28) == []
    assert get_odd_collatz(29) == [29]
    assert get_odd_collatz(30) == []
    assert get_odd_collatz(31) == [31]
    assert get_odd_collatz(32) == []
    assert get_odd_collatz(33) == [33]
    assert get_odd_collatz(34) == []
    assert get_odd_collatz(35) == [35]
    assert get_odd_collatz(36) == []
    assert get_odd_collatz(37) == [37]
    assert get_odd_collatz(38) == []
    assert get_odd_collatz(39) == [39]
    assert get_odd_collatz(40) == []
    assert get_odd_collatz(41) == [41]
    assert