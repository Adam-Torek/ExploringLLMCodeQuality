"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""

def differ_At_One_Bit_Pos(num1, num2):
    """
    This function checks whether two numbers differ at one bit position only or not.
    """
    # Convert the two numbers to binary
    num1_bin = bin(num1)[2:]
    num2_bin = bin(num2)[2:]

    # Find the index of the first 1 in num1_bin
    first_1_index = num1_bin.find('1')

    # Find the index of the first 1 in num2_bin
    second_1_index = num2_bin.find('1')

    # Check if the two numbers differ at one bit position only
    if first_1_index != second_1_index:
        return True
    else:
        return False