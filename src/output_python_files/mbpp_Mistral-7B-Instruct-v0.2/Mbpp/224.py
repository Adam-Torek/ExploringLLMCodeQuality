"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""
def count_Set_Bits(n):
    """
    :param n: an integer
    :return: the number of set bits in the binary representation of n
    """
    return bin(n).count('1')

if __name__ == "__main__":
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(3) == 2
    assert count_Set_Bits(12) == 3
    assert count_Set_Bits(15) == 4
    assert count_Set_Bits(123) == 6
    assert count_Set_Bits(12345) == 11
    assert count_Set_Bits(123456789) == 18
    assert count_Set_Bits(1234567890) == 19
    assert count_Set_Bits(123456789012345) == 27
    assert count_Set_Bits(1234567890123456789) == 36
    assert count_Set_Bits(1234567890123456789012345) == 45
    assert count_Set_Bits(12345678901234567890123456789) == 54
    assert count_Set_Bits(12345678901234567890123456789012345) == 55
    assert count_Set_Bits(123456789012345678901234567890123456789) == 56
    assert count_Set_Bits(123456789012345678901234567890123456789012345) == 57
    assert count_Set_Bits(1234567890123456789012345678901234567890123456789) == 58
    assert count_Set_Bits(1234567890123456789012345678901234567890123456789012345) == 59
    assert count_Set_Bits(12345678901234567890123456789012345678901234567890123456789) == 60
    assert count_Set_Bits(12345678901234567890123456789012345678901234567890123456789012345) == 61
    assert count_Set_Bits(123456789012345678901234567890123456789012345678901234567890123456789) == 62
    assert count_Set_Bits(12345678901234567890