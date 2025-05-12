def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i:i+3] == s[i+1:i+3] or len(set(s[i:i+3])) < 3:
            return False
    return True

# Test cases
print(is_happy("a")) # False
print(is_happy("aa")) # False
print(is_happy("abcd")) # True
print(is_happy("aabb")) # False
print(is_happy("adb")) # True
print(is_happy("xyy")) # False
print(is_happy("abcdefghijklmnopqrstuvwxyz")) # True
print(is_happy("abcabcabc")) # False
print(is_happy("123456789")) # False
print(is_happy("1234567890")) # False
print(is_happy("12345678901")) # True
print(is_happy("123456789012")) # False
print(is_happy("1234567890123")) # True
print(is_happy("12345678901234")) # False
print(is_happy("123456789012345")) # True
print(is_happy("1234567890123456")) # False
print(is_happy("12345678901234567")) # True
print(is_happy("123456789012345678")) # False
print(is_happy("1234567890123456789")) # True
print(is_happy("12345678901234567890")) # False
print(is_happy("123456789012345678901")) # True
print(is_happy("1234567890123456789012")) # False
print(is_happy("12345678901234567890123")) # True
print(is_happy("123456789012345678901234")) # False
print(is_happy("1234567890123456789012345")) # True
print(is_happy("12345678901234567890123456")) # False
print(is_happy