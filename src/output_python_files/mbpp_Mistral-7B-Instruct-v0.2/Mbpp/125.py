"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""
def find_length(binary_string):
    """
    :param binary_string: string of 0s and 1s
    :return: maximum difference between number of 0s and 1s in any sub-string
    """
    max_diff = 0
    zero_count = 0
    one_count = 0

    for bit in binary_string:
        if bit == '0':
            zero_count += 1
        else:
            one_count += 1

        diff = abs(zero_count - one_count)
        max_diff = max(max_diff, diff)

        # reset counters for next sub-string
        zero_count = 0
        one_count = 0

    # handle last sub-string
    zero_count = binary_string.count('0')
    one_count = binary_string.count('1')
    diff = abs(zero_count - one_count)
    max_diff = max(max_diff, diff)

    return max_diff

if __name__ == "__main__":
    binary_string = "11000010001"
    print(find_length(binary_string)) # 6
    binary_string = "11111111111111111111111111111111"
    print(find_length(binary_string)) # 0
    binary_string = "00000000000000000000000000000000"
    print(find_length(binary_string)) # 0
    binary_string = "10101010101010101010101010101010"
    print(find_length(binary_string)) # 2
    binary_string = "11111111111111111111111111111110"
    print(find_length(binary_string)) # 2
    binary_string = "11111111111111111111111111111101"
    print(find_length(binary_string)) # 1
    binary_string = "11111111111111111111111111111011"
    print(find_length(binary_string)) # 1
    binary_string = "11111111111111111111111111110111"
    print(find_length(binary_string)) # 0
    binary_string = "11111111111111111111111111101111"
    print(find_length(binary_string)) # 1
    binary_string = "11111111111111111111111111011111"
    print(find_length(binary_string)) # 1
    binary_string = "11111111111111111111111110111111"
    print(find_length(binary_string)) # 1
    binary_string = "11111111111111111111111101111111"
    print(find_length(binary_string)) # 1
    binary_string = "11111111111111111111111011111111"
    print(find_length(binary_string)) # 1
    binary_string = "11111111