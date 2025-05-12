def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) != len(b):
        return False
    if a == b:
        return True
    a = a + a
    for i in range(len(b)):
        if a.find(b) != -1:
            return True
        a = a[1:]
    return False


# Test cases
print(cycpattern_check("abcd", "abd")) # False
print(cycpattern_check("hello", "ell")) # True
print(cycpattern_check("whassup", "psus")) # False
print(cycpattern_check("abab", "baa")) # True
print(cycpattern_check("efef", "eeff")) # False
print(cycpattern_check("himenss", "simen")) # True
print(cycpattern_check("abcd", "abd")) # False
print(cycpattern_check("hello", "ell")) # True
print(cycpattern_check("whassup", "psus")) # False
print(cycpattern_check("abab", "baa")) # True
print(cycpattern_check("efef", "eeff")) # False
print(cycpattern_check("himenss", "simen")) # True

# Edge cases
print(cycpattern_check("", "")) # False
print(cycpattern_check("a", "a")) # True
print(cycpattern_check("abc", "cba")) # True
print(cycpattern_check("abc", "abcd")) # False
print(cycpattern_check("abc", "abcd")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cycpattern_check("abc", "abdc")) # False
print(cyc