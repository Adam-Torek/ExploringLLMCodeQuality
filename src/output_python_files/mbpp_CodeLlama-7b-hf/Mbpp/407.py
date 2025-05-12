"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""


def rearrange_bigger(number):
    """
    :param number: int
    :return: int
    """
    number = str(number)
    number_list = list(number)
    number_list.sort(reverse=True)
    number_list = ''.join(number_list)
    return int(number_list)


if __name__ == '__main__':
    print(rearrange_bigger(12))
    print(rearrange_bigger(21))
    print(rearrange_bigger(123))
    print(rearrange_bigger(132))
    print(rearrange_bigger(231))
    print(rearrange_bigger(321))
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
    print(rearrange_bigger(12345678901234567890123456