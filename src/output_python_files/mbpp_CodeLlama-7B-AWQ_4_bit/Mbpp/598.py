"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""


def armstrong_number(number):
    """
    :param number: int
    :return: bool
    """
    if number < 0:
        return False
    else:
        num_list = list(str(number))
        num_len = len(num_list)
        num_sum = 0
        for i in num_list:
            num_sum += int(i) ** num_len
        if num_sum == number:
            return True
        else:
            return False


if __name__ == '__main__':
    print(armstrong_number(153))
    print(armstrong_number(123))
    print(armstrong_number(1234))
    print(armstrong_number(12345))
    print(armstrong_number(123456))
    print(armstrong_number(1234567))
    print(armstrong_number(12345678))
    print(armstrong_number(123456789))
    print(armstrong_number(1234567890))
    print(armstrong_number(12345678901))
    print(armstrong_number(123456789012))
    print(armstrong_number(1234567890123))
    print(armstrong_number(12345678901234))
    print(armstrong_number(123456789012345))
    print(armstrong_number(1234567890123456))
    print(armstrong_number(12345678901234567))
    print(armstrong_number(123456789012345678))
    print(armstrong_number(1234567890123456789))
    print(armstrong_number(12345678901234567890))
    print(armstrong_number(123456789012345678901))
    print(armstrong_number(1234567890123456789012))
    print(armstrong_number(12345678901234567890123))
    print(armstrong_number(123456789012345678901234))
    print(armstrong_number(1234567890123456789012345))
    print(armstrong_number(12345678901234567890123456))
    print(armstrong_number(123456789012345678901234567))
    print(armstrong_number(1234567890123456789012345678))
    print(armstrong_number(12345678901234567890123456789))
    print(armstrong_number(123456789012345678901234567890))
    print(armstrong_number(1234567890123456789012345678901))
    print(armstrong_number(12345678901234567890123