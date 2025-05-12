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
        if s[i] == s[i+1] == s[i+2]:
            return False
    return True


# Test cases
print(is_happy("aabb")) # False
print(is_happy("abc")) # True
print(is_happy("abcd")) # True
print(is_happy("aaa")) # False
print(is_happy("xyy")) # False
print(is_happy("abca")) # False
print(is_happy("abcaa")) # False
print(is_happy("abcb")) # True
print(is_happy("abc")) # True
print(is_happy("abcabc")) # False
print(is_happy("abcab")) # True
print(is_happy("abcabcabc")) # True
print(is_happy("abcabcab")) # False
print(is_happy("abcabcabcd")) # True
print(is_happy("abcabcabcdc")) # False
print(is_happy("abcabcabcde")) # False
print(is_happy("abcabcabcdea")) # True
print(is_happy("abcabcabcdeab")) # False
print(is_happy("abcabcabcdeabcd")) # True
print(is_happy("abcabcabcdeabc")) # False
print(is_happy("abcabcabcdeabcde")) # False
print(is_happy("abcabcabcdeabcdef")) # True
print(is_happy("abcabcabcdeabcdefg")) # False
print(is_happy("abcabcabcdeabcdefgf")) # True
print(is_happy("abcabcabcdeabcdefgh")) # False
print(is_happy("abcabcabcdeabcdefghi")) # True
print(is_happy("abcabcabcdeabcdefghij")) # False
print(is_happy("abcabcabcdeabcdefghijk")) # True
print(is_happy("abcabcabcdeabcdefghijkl")) # False
print(is_happy("abcabcabcdeabcdefghijklm")) # True
print(is_happy("abcabcabcdeabcdefghijklmn")) # False
print(is_happy("abcabcabcdeabcdefghijklmno")) # True
print(is_happy("abcabcabcdeabcdefghijklmnp")) # False
print(is_happy("abcabcabcdeabcdefghijklmnpq")) # True
print(is_happy("abcabcabcdeabcdefghijklmnpqr")) # False
print(is_happy("abcabcabcdeabcdefghijklmnpqrs")) # True
print(is_happy("abcabcabcdeabcdefghijklmnpqrst")) # False
print(is_happy("abcabcabcdeabcdefghijklmnpqrstu")) # True
print(is_h