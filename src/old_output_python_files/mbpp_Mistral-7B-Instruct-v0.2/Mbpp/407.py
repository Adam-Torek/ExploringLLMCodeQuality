"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""
def rearrange_bigger(num):
    """
    :param num: int
    :return: int
    """
    num_str = str(num)
    digits = [int(d) for d in num_str]
    digits.sort()
    index = digits.index(num % 10)
    return int(''.join([str(digits[i]) for i in range(len(digits)) if i != index and digits[i] > digits[index]] + [str(digits[index])] + [str(d) for d in digits[:index] if d < digits[index]]))

if __name__ == '__main__':
    assert rearrange_bigger(12) == 21
    assert rearrange_bigger(9876) == 98672
    assert rearrange_bigger(111) == 111
    assert rearrange_bigger(12345) == 54321
    assert rearrange_bigger(123456) == 654321
    assert rearrange_bigger(1234567) == 7654321
    assert rearrange_bigger(12345678) == 87654321
    assert rearrange_bigger(123456789) == 987654321
    assert rearrange_bigger(1234567891) == 1234567899
    assert rearrange_bigger(12345678910) == 10234567891
    assert rearrange_bigger(123456789101) == 101234567891
    assert rearrange_bigger(1234567891011) == 1101234567891
    assert rearrange_bigger(12345678910111) == 11101234567891
    assert rearrange_bigger(123456789101111) == 111101234567891
    assert rearrange_bigger(1234567891011111) == 1111101234567891
    assert rearrange_bigger(12345678910111111) == 11111101234567891
    assert rearrange_bigger(123456789101111111) == 111111101234567891
    assert rearrange_bigger(1234567891011111111) == 1111111101234567891
    assert rearrange_bigger(12345678910111111111) == 11111111101234567891
    assert rearrange_bigger(123456789101111111111) == 111111111101234567891
    assert rearrange_bigger(1234567891011111111111) == 1111111111101234567891
    assert rearrange_bigger(12345678910111111111111) == 1111