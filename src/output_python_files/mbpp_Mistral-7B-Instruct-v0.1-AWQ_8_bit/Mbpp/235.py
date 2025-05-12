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
    num_binary = bin(num)[2:]

    # Find the index of the first even bit
    even_bit_index = num_binary.find('0', start=1)

    # If there is no even bit, return the original number
    if even_bit_index == -1:
        return num

    # Set all even bits to 1
    num_binary = num_binary[:even_bit_index] + '1' + num_binary[even_bit_index:]

    # Convert the binary number back to int
    return int(num_binary, 2)


if __name__ == '__main__':
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(15) == 15
    assert even_bit_set_number(20) == 20
    assert even_bit_set_number(25) == 25