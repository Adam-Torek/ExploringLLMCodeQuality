"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""


def removezero_ip(ip):
    """
    :param ip:
    :return:
    """
    ip_list = ip.split('.')
    for i in range(len(ip_list)):
        if ip_list[i] == '0':
            ip_list[i] = ''
    return '.'.join(ip_list)


if __name__ == '__main__':
    print(removezero_ip('216.08.094.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.196'))
    print(removezero_ip('216.8.94.