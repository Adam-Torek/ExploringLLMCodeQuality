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
    print(number_ctr('program2bedone1'))
    print(number_ctr('program2bedone12'))
    print(number_ctr('program2bedone123'))
    print(number_ctr('program2bedone1234'))
    print(number_ctr('program2bedone12345'))
    print(number_ctr('program2bedone123456'))
    print(number_ctr('program2bedone1234567'))
    print(number_ctr('program2bedone12345678'))
    print(number_ctr('program2bedone123456789'))
    print(number_ctr('program2bedone1234567890'))
    print(number_ctr('program2bedone12345678901'))
    print(number_ctr('program2bedone123456789012'))
    print(number_ctr('program2bedone1234567890123'))
    print(number_ctr('program2bedone12345678901234'))
    print(number_ctr('program2bedone123456789012345'))
    print(number_ctr('program2bedone1234567890123456'))
    print(number_ctr('program2bedone12345678901234567'))
    print(number_ctr('program2bedone123456789012345678'))
    print(number_ctr('program2bedone1234567890123456789'))
    print(number_ctr('program2bedone12345678901234567890'))
    print(number_ctr('program2bedone123456789012345678901'))
    print(number_ctr('program2bedone1234567890123456789012'))
    print(number_ctr('program2bedone12345678901234567890123'))
    print(number_ctr('program2bedone123456789012345678901234'))
    print(number_ctr('program2bedone1234567890123456789012345'))
    print(number_ctr('program2bedone12345678901234567890123456'))
    print(number_ctr('program2bedone123456789012345678901234567'))
    print(number_ctr('program2bedone1234567890123456789012345678'))
    print(number_ctr('program2bedone12345678901234567890123456789'))
    print(number_ctr('program2bedone1234567