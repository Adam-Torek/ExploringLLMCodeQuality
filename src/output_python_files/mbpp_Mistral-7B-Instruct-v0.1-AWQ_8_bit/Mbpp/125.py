"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""

def find_length(s):
    max_diff = 0
    for i in range(len(s)):
        count_zero = 0
        count_one = 0
        for j in range(i, len(s)):
            if s[j] == '0':
                count_zero += 1
            else:
                count_one += 1
            diff = abs(count_zero - count_one)
            max_diff = max(max_diff, diff)
    return max_diff

# test
assert find_length("11000010001") == 6