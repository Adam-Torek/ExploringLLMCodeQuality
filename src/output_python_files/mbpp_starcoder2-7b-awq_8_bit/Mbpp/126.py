"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_common_divisors(a,b):
    """
    >>> sum_common_divisors(10,15)
    6
    """
    return sum(common_divisors(a,b))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/python_code_challenges/code_challenge_001.py
"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_common_divisors(a,b):
    """
    >>> sum_common_divisors(10,15)
    6
    """
    return sum(common_divisors(a,b))

def common_divisors(a,b):
    """
    >>> common_divisors(10,15)
    [1, 5]
    """
    return [x for x in range(1,min(a,b)+1) if a%x==0 and b%x==0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/python_code_challenges/code_challenge_002.py
"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_common_divisors(a,b):
    """
    >>> sum_common_divisors(10,15)
    6
    """
    return sum(common_divisors(a,b))

def common_divisors(a,b):
    """
    >>> common_divisors(10,15)
    [1, 5]
    """
    return [x for x in range(1,min(a,b)+1) if a%x==0 and b%x==0]

def sum_common_divisors_2(a,b):
    """
    >>> sum_common_divisors_2(10,15)
    6
    """
    return sum(common_divisors_2(a,b))

def common_divisors_2(a,b):
    """
    >>> common_divisors_2(10,15)
    [1, 5]
    """
    return [x for x in range(1,min(a,b)+1) if a%x==0 and b%x==0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/python_code_challenges/code_challenge_003.py
"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_common_divisors(a,b):
    """
    >>> sum_common_divisors(10,15)
    6
    """
    return sum(common_divisors(a,b))

def common_divisors(a,b):
    """
    >>> common_divisors(10,15)
    [1, 5]
    """
    return [x for x in range(1,min(a,b)+1) if a%x==0 and b%x==0]

def sum_common_divisors_2(a,b):
    """
    >>> sum_common_divisors_2(10,15)
    6
    """
    return sum(common_divisors_2(a,b))

def common_divisors_2(a,b):
    """
    >>> common_divisors_2(10,15)
    [1, 5]
    """
    return [x for x in range(1,min(a,b)+1) if a%x==0 and b%x==0]

def sum_common_divisors_3(a,b):
    """
    >>> sum_common_divisors_3(10,15)
    6
    """
    return sum(common_divisors_3(a,b))

def common_divisors_3(a,b):
    """
    >>> common_divisors_