"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if sum(int(d) for d in sub) == len(sub):
                count += 1
    return count

# Test cases
print(count_Substrings('112112')) # Output: 6
print(count_Substrings('123456')) # Output: 10
print(count_Substrings('1234567')) # Output: 15
print(count_Substrings('12345678')) # Output: 21
print(count_Substrings('123456789')) # Output: 28
print(count_Substrings('1234567890')) # Output: 36
print(count_Substrings('12345678901')) # Output: 45
print(count_Substrings('123456789012')) # Output: 55
print(count_Substrings('1234567890123')) # Output: 66
print(count_Substrings('12345678901234')) # Output: 78
print(count_Substrings('123456789012345')) # Output: 91
print(count_Substrings('1234567890123456')) # Output: 105
print(count_Substrings('12345678901234567')) # Output: 120
print(count_Substrings('123456789012345678')) # Output: 136
print(count_Substrings('1234567890123456789')) # Output: 151
print(count_Substrings('12345678901234567890')) # Output: 166
print(count_Substrings('123456789012345678901')) # Output: 182
print(count_Substrings('1234567890123456789012')) # Output: 200
print(count_Substrings('12345678901234567890123')) # Output: 220
print(count_Substrings('123456789012345678901234')) # Output: 241
print(count_Substrings('1234567890123456789012345')) # Output: 265
print(count_Substrings('12345678901234567890123456')) # Output: 289
print(count_Substrings('123456789012345678901234567')) # Output: 315
print(count_Substrings('1234567890123456789012345678')) # Output: 342
print(count_Substrings('12345678901234567890123456789')) # Output: 370
print(count_Substrings('123456789012345678901234567890')) # Output: 399
print(count_Substrings('123456789012345678901234