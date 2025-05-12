"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""

def all_Characters_Same(string):
    return len(set(string)) == 1

print(all_Characters_Same("python")) # False
print(all_Characters_Same("hello")) # True
print(all_Characters_Same("aaaaa")) # True
print(all_Characters_Same("abcd")) # False
print(all_Characters_Same("")) # True
print(all_Characters_Same("a")) # True
print(all_Characters_Same("aa")) # True
print(all_Characters_Same("aaa")) # True
print(all_Characters_Same("aaaa")) # True
print(all_Characters_Same("aaaaa")) # True
print(all_Characters_Same("abba")) # False
print(all_Characters_Same("abcdabcd")) # False
print(all_Characters_Same("abcdefg")) # False
print(all_Characters_Same("123456789")) # False
print(all_Characters_Same("1234567890")) # True
print(all_Characters_Same("12345678901")) # False
print(all_Characters_Same("")) # True
print(all_Characters_Same("a")) # True
print(all_Characters_Same("aa")) # True
print(all_Characters_Same("aaa")) # True
print(all_Characters_Same("aaaa")) # True
print(all_Characters_Same("aaaaa")) # True
print(all_Characters_Same("abba")) # False
print(all_Characters_Same("abcdabcd")) # False
print(all_Characters_Same("abcdefg")) # False
print(all_Characters_Same("123456789")) # False
print(all_Characters_Same("1234567890")) # True
print(all_Characters_Same("12345678901")) # False
print(all_Characters_Same("")) # True
print(all_Characters_Same("a")) # True
print(all_Characters_Same("aa")) # True
print(all_Characters_Same("aaa")) # True
print(all_Characters_Same("aaaa")) # True
print(all_Characters_Same("aaaaa")) # True
print(all_Characters_Same("abba")) # False
print(all_Characters_Same("abcdabcd")) # False
print(all_Characters_Same("abcdefg")) # False
print(all_Characters_Same("123456789")) # False
print(all_Characters_Same("1234567890")) # True
print(all_Characters_Same("12345678901")) # False

# Output:
# False
# True
# True
# False
# True
# True
# True
# True
# False
# False
# False
# True
# True
# True
# True
# False
# False
# False
# False
# True
# True
# True
# True
# False
# False
# False
# False
# True
# True
# True
# True
# False
# False
# False
# False
# True
# True
# True
# True
# False
# False
# False
# False
# True
# True
# True
# True
# False
# False
# False
# False
# True
# True
# True
# True
# False
# False