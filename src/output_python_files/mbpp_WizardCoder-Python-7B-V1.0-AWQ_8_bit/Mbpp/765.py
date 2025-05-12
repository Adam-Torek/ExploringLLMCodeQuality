"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""

def is_polite(n: int) -> int:
    def is_polite_helper(n: int, count: int) -> int:
        if n == 1:
            return 1
        if n % 2 == 0:
            return is_polite_helper(n-1, count+1) + count
        else:
            return is_polite_helper(n-1, count) + count + 1

    return is_polite_helper(n, 1)


def nth_polite_number(n: int) -> int:
    return is_polite(n)


# Test cases
assert nth_polite_number(1) == 1
assert nth_polite_number(2) == 2
assert nth_polite_number(3) == 3
assert nth_polite_number(4) == 4
assert nth_polite_number(5) == 5
assert nth_polite_number(6) == 7
assert nth_polite_number(7) == 11
assert nth_polite_number(8) == 12
assert nth_polite_number(9) == 13
assert nth_polite_number(10) == 14
assert nth_polite_number(11) == 15
assert nth_polite_number(12) == 16
assert nth_polite_number(13) == 17
assert nth_polite_number(14) == 18
assert nth_polite_number(15) == 19
assert nth_polite_number(16) == 20
assert nth_polite_number(17) == 22
assert nth_polite_number(18) == 23
assert nth_polite_number(19) == 24
assert nth_polite_number(20) == 25
assert nth_polite_number(21) == 26
assert nth_polite_number(22) == 28
assert nth_polite_number(23) == 29
assert nth_polite_number(24) == 30
assert nth_polite_number(25) == 31
assert nth_polite_number(26) == 32
assert nth_polite_number(27) == 34
assert nth_polite_number(28) == 35
assert nth_polite_number(29) == 36
assert nth_polite_number(30) == 37
assert nth_polite_number(31) == 38
assert nth_polite_number(32) == 39
assert nth_polite_number(33) == 41
assert nth_polite_number(34) == 42
assert nth_polite_number(35) == 43
assert nth_polite_number(36) == 44
assert nth_polite_number(37) == 45
assert nth_polite_number(38) == 46
assert nth_polite_number(39) == 48
assert nth_polite_number(40) == 49
assert nth_polite_number(41) == 50
assert nth_polite_number(42) == 51
assert nth_polite_number(43) == 53
assert nth_polite_number(44) == 54
assert nth_polite_number(45) == 55
assert nth_polite_number(46) == 56
assert nth_polite_number(47) == 58
assert nth_polite_number(48) == 59
assert nth_polite_number(49) == 60
assert nth