def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)



def test_even_odd_count():
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(123456789) == (4, 5)
    assert even_odd_count(-123456789) == (4, 5)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(10) == (1, 1)
    assert even_odd_count(100) == (2, 0)
    assert even_odd_count(1000) == (2, 1)
    assert even_odd_count(10000) == (3, 1)
    assert even_odd_count(100000) == (4, 1)
    assert even_odd_count(1000000) == (4, 2)
    assert even_odd_count(10000000) == (5, 1)
    assert even_odd_count(100000000) == (5, 2)
    assert even_odd_count(1000000000) == (6, 2)
    assert even_odd_count(10000000000) == (6, 3)
    assert even_odd_count(10000000000) == (7, 3)
    assert even_odd_count(100000000000) == (7, 4)
    assert even_odd_count(100000000000) == (8, 4)
    assert even_odd_count(1000000000000) == (8, 5)
    assert even_odd_count(10000000000000) == (9, 5)
    assert even_odd_count(100000000000000) == (10, 5)
    assert even_odd_count(100000000000000) == (10, 6)
    assert even_odd_count(1000000000000000) == (11, 6)
    assert even_odd_count(10000000000000000) == (11, 7)
    assert even_odd_count(100000000000