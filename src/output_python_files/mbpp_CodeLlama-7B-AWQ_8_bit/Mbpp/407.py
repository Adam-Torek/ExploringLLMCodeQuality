"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""


def rearrange_bigger(num):
    """
    :param num: int
    :return: int
    """
    num = str(num)
    num_list = list(num)
    num_list.sort(reverse=True)
    num_list = ''.join(num_list)
    return int(num_list)


if __name__ == '__main__':
    print(rearrange_bigger(12))
    print(rearrange_bigger(123))
    print(rearrange_bigger(1234))
    print(rearrange_bigger(12345))
    print(rearrange_bigger(123456))
    print(rearrange_bigger(1234567))
    print(rearrange_bigger(12345678))
    print(rearrange_bigger(123456789))
    print(rearrange_bigger(1234567890))
    print(rearrange_bigger(12345678901))
    print(rearrange_bigger(123456789012))
    print(rearrange_bigger(1234567890123))
    print(rearrange_bigger(12345678901234))
    print(rearrange_bigger(123456789012345))
    print(rearrange_bigger(1234567890123456))
    print(rearrange_bigger(12345678901234567))
    print(rearrange_bigger(123456789012345678))
    print(rearrange_bigger(1234567890123456789))
    print(rearrange_bigger(12345678901234567890))
    print(rearrange_bigger(123456789012345678901))
    print(rearrange_bigger(1234567890123456789012))
    print(rearrange_bigger(12345678901234567890123))
    print(rearrange_bigger(123456789012345678901234))
    print(rearrange_bigger(1234567890123456789012345))
    print(rearrange_bigger(12345678901234567890123456))
    print(rearrange_bigger(123456789012345678901234567))
    print(rearrange_bigger(1234567890123456789012345678))
    print(rearrange_bigger(12345678901234567890123456789))
    print(rearrange_bigger(123456789012345678901234567890))
    print(rearrange_bigger(1234567890123456789012345678901))
    print(rearrange_bigger(123456789012345678901