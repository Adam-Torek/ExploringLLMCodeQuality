"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""


def number_ctr(string):
    """
    Write a python function to count number of digits in a given string.
    assert number_ctr('program2bedone') == 1
    """
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count


if __name__ == '__main__':
    print(number_ctr('program2bedone'))
    print(number_ctr('program2bedone2'))
    print(number_ctr('program2bedone22'))
    print(number_ctr('program2bedone222'))
    print(number_ctr('program2bedone2222'))
    print(number_ctr('program2bedone22222'))
    print(number_ctr('program2bedone222222'))
    print(number_ctr('program2bedone2222222'))
    print(number_ctr('program2bedone22222222'))
    print(number_ctr('program2bedone222222222'))
    print(number_ctr('program2bedone2222222222'))
    print(number_ctr('program2bedone22222222222'))
    print(number_ctr('program2bedone222222222222'))
    print(number_ctr('program2bedone2222222222222'))
    print(number_ctr('program2bedone22222222222222'))
    print(number_ctr('program2bedone222222222222222'))
    print(number_ctr('program2bedone2222222222222222'))
    print(number_ctr('program2bedone22222222222222222'))
    print(number_ctr('program2bedone222222222222222222'))
    print(number_ctr('program2bedone2222222222222222222'))
    print(number_ctr('program2bedone22222222222222222222'))
    print(number_ctr('program2bedone222222222222222222222'))
    print(number_ctr('program2bedone2222222222222222222222'))
    print(number_ctr('program2bedone22222222222222222222222'))
    print(number_ctr('program2bedone222222222222222222222222'))
    print(number_ctr('program2bedone2222222222222222222222222'))
    print(number_ctr('program2bedone22222222222222222222222222'))
    print(number_ctr('program2bedone222222222222222222222222222'))
    print(number_ctr('program2bedone2222222222222222222222222222'))
    print(number_ctr('program2bedone22222222222222222222222222222'))
    print(number_ctr('program2bedone2222222