"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""


def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if sum(int(x) for x in s[i:j+1]) == j-i+1:
                count += 1
    return count


if __name__ == '__main__':
    print(count_Substrings('112112'))
    print(count_Substrings('123456789'))
    print(count_Substrings('1234567890'))
    print(count_Substrings('12345678901'))
    print(count_Substrings('123456789012'))
    print(count_Substrings('1234567890123'))
    print(count_Substrings('12345678901234'))
    print(count_Substrings('123456789012345'))
    print(count_Substrings('1234567890123456'))
    print(count_Substrings('12345678901234567'))
    print(count_Substrings('123456789012345678'))
    print(count_Substrings('1234567890123456789'))
    print(count_Substrings('12345678901234567890'))
    print(count_Substrings('123456789012345678901'))
    print(count_Substrings('1234567890123456789012'))
    print(count_Substrings('12345678901234567890123'))
    print(count_Substrings('123456789012345678901234'))
    print(count_Substrings('1234567890123456789012345'))
    print(count_Substrings('12345678901234567890123456'))
    print(count_Substrings('123456789012345678901234567'))
    print(count_Substrings('1234567890123456789012345678'))
    print(count_Substrings('12345678901234567890123456789'))
    print(count_Substrings('123456789012345678901234567890'))
    print(count_Substrings('1234567890123456789012345678901'))
    print(count_Substrings('12345678901234567890123456789012'))
    print(count_Substrings('123456789012345678901234567890123'))
    print(count_Substrings('1234567890123456789012345678901234'))
    print(count_Substrings('12345678901234567890123456789012345'))
    print(count_Substrings('