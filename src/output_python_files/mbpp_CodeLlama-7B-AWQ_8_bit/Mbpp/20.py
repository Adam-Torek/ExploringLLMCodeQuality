"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""


def is_woodall(num):
    """
    :param num: int
    :return: bool
    """
    return num == sum(int(i) for i in str(num))


if __name__ == '__main__':
    print(is_woodall(383))
    print(is_woodall(123))
    print(is_woodall(1234))
    print(is_woodall(12345))
    print(is_woodall(123456))
    print(is_woodall(1234567))
    print(is_woodall(12345678))
    print(is_woodall(123456789))
    print(is_woodall(1234567890))
    print(is_woodall(12345678901))
    print(is_woodall(123456789012))
    print(is_woodall(1234567890123))
    print(is_woodall(12345678901234))
    print(is_woodall(123456789012345))
    print(is_woodall(1234567890123456))
    print(is_woodall(12345678901234567))
    print(is_woodall(123456789012345678))
    print(is_woodall(1234567890123456789))
    print(is_woodall(12345678901234567890))
    print(is_woodall(123456789012345678901))
    print(is_woodall(1234567890123456789012))
    print(is_woodall(12345678901234567890123))
    print(is_woodall(123456789012345678901234))
    print(is_woodall(1234567890123456789012345))
    print(is_woodall(12345678901234567890123456))
    print(is_woodall(123456789012345678901234567))
    print(is_woodall(1234567890123456789012345678))
    print(is_woodall(12345678901234567890123456789))
    print(is_woodall(123456789012345678901234567890))
    print(is_woodall(1234567890123456789012345678901))
    print(is_woodall(12345678901234567890123456789012))
    print(is_woodall(123456789012345678901234567890123))
    print(is_woodall(1234567890123456789012345678901234))
    print(