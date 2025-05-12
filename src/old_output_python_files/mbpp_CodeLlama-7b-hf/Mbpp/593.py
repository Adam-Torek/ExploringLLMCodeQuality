"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""


def removezero_ip(ip):
    """
    :param ip: ip address
    :return: ip address without leading zeroes
    """
    ip_list = ip.split('.')
    for i in range(len(ip_list)):
        if ip_list[i] == '0':
            ip_list[i] = ''
    return '.'.join(ip_list)


if __name__ == '__main__':
    print(removezero_ip('216.08.094.196'))
    print(removezero_ip('192.168.0.1'))
    print(removezero_ip('192.168.0.0'))
    print(removezero_ip('192.168.0.00'))
    print(removezero_ip('192.168.0.000'))
    print(removezero_ip('192.168.0.0000'))
    print(removezero_ip('192.168.0.00000'))
    print(removezero_ip('192.168.0.000000'))
    print(removezero_ip('192.168.0.0000000'))
    print(removezero_ip('192.168.0.00000000'))
    print(removezero_ip('192.168.0.000000000'))
    print(removezero_ip('192.168.0.0000000000'))
    print(removezero_ip('192.168.0.00000000000'))
    print(removezero_ip('192.168.0.000000000000'))
    print(removezero_ip('192.168.0.0000000000000'))
    print(removezero_ip('192.168.0.00000000000000'))
    print(removezero_ip('192.168.0.000000000000000'))
    print(removezero_ip('192.168.0.0000000000000000'))
    print(removezero_ip('192.168.0.00000000000000000'))
    print(removezero_ip('192.168.0.000000000000000000'))
    print(removezero_ip('192.168.0.0000000000000000000'))
    print(removezero_ip('192.168.0.00000000000000000000'))
    print(removezero_ip('192.168.0.000000000000000000000'))
    print(removezero_ip('192.168.0.0000000000000000000000'))
    print(removezero_ip('192.168.0.00000000000000000000000'))
    print(removezero_ip('192.168.0.000000000000000000000000'))
    print(removezero_ip('192.168.0.00000000000000000