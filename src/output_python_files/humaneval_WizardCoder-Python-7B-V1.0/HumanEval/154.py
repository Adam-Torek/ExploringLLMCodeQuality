def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def rotate_string(s):
        return s[1:] + s[0]

    def is_substring(a, b):
        return b in a

    def is_rotation(a, b):
        return is_substring(a, b) or is_substring(rotate_string(a), b)

    return is_rotation(a, b)


# Test cases
print(cycpattern_check("abcd", "abd"))  # False
print(cycpattern_check("hello", "ell"))  # True
print(cycpattern_check("whassup", "psus"))  # False
print(cycpattern_check("abab", "baa"))  # True
print(cycpattern_check("efef", "eeff"))  # False
print(cycpattern_check("himenss", "simen"))  # True
print(cycpattern_check("abcd", "abcd"))  # True
print(cycpattern_check("abcd", "abdc"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdae"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdae"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdea"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdea"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdea"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdea"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdea"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdea"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdea"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdea"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdea"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check("abcde", "cdea"))  # False
print(cycpattern_check("abcde", "cdea"))  # True
print(cycpattern_check