"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""
def rearrange_bigger(num):
    """
    :param num: int
    :return: int
    """
    str_num = str(num)
    digits = sorted(list(set(str_num)))
    index = str_num.index(str(digits[-1]))
    left = str_num[:index]
    right = str_num[index:]
    return int(left + str(digits[-1]) + str(right)[::-1])

if __name__ == "__main__":
    assert rearrange_bigger(12) == 21
    assert rearrange_bigger(9876) == 9867
    assert rearrange_bigger(12345) == 54321
    assert rearrange_bigger(11111) == None
    assert rearrange_bigger(123) == 321
    assert rearrange_bigger(1230) == 3210
    assert rearrange_bigger(1234) == 4321
    assert rearrange_bigger(12345) == 54321
    assert rearrange_bigger(123456) == 654321
    assert rearrange_bigger(1234567) == 7654321
    assert rearrange_bigger(12345678) == 87654321
    assert rearrange_bigger(123456789) == 987654321
    assert rearrange_bigger(1234567890) == 9876543210
    assert rearrange_bigger(12345678901) == 1012345678909
    assert rearrange_bigger(123456789012) == 1201345678909
    assert rearrange_bigger(1234567890123) == 12301345678909
    assert rearrange_bigger(12345678901234) == 12340135678909
    assert rearrange_bigger(123456789012345) == 12345013678909
    assert rearrange_bigger(1234567890123456) == 123456013678909
    assert rearrange_bigger(12345678901234567) == 1234567013678909
    assert rearrange_bigger(123456789012345678) == 12345678013678909
    assert rearrange_bigger(1234567890123456789) == 123456789013678909
    assert rearrange_bigger(12345678901234567890) == 1234567890136789090
    assert rearrange_bigger(123456789012345678901) == 12345678901367890901
    assert rearrange_bigger(1234567890123456789012) == 1