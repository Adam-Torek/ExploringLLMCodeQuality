def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i, char in enumerate(s):
        if i % 2 == 0 and char.isalpha() and char in vowels and char.isupper():
            count += 1
    return count

# Test cases
print(count_upper('aBCdEf')) # 1
print(count_upper('abcdefg')) # 0
print(count_upper('dBBE')) # 0
print(count_upper('AeIoU')) # 3
print(count_upper('AeI')) # 1
print(count_upper('AeI123')) # 0
print(count_upper('AeIou')) # 3
print(count_upper('AeIou123')) # 0
print(count_upper('AeIou12345')) # 0
print(count_upper('AeIou123456')) # 0
print(count_upper('AeIou1234567')) # 0
print(count_upper('AeIou12345678')) # 0
print(count_upper('AeIou123456789')) # 0
print(count_upper('AeIou1234567890')) # 0
print(count_upper('AeIou12345678901')) # 0
print(count_upper('AeIou123456789012')) # 0
print(count_upper('AeIou1234567890123')) # 0
print(count_upper('AeIou12345678901234')) # 0
print(count_upper('AeIou123456789012345')) # 0
print(count_upper('AeIou1234567890123456')) # 0
print(count_upper('AeIou12345678901234567')) # 0
print(count_upper('AeIou123456789012345678')) # 0
print(count_upper('AeIou1234567890123456789')) # 0
print(count_upper('AeIou12345678901234567890')) # 0
print(count_upper('AeIou123456789012345678901')) # 0
print(count_upper('AeIou1234567890123456789012')) # 0
print(count_upper('AeIou12345678901234567890123')) # 0
print(count_upper('AeIou123456789012345678901234')) # 0
print(count_upper('AeIou1234567890123456789012345')) # 0
print(count_upper('AeIou12345678901234567890123456')) # 0
print(count_upper('AeIou123456789012345678901234567')) # 0
print(count_upper('AeIou12345678901