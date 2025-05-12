"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""
def count_Set_Bits(n):
    """
    :param n: an integer
    :return: the number of set bits in the binary representation of n
    """
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

if __name__ == "__main__":
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(5) == 2
    assert count_Set_Bits(12) == 3
    assert count_Set_Bits(13) == 2
    assert count_Set_Bits(15) == 4
    assert count_Set_Bits(16) == 4
    assert count_Set_Bits(17) == 3
    assert count_Set_Bits(24) == 3
    assert count_Set_Bits(255) == 8
    assert count_Set_Bits(1023) == 10
    assert count_Set_Bits(16777215) == 16
    assert count_Set_Bits(16777216) == 17
    assert count_Set_Bits(16777217) == 16
    assert count_Set_Bits(16777218) == 16
    assert count_Set_Bits(16777219) == 16
    assert count_Set_Bits(16777220) == 16
    assert count_Set_Bits(16777221) == 16
    assert count_Set_Bits(16777222) == 16
    assert count_Set_Bits(16777223) == 16
    assert count_Set_Bits(16777224) == 16
    assert count_Set_Bits(16777225) == 16
    assert count_Set_Bits(16777226) == 16
    assert count_Set_Bits(16777227) == 16
    assert count_Set_Bits(16777228) == 16
    assert count_Set_Bits(16777229) == 16
    assert count_Set_Bits(16777230) == 16
    assert count_Set_Bits(16777231) == 16
    assert count_Set_Bits(16777232) == 16
    assert count_Set_Bits(16777233) == 16
    assert count_Set_Bits(16777234) == 16
    assert count_Set_Bits(16777235) == 16
    assert count_Set_Bits(16777236) == 16
    assert count_Set_Bits(16777237) == 16
    assert count_Set_Bits(16777238) == 16
    assert count_Set_Bits(16777239) == 16
    assert count_Set_Bits(16777240) == 16
    assert count_Set_Bits(16777241) == 16
    assert count_Set_Bits(16777242) == 16
    assert count_Set_Bits(16777243) == 16
    assert count_Set_Bits(16777244) == 16
    assert count_Set_Bits(16777245) == 16
    assert count_Set_Bits(16777246) == 16
    assert count_Set_Bits(16777247) == 16
    assert count_Set_Bits(16777248) == 16