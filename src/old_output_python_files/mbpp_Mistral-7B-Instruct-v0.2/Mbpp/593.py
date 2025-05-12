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
    for i in range(len(ip_list)):
        if ip_list[i] == '0':
            ip_list[i] = ''
            if i < len(ip_list) - 1 and ip_list[i+1] != '':
                ip_list[i] = str(int(ip_list[i]))
    return '.'.join(ip_list)

if __name__ == "__main__":
    assert removezero_ip("216.08.094.196") == '216.8.94.196'
    assert removezero_ip("192.168.0.0") == '192.168.0.0'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("1.2.3") == '1.2.3'
    assert removezero_ip("255.255.255.255") == '255.255.255.255'
    assert removezero_ip("123.0.0.123") == '123.0.0.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.123.123.123") == '123.123.123.123'
    assert removezero_ip("123.12