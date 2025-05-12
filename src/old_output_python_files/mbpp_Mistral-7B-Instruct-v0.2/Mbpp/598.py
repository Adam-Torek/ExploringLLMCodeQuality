"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
import math

def armstrong_number(num):
    """
    :param num: integer
    :return: boolean
    """
    power = len(str(num))
    sum = 0
    original_num = num

    while num > 0:
        digit = num % 10
        sum += digit ** power
        num //= 10

    if sum == original_num:
        return True
    else:
        return False

if __name__ == "__main__":
    assert armstrong_number(153) == True
    assert armstrong_number(370) == True
    assert armstrong_number(371) == False
    assert armstrong_number(407) == True
    assert armstrong_number(1634) == True
    assert armstrong_number(8208) == True
    assert armstrong_number(9474) == True
    assert armstrong_number(9475) == False
    assert armstrong_number(1357) == True
    assert armstrong_number(1358) == False
    assert armstrong_number(1365) == True
    assert armstrong_number(1373) == True
    assert armstrong_number(1382) == False
    assert armstrong_number(1395) == True
    assert armstrong_number(1428) == True
    assert armstrong_number(1453) == True
    assert armstrong_number(1454) == False
    assert armstrong_number(1460) == True
    assert armstrong_number(1462) == True
    assert armstrong_number(1490) == True
    assert armstrong_number(1492) == True
    assert armstrong_number(1530) == False
    assert armstrong_number(1560) == True
    assert armstrong_number(1561) == True
    assert armstrong_number(1562) == True
    assert armstrong_number(1563) == True
    assert armstrong_number(1564) == True
    assert armstrong_number(1565) == True
    assert armstrong_number(1566) == True
    assert armstrong_number(1567) == True
    assert armstrong_number(1568) == True
    assert armstrong_number(1569) == True
    assert armstrong_number(1570) == True
    assert armstrong_number(1571) == True
    assert armstrong_number(1572) == True
    assert armstrong_number(1573) == True
    assert armstrong_number(1574) == True
    assert armstrong_number(1575) == True
    assert armstrong_number(1576) == True
    assert armstrong_number(1577) == True
    assert armstrong_number(1578) == True
    assert armstrong_number(1579) == True
    assert armstrong_number(1580) == True
    assert armstrong_number(1581) == True
    assert armstrong_number(1582) == True
    assert armstrong_number(1583) == True
    assert armstrong_number(1584) == True
    assert armstrong_number(1585) == True
    assert armstrong_number(1586) == True
    assert armstrong_number(1587) == True
    assert armstrong_number(1588) == True
    assert armstrong_number(1589) == True
    assert armstrong_number(1590) == True
    assert armstrong_number(1591) == True
    assert armstrong_number(1592) == True
    assert armstrong_number(1593) == True
    assert armstrong_number(1594) == True
    assert armstrong_number(1595) == True
    assert arm