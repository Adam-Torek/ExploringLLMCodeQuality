"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""
def find_length(binary_string):
    """
    :param binary_string: str
    :return: int
    """
    max_diff = 0
    zero_count = 0
    one_count = 0
    for bit in binary_string:
        if bit == '0':
            zero_count += 1
            one_count = 0
        else:
            one_count += 1
            zero_count = 0
        diff = abs(zero_count - one_count)
        max_diff = max(max_diff, diff)
    return max_diff

if __name__ == "__main__":
    binary_string = "11000010001"
    print(find_length(binary_string))
    assert find_length("11000010001") == 6
    assert find_length("11111111111") == 0
    assert find_length("00000000000") == 0
    assert find_length("10101010101") == 2
    assert find_length("11111111110") == 1
    assert find_length("00000000011") == 2
    assert find_length("111111111111") == 0
    assert find_length("000000000000") == 0
    assert find_length("1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010