"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""
def differ_At_One_Bit_Pos(num1, num2):
    """
    :param num1: int
    :param num2: int
    :return: bool
    """
    xor = num1 ^ num2
    count = 0
    while xor:
        if xor & 1:
            count += 1
        xor >>= 1
    return count == 1

if __name__ == "__main__":
    assert differ_At_One_Bit_Pos(13, 9) == True
    assert differ_At_One_Bit_Pos(1, 2) == True
    assert differ_At_One_Bit_Pos(1, 1) == False
    assert differ_At_One_Bit_Pos(1, 3) == False
    assert differ_At_One_Bit_Pos(1, 4) == False
    assert differ_At_One_Bit_Pos(1, 5) == False
    assert differ_At_One_Bit_Pos(1, 6) == False
    assert differ_At_One_Bit_Pos(1, 7) == False
    assert differ_At_One_Bit_Pos(1, 8) == False
    assert differ_At_One_Bit_Pos(1, 10) == False
    assert differ_At_One_Bit_Pos(1, 11) == False
    assert differ_At_One_Bit_Pos(1, 12) == False
    assert differ_At_One_Bit_Pos(1, 13) == False
    assert differ_At_One_Bit_Pos(1, 14) == False
    assert differ_At_One_Bit_Pos(1, 15) == False
    assert differ_At_One_Bit_Pos(1, 16) == False
    assert differ_At_One_Bit_Pos(1, 17) == False
    assert differ_At_One_Bit_Pos(1, 18) == False
    assert differ_At_One_Bit_Pos(1, 19) == False
    assert differ_At_One_Bit_Pos(1, 20) == False
    assert differ_At_One_Bit_Pos(1, 21) == False
    assert differ_At_One_Bit_Pos(1, 22) == False
    assert differ_At_One_Bit_Pos(1, 23) == False
    assert differ_At_One_Bit_Pos(1, 24) == False
    assert differ_At_One_Bit_Pos(1, 25) == False
    assert differ_At_One_Bit_Pos(1, 26) == False
    assert differ_At_One_Bit_Pos(1, 27) == False
    assert differ_At_One_Bit_Pos(1, 28) == False
    assert differ_At_One_Bit_Pos(1, 29) == False
    assert differ_At_One_Bit_Pos(1, 30) == False
    assert differ_At_One_Bit_Pos(1, 31) == False
    assert differ_At_One_Bit_Pos(1, 32) == False
    assert differ_At_One_Bit_Pos(1, 33) == False
    assert differ_At_One_Bit_Pos(1, 34) == False
    assert differ_At_One_Bit_Pos(1, 35) == False
    assert differ_At_One_Bit_Pos(1, 36) == False
    assert differ_At_One_Bit_Pos(1, 37) == False
    assert differ_At_One_Bit_Pos(1, 38) == False
    assert differ_At_One_Bit_Pos(1, 39) == False
    assert differ_At_One_Bit_Pos(1, 40) == False
    assert differ_At_One_Bit_Pos(1, 41) == False
    assert differ_At_One_Bit_Pos(1, 42)