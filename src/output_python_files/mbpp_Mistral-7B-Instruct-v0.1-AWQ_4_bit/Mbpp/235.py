"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""

def even_bit_set_number(num):
    """
    This function sets all even bits of a given number.
    :param num: int
    :return: int
    """
    # Convert the number to binary
    binary_num = bin(num)[2:]

    # Find the index of the first even bit
    even_bit_index = binary_num.find('0', binary_num.find('1'))

    # If there is no even bit, return the original number
    if even_bit_index == -1:
        return num

    # Set all even bits to 1
    for i in range(even_bit_index, len(binary_num), 2):
        binary_num = binary_num[:i] + '1' + binary_num[i+1:]

    # Convert the binary number back to decimal
    result = int(binary_num, 2)

    return result


if __name__ == '__main__':
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(15) == 15
    assert even_bit_set_number(20) == 20
    assert even_bit_set_number(25) == 25