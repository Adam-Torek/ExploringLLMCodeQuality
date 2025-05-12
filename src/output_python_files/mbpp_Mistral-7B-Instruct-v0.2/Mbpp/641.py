"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""
import math

def is_nonagonal(n):
    """
    Check if n is a nonagonal number
    """
    side_length = 3 * (3 * math.sqrt(3) + 2)
    return bool(int(math.floor(math.pow(side_length, 2) / 3 * n)) % 2)

def nonagonal_number(n):
    """
    Find the nth nonagonal number
    """
    side_length = 3 * (3 * math.sqrt(3) + 2)
    return int(math.floor(math.pow(side_length, 2) / 3 * n))

if __name__ == "__main__":
    assert is_nonagonal(10) == True
    assert is_nonagonal(11) == False
    assert nonagonal_number(1) == 1
    assert nonagonal_number(2) == 13
    assert nonagonal_number(3) == 61
    assert nonagonal_number(4) == 231
    assert nonagonal_number(5) == 851
    assert nonagonal_number(6) == 3061
    assert nonagonal_number(7) == 10641
    assert nonagonal_number(8) == 36561
    assert nonagonal_number(9) == 123641
    assert nonagonal_number(10) == 419931
    assert nonagonal_number(20) == 16434201
    assert nonagonal_number(30) == 593024001
    assert nonagonal_number(40) == 21801760001
    assert nonagonal_number(50) == 754553600001
    assert nonagonal_number(60) == 25636672000001
    assert nonagonal_number(70) == 869099840000001
    assert nonagonal_number(80) == 29072992000000001
    assert nonagonal_number(90) == 976287488000000001
    assert nonagonal_number(100) == 32517651200000000001
    print("All tests passed")