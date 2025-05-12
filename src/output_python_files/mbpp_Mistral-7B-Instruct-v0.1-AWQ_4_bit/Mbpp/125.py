"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""

def find_length(s):
    """
    :type s: str
    :rtype: int
    """
    max_diff = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            diff = abs(s.count("0")[i:j] - s.count("1")[i:j])
            if diff > max_diff:
                max_diff = diff
    return max_diff


if __name__ == '__main__':
    s = "11000010001"
    print(find_length(s))