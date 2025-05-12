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
        if s[i] == s[i + 1] == s[i + 2]:
            return False
    return True


# Test cases
print(is_happy("abcd"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False
print(is_happy("abc"))  # False
print(is_happy("abcabc"))  # True
print(is_happy("abca"))  # False
print(is_happy("abcaa"))  # False
print(is_happy("abcaaab"))  # False
print(is_happy("abcaaabc"))  # True
print(is_happy("abcaaabcd"))  # False
print(is_happy("abcaaabcde"))  # False
print(is_happy("abcaaabcdee"))  # True
print(is_happy("abcaaabcdef"))  # False
print(is_happy("abcaaabcdefg"))  # False
print(is_happy("abcaaabcdefgh"))  # True
print(is_happy("abcaaabcdefghi"))  # False
print(is_happy("abcaaabcdefghih"))  # True
print(is_happy("abcaaabcdefghij"))  # False
print(is_happy("abcaaabcdefghijk"))  # True
print(is_happy("abcaaabcdefghijkl"))  # False
print(is_happy("abcaaabcdefghijklm"))  # True
print(is_happy("abcaaabcdefghijklmn"))  # False
print(is_happy("abcaaabcdefghijklmno"))  # True
print(is_happy("abcaaabcdefghijklmnoo"))  # False
print(is_happy("abcaaabcdefghijklmnoop"))  # True
print(is_happy("abcaaabcdefghijklmnoopq"))  # False
print(is_happy("abcaaabcdefghijklmnoopqr"))  # True
print(is_happy("abcaaabcdefghijklmnoopqrs"))  # False
print(is_happy("abcaaabcdefghijklmnoopqrst"))  # True
print(is_happy("abcaaabcdefghijklmnoopqrstu"))  # False
print(is_happy("abcaaabcdefghijklmnoopqrstuv"))  # True
print(is_happy("abcaaabcdefghijklmnoopqrstuvw"))  # False
print(is_happy("abcaaabcdefghijklmnoopqr