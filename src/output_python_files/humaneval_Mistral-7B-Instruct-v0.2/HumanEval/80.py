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
print(is_happy("a"))
print(is_happy("aa"))
print(is_happy("abcd"))
print(is_happy("aabb"))
print(is_happy("adb"))
print(is_happy("xyy"))
print(is_happy("abcdefghijklmnopqrstuvwxyz"))
print(is_happy("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
print(is_happy("abc1234567890abc1234567890"))
print(is_happy("abc1234567890abc1234567890abc1234567890"))
print(is_happy("abc1234567890abc1234567890abc1234567890abc1234567890"))
print(is_happy("abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890"))
print(is_happy("abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890"))
print(is_happy("abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890"))
print(is_happy("abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc1234567890abc123