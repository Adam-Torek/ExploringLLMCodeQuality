"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
def count_Substrings(string):
    count = 0
    for i in range(len(string)):
        substring = string[i:]
        sum_digits = sum(int(digit) for digit in substring)
        if sum_digits == len(substring):
            count += 1
    return count

assert count_Substrings('112112') == 6
assert count_Substrings('1234') == 1
assert count_Substrings('123012') == 2
assert count_Substrings('123456789') == 9
assert count_Substrings('12345678910') == 10
assert count_Substrings('1234567891011') == 11
assert count_Substrings('123456789101112') == 12
assert count_Substrings('12345678910111213') == 13
assert count_Substrings('1234567891011121314') == 14
assert count_Substrings('123456789101112131415') == 15
assert count_Substrings('12345678910111213141516') == 16
assert count_Substrings('1234567891011121314151617') == 17
assert count_Substrings('123456789101112131415161718') == 18
assert count_Substrings('12345678910111213141516171819') == 19
assert count_Substrings('1234567891011121314151617181920') == 20
assert count_Substrings('123456789101112131415161718192021') == 21
assert count_Substrings('12345678910111213141516171819202122') == 22
assert count_Substrings('1234567891011121314151617181920212223') == 23
assert count_Substrings('123456789101112131415161718192021222334') == 24
assert count_Substrings('12345678910111213141516171819202122233445') == 25
assert count_Substrings('1234567891011121314151617181920212223344556') == 26
assert count_Substrings('123456789101112131415161718192021222334455667') == 27
assert count_Substrings('12345678910111213141516171819202122233445566778') == 28
assert count_Substrings('1234567891011121314151617181920212223344556677