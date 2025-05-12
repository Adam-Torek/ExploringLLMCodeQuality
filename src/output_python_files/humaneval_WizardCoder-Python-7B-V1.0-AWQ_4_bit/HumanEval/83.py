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



def test_count_ones_start_end():
    assert count_ones_start_end(1) == 9
    assert count_ones_start_end(2) == 90
    assert count_ones_start_end(3) == 900
    assert count_ones_start_end(4) == 9000
    assert count_ones_start_end(5) == 90000
    assert count_ones_start_end(6) == 900000
    assert count_ones_start_end(7) == 9000000
    assert count_ones_start_end(8) == 90000000
    assert count_ones_start_end(9) == 900000000
    assert count_ones_start_end(10) == 9000000000
    assert count_ones_start_end(11) == 90000000000
    assert count_ones_start_end(12) == 900000000000
    assert count_ones_start_end(13) == 9000000000000
    assert count_ones_start_end(14) == 90000000000000
    assert count_ones_start_end(15) == 90000000000000
    assert count_ones_start_end(16) == 900000000000000
    assert count_ones_start_end(17) == 900000000000000
    assert count_ones_start_end(18) == 9000000000000000
    assert count_ones_start_end(19) == 90000000000000000
    assert count_ones_start_end(20) == 900000000000000000



if __name__ == "__main__":
    test_count_ones_start_end()
    print(count_ones_start_end(10))