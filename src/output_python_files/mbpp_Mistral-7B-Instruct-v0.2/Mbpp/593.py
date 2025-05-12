"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""
def removezero_ip(ip):
    """
    :param ip: string of ip address
    :return: string of ip address with leading zeroes removed
    """
    ip_list = ip.split('.')
    for index, value in enumerate(ip_list):
        if value.isdigit() and value[0] == '0':
            ip_list[index] = value[1:]
        elif value == '':
            ip_list[index] = '0'
    return '.'.join(ip_list)

if __name__ == '__main__':
    assert removezero_ip("216.08.094.196") == '216.8.94.196'
    assert removezero_ip("192.168.0.0") == '192.168.0.0'
    assert removezero_ip("123.45.67.89") == '123.45.67.89'
    assert removezero_ip("1.2.3") == '1.2.3'
    assert removezero_ip("") == ''
    assert removezero_ip("1") == '1'
    assert removezero_ip("255.255.255.255") == '255.255.255.255'
    assert removezero_ip("123.0.0.123") == '123.0.0.123'
    assert removezero_ip("123.0.0.0") == '123.0.0.0'
    assert removezero_ip("123.0.0") == '123.0.0'
    assert removezero_ip("123") == '123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123.123.123") == '123.123.123.123.123'
    assert removezero_ip("123.123.123.123.123.123.123") == '123.123.123.123.123.123'
    assert removezero_ip("123.123.123.123.123.123.123.123") == '123.123.123.123.123.123.123'
    assert removezero_ip("123.123.123.123.123.123.123.123.123") == '123.123.123.123.123.123.123.123'
    assert removezero_ip("123.123.123.123.123.123.123.123.123.123") == '123.123.123.123.123.123.123.123.123'
    assert removezero_ip("123.123.123.123.123.123.123.123.123.123.123") == '123.123.123.123.123.