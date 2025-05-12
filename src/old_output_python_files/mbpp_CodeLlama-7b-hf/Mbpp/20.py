"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""


def is_woodall(num):
    """
    :param num: int
    :return: bool
    """
    if num < 100:
        return False
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] != num_str[i + 1]:
            return False
    return True


if __name__ == '__main__':
    print(is_woodall(383))
    print(is_woodall(3833))
    print(is_woodall(38333))
    print(is_woodall(383333))
    print(is_woodall(3833333))
    print(is_woodall(38333333))
    print(is_woodall(383333333))
    print(is_woodall(3833333333))
    print(is_woodall(38333333333))
    print(is_woodall(383333333333))
    print(is_woodall(3833333333333))
    print(is_woodall(38333333333333))
    print(is_woodall(383333333333333))
    print(is_woodall(3833333333333333))
    print(is_woodall(38333333333333333))
    print(is_woodall(383333333333333333))
    print(is_woodall(3833333333333333333))
    print(is_woodall(38333333333333333333))
    print(is_woodall(383333333333333333333))
    print(is_woodall(3833333333333333333333))
    print(is_woodall(38333333333333333333333))
    print(is_woodall(383333333333333333333333))
    print(is_woodall(3833333333333333333333333))
    print(is_woodall(38333333333333333333333333))
    print(is_woodall(383333333333333333333333333))
    print(is_woodall(3833333333333333333333333333))
    print(is_woodall(38333333333333333333333333333))
    print(is_woodall(383333333333333333333333333333))
    print(is_woodall(3833333333333333333333333333333))
    print(is_woodall(38333333333333333333333333333333))
    print(is_woodall(383333333333333333333333333333333))
    print(is_woodall(383333