"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""

def get_lucid(n):
    """
    :param n: int
    :return: list
    """
    lucid = []
    for i in range(1, n+1):
        if i == 1:
            lucid.append(i)
        else:
            if i % 2 == 0:
                lucid.append(i)
            else:
                if i % 3 == 0:
                    lucid.append(i)
                else:
                    if i % 5 == 0:
                        lucid.append(i)
    return lucid

print(get_lucid(10))
<file_sep>/0000-0015/0008-0015/0010.py
"""
Write a function to get the number of digits in a given integer.
assert get_digits(12345) == 5
"""

def get_digits(n):
    """
    :param n: int
    :return: int
    """
    return len(str(n))

print(get_digits(12345))
<file_sep>/0000-0015/0008-0015/0011.py
"""
Write a function to get the number of digits in a given integer.
assert get_digits(12345) == 5
"""

def get_digits(n):
    """
    :param n: int
    :return: int
    """
    return len(str(n))

print(get_digits(12345))
<file_sep>/0000-0015/0008-0015/0012.py
"""
Write a function to get the number of digits in a given integer.
assert get_digits(12345) == 5
"""

def get_digits(n):
    """
    :param n: int
    :return: int
    """
    return len(str(n))

print(get_digits(12345))
<file_sep>/0000-0015/0008-0015/0013.py
"""
Write a function to get the number of digits in a given integer.
assert get_digits(12345) == 5
"""

def get_digits(n):
    """
    :param n: int
    :return: int
    """
    return len(str(n))

print(get_digits(12345))
<file_sep>/0000-0015/0008-0015/0014.py
"""
Write a function to get the number of digits in a given integer.
assert get_digits(12345) == 5
"""

def get_digits(n):
    """
    :param n: int
    :return: int
    """
    return len(str(n))

print(get_digits(12345))
<file_sep>/0000-0015/0008-0015/0015.py
"""
Write a function to get the number of digits in a given integer.
assert get_digits(12345) == 5
"""

def get_digits(n):
    """
    :param n: int
    :return: int
    """
    return len(str(n))

print(get_digits(12345))
<file_sep>/0000-0015/0008-0015/0009.py
"""
Write a function to get the number of digits in a given integer.
assert get_digits(12345) == 5
"""

def get_digits(n):
    """
    :param n: int
    :return: int
    """
    return len(str(n))

print(get_digits(12345))
<file_sep>/0000-0015/0008-0015/0011.py
"""
Write a function to get the number of digits in a given integer.
assert get_digits(12345) == 5
"""

def get_digits