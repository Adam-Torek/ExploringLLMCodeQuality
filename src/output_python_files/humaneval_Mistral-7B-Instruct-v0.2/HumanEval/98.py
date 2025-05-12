def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = "aeiouAEIOU"
    count = 0
    for i, char in enumerate(s):
        if i % 2 == 0 and char in vowels and char.isupper():
            count += 1
    return count

# Test cases
print(count_upper("aBCdEf")) # 1
print(count_upper("abcdefg")) # 0
print(count_upper("dBBE")) # 0
print(count_upper("AeIoU")) # 3
print(count_upper("Hello World")) # 1
print(count_upper("12345")) # 0
print(count_upper("")) # 0
print(count_upper("Python")) # 0
print(count_upper("PyThOn")) # 1