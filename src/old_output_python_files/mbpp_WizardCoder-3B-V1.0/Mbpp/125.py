"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""

def find_length(binary_string):
    count_0 = 0
    count_1 = 0
    max_diff = 0

    for bit in binary_string:
        if bit == '0':
            count_0 += 1
        else:
            count_1 += 1

        diff = abs(count_0 - count_1)
        max_diff = max(max_diff, diff)

    return max_diff

# Test cases
print(find_length("11000010001"))  # Output: 6<|endoftext|>