"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""
def is_undulating(num):
    """
    :param num: int
    :return: bool
    """
    num_str = str(num)
    prev_digit = num_str[0]
    for digit in num_str[1:]:
        if int(digit) > int(prev_digit):
            prev_digit = digit
        else:
            return False
    return True

if __name__ == "__main__":
    assert is_undulating(1212121) == True
    assert is_undulating(1111111) == False
    assert is_undulating(12345) == True
    assert is_undulating(123456) == False
    assert is_undulating(1234567) == True
    assert is_undulating(12345678) == False
    assert is_undulating(123456789) == True
    assert is_undulating(1234567891) == False
    assert is_undulating(12345678912) == True
    assert is_undulating(123456789123) == False
    assert is_undulating(1234567891234) == True
    assert is_undulating(12345678912345) == False
    assert is_undulating(123456789123456) == True
    assert is_undulating(1234567891234567) == False
    assert is_undulating(12345678912345678) == True
    assert is_undulating(123456789123456789) == False
    assert is_undulating(1234567891234567891) == True
    assert is_undulating(12345678912345678912) == False
    assert is_undulating(123456789123456789123) == True
    assert is_undulating(1234567891234567891234) == False
    assert is_undulating(12345678912345678912345) == True
    assert is_undulating(123456789123456789123456) == False
    assert is_undulating(1234567891234567891234567) == True
    assert is_undulating(12345678912345678912345678) == False
    assert is_undulating(123456789123456789123456789) == True
    assert is_undulating(1234567891234567891234567891) == False
    assert is_undulating(12345678912345678912345678912) == True
    assert is_undulating(123456789123456789123456789123) == False
    assert is_undulating(1234567891234567891234567891234) == True
    assert is_undulating(12345678912345678912345678912345) == False
    assert is_undulating(1234567