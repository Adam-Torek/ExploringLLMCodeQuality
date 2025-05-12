"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""
def all_Characters_Same(string):
    return len(set(string)) == 1

# Test cases
print(all_Characters_Same("python")) # False
print(all_Characters_Same("hello")) # False
print(all_Characters_Same("aaa")) # True
print(all_Characters_Same("a")) # True
print(all_Characters_Same("")) # True
print(all_Characters_Same("abcd")) # False
print(all_Characters_Same("abab")) # True
print(all_Characters_Same("abba")) # False
print(all_Characters_Same("12345")) # False
print(all_Characters_Same("111111")) # True
print(all_Characters_Same("123456")) # False
print(all_Characters_Same("1234567")) # False
print(all_Characters_Same("12345678")) # False
print(all_Characters_Same("123456789")) # False
print(all_Characters_Same("1234567890")) # False
print(all_Characters_Same("12345678901")) # True
print(all_Characters_Same("123456789012")) # False
print(all_Characters_Same("1234567890123")) # False
print(all_Characters_Same("12345678901234")) # False
print(all_Characters_Same("123456789012345")) # False
print(all_Characters_Same("1234567890123456")) # False
print(all_Characters_Same("12345678901234567")) # False
print(all_Characters_Same("123456789012345678")) # False
print(all_Characters_Same("1234567890123456789")) # False
print(all_Characters_Same("12345678901234567890")) # False
print(all_Characters_Same("123456789012345678901")) # False
print(all_Characters_Same("1234567890123456789012")) # False
print(all_Characters_Same("12345678901234567890123")) # False
print(all_Characters_Same("123456789012345678901234")) # False
print(all_Characters_Same("1234567890123456789012345")) # False
print(all_Characters_Same("12345678901234567890123456")) # False
print(all_Characters_Same("123456789012345678901234567")) # False
print(all_Characters_Same("1234567890123456789012345678")) # False
print(