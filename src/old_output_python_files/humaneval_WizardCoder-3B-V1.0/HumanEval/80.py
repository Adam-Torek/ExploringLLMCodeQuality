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

def is_happy_helper(s, index, seen):
    if index == len(s):
        return True
    if s[index] in seen:
        return False
    seen.add(s[index])
    return is_happy_helper(s, index + 1, seen)

def is_happy(s):
    if len(s) < 3:
        return False
    seen = set()
    return is_happy_helper(s, 0, seen)

# Test cases
print(is_happy("a"))  # False
print(is_happy("aa"))  # False
print(is_happy("abcd"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False<|endoftext|>