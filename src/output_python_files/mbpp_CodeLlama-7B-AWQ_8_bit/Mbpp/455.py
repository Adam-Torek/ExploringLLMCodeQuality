"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""


def check_monthnumb_number(month_number):
    if month_number in range(1, 13):
        if month_number in [1, 3, 5, 7, 8, 10, 12]:
            return True
        elif month_number in [4, 6, 9, 11]:
            return False
    else:
        return False


if __name__ == '__main__':
    print(check_monthnumb_number(5))
    print(check_monthnumb_number(13))
    print(check_monthnumb_number(1))
    print(check_monthnumb_number(14))
    print(check_monthnumb_number(10))
    print(check_monthnumb_number(11))
    print(check_monthnumb_number(12))
    print(check_monthnumb_number(13))
    print(check_monthnumb_number(14))
    print(check_monthnumb_number(15))
    print(check_monthnumb_number(16))
    print(check_monthnumb_number(17))
    print(check_monthnumb_number(18))
    print(check_monthnumb_number(19))
    print(check_monthnumb_number(20))
    print(check_monthnumb_number(21))
    print(check_monthnumb_number(22))
    print(check_monthnumb_number(23))
    print(check_monthnumb_number(24))
    print(check_monthnumb_number(25))
    print(check_monthnumb_number(26))
    print(check_monthnumb_number(27))
    print(check_monthnumb_number(28))
    print(check_monthnumb_number(29))
    print(check_monthnumb_number(30))
    print(check_monthnumb_number(31))
    print(check_monthnumb_number(32))
    print(check_monthnumb_number(33))
    print(check_monthnumb_number(34))
    print(check_monthnumb_number(35))
    print(check_monthnumb_number(36))
    print(check_monthnumb_number(37))
    print(check_monthnumb_number(38))
    print(check_monthnumb_number(39))
    print(check_monthnumb_number(40))
    print(check_monthnumb_number(41))
    print(check_monthnumb_number(42))
    print(check_monthnumb_number(43))
    print(check_monthnumb_number(44))
    print(check_monthnumb_number(45))
    print(check_monthnumb_number(46))
    print(check_monthnumb_number(47))
    print(check_monthnumb_number(48))
    print(check_monthnumb_number(49))
    print(check_monthnumb_number(50))
    print(check_monthnumb_number(51))
    print(check_monthnumb_number(52))
    print(check_monthnumb_number(53))
    print(check_monthnumb_number(54))
    print(check_monthnumb_number(55))
    print(check_monthnumb_number(56))
    print(check_monthnumb_number(57))
    print(check_monthnumb_number(58))
    print(check_monthnumb_number(59))
    print(check_monthnumb_number(60))
    print(check_monthnumb_number(61))
    print(check_monthnumb_number(62))
    print(check_monthnumb_number(63))
    print(check_monthnum