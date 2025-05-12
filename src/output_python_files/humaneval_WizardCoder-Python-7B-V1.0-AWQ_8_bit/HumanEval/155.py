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
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(10) == (1, 1)
    assert even_odd_count(100) == (2, 0)
    assert even_odd_count(1230) == (1, 2)
    assert even_odd_count(123045) == (2, 3)
    assert even_odd_count(1230456) == (3, 3)
    assert even_odd_count(12304567) == (3, 4)
    assert even_odd_count(123045678) == (4, 4)
    assert even_odd_count(1230456789) == (4, 5)
    assert even_odd_count(12304567890) == (5, 5)
    assert even_odd_count(123045678900) == (6, 5)
    assert even_odd_count(1230456789000) == (7, 6)
    assert even_odd_count(12304567890000) == (8, 7)
    assert even_odd_count(123045678900000) == (9, 8)
    assert even_odd_count(1230456789000000) == (10, 9)
    assert even_odd_count(12304567890000000) == (11, 10)
    assert even_odd_count(123045678900000000) == (12, 11)
    assert even_odd_count(1230456789000000000) == (13, 12)
    assert even_odd_count(12304567890000000000) == (14, 13)
    assert even_odd_count(123045678900000000000) == (15, 14)
    assert even_odd_count(123045678900000000000) == (16, 15)
    assert even_odd_count(123045678900000000000) == (17, 16)
    assert even_odd_count(1230456789000000000000) == (18, 17)
    assert even_odd_count(12304567890000000000000) == (19, 18)
    assert even_odd_count(12304567890000000000000) == (20, 19)
    assert even_odd_count(1230456789000000000