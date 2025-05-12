def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = a.lower()
    b = b.lower()
    a_list = list(a)
    b_list = list(b)
    a_set = set(a_list)
    b_set = set(b_list)
    if len(a_set) == 1 and len(b_set) == 1:
        return True
    else:
        for i in range(len(a_list)):
            if a_list[i] != b_list[i]:
                return False
        return True