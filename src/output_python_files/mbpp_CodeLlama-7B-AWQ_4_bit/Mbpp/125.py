"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""


def find_length(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    max_diff = 0
    count_0 = 0
    count_1 = 0

    for i in range(len(s)):
        if s[i] == '0':
            count_0 += 1
        else:
            count_1 += 1

        max_diff = max(max_diff, count_0 - count_1)

    return max_diff


if __name__ == '__main__':
    print(find_length("11000010001"))
    print(find_length("110000100011"))
    print(find_length("1100001000111"))
    print(find_length("11000010001111"))
    print(find_length("110000100011111"))
    print(find_length("1100001000111111"))
    print(find_length("11000010001111111"))
    print(find_length("110000100011111111"))
    print(find_length("1100001000111111111"))
    print(find_length("11000010001111111111"))
    print(find_length("110000100011111111111"))
    print(find_length("1100001000111111111111"))
    print(find_length("11000010001111111111111"))
    print(find_length("110000100011111111111111"))
    print(find_length("1100001000111111111111111"))
    print(find_length("11000010001111111111111111"))
    print(find_length("110000100011111111111111111"))
    print(find_length("1100001000111111111111111111"))
    print(find_length("11000010001111111111111111111"))
    print(find_length("110000100011111111111111111111"))
    print(find_length("1100001000111111111111111111111"))
    print(find_length("11000010001111111111111111111111"))
    print(find_length("110000100011111111111111111111111"))
    print(find_length("1100001000111111111111111111111111"))
    print(find_length("11000010001111111111111111111111111"))
    print(find_length("11