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
    if n <= 0:
        raise ValueError("n must be a positive integer")
    odd_collatz = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            odd_collatz.append(n)
            n = 3 * n + 1
    odd_collatz.append(1)
    return sorted(odd_collatz)


def test_get_odd_collatz():
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(10) == [1, 10]
    assert get_odd_collatz(100) == [1, 100]
    assert get_odd_collatz(1000) == [1, 1000]
    assert get_odd_collatz(10000) == [1, 10000]
    assert get_odd_collatz(100000) == [1, 100000]
    assert get_odd_collatz(1000000) == [1, 1000000]
    assert get_odd_collatz(10000000) == [1, 10000000]
    assert get_odd_collatz(100000000) == [1, 100000000]
    assert get_odd_collatz(1000000000) == [1, 1000000000]
    assert get_odd_collatz(10000000000) == [1, 10000000000]
    assert get_odd_collatz(100000000000) == [1, 100000000000]
    assert get_odd_collatz(1000000000000) == [1, 1000000000000]
    assert get_odd_collatz(10000000000000) == [1, 10000000000000]
    assert get_odd_collatz(100000000000000) == [1, 100000000000000]
    assert get_odd_collatz(1000000000000000) == [1, 1000000000000000]
    assert get_odd_collatz(10000000000000000) == [1, 10000000000000000]
    assert get_odd_collatz(100000000000000000) == [1, 100000000000000000]
    assert get_odd_collatz(1000