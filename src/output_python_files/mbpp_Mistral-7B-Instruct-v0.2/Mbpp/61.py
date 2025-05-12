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
assert count_Substrings('123') == 1
assert count_Substrings('12345') == 2
assert count_Substrings('11112222') == 6
assert count_Substrings('12345678910') == 11
assert count_Substrings('1234567891011') == 13
assert count_Substrings('12345678910111') == 15
assert count_Substrings('123456789101111') == 18
assert count_Substrings('1234567891011111') == 21
assert count_Substrings('12345678910111111') == 24
assert count_Substrings('123456789101111111') == 27
assert count_Substrings('1234567891011111111') == 30
assert count_Substrings('12345678910111111111') == 33
assert count_Substrings('123456789101111111111') == 36
assert count_Substrings('1234567891011111111111') == 39
assert count_Substrings('12345678910111111111111') == 42
assert count_Substrings('123456789101111111111111') == 45
assert count_Substrings('1234567891011111111111111') == 48
assert count_Substrings('12345678910111111111111111') == 51
assert count_Substrings('123456789101111111111111111') == 54
assert count_Substrings('1234567891011111111111111111') == 57
assert count_Substrings('12345678910111111111111111111') == 60
assert count_Substrings('123456789101111111111111111111') == 63
assert count_Substrings('1234567891011111111111111111111') == 66
assert count_Substrings('12345678910111111111111111111111') == 69
assert count_Substrings('123456789101111111111111111111111') == 72
assert count_Substrings('1234567891011111111111111111111111') == 75
assert count_Substrings('12345678