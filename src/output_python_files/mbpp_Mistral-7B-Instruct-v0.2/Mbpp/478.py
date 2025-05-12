"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
def remove_lowercase(string):
    """
    :param string: string to remove lowercase substrings from
    :return: string with all lowercase substrings removed
    """
    return ''.join(filter(lambda x: x.isupper() or not x, string))

if __name__ == "__main__":
    assert remove_lowercase("PYTHon") == "PYTH"
    assert remove_lowercase("PyThOn") == "PYTH"
    assert remove_lowercase("PyThOn123") == "PYTH123"
    assert remove_lowercase("PyThOn_123") == "PYTH_123"
    assert remove_lowercase("PyThOn!@#$%^&*()_+-=[]{}|;:,.<>/?`~") == "PYTH!@#$%^&*()_+-=[]{}|;:,.<>/?`~"
    assert remove_lowercase("") == ""
    assert remove_lowercase("abc") == ""
    assert remove_lowercase("ABC") == "ABC"
    assert remove_lowercase("123") == "123"
    assert remove_lowercase("1A2b3C") == "1A3C"
    assert remove_lowercase("1A2b3cD") == "1A3cD"
    assert remove_lowercase("1A2b3c dE") == "1A3c dE"
    assert remove_lowercase("1A2b3c dE F") == "1A3c dE F"
    assert remove_lowercase("1A2b3c dE Fg") == "1A3c dE Fg"
    assert remove_lowercase("1A2b3c dE FgH") == "1A3c dE FgH"
    assert remove_lowercase("1A2b3c dE FgHi") == "1A3c dE FgHi"
    assert remove_lowercase("1A2b3c dE FgHiJ") == "1A3c dE FgHiJ"
    assert remove_lowercase("1A2b3c dE FgHiJk") == "1A3c dE FgHiJk"
    assert remove_lowercase("1A2b3c dE FgHiJkl") == "1A3c dE FgHiJkl"
    assert remove_lowercase("1A2b3c dE FgHiJklm") == "1A3c dE FgHiJklm"
    assert remove_lowercase("1A2b3c dE FgHiJklmn") == "1A3c dE FgHiJklmn"
    assert remove_lowercase("1A2b3c dE FgHiJklmno") == "1A3c dE FgHiJklmno"
    assert remove_lowercase("1A2b3c dE FgHiJklmnop") == "1A3c dE FgHiJklmnop"
    assert remove_lowercase("1A2b3c dE FgHiJklmnoq") == "1A3c dE FgHiJklmnoq"
    assert remove_lowercase("1A2b3c dE FgHiJklmnoqr") == "1A3c dE FgHiJklmnoqr"
    assert remove_lowercase("1A2b3c dE FgHiJklmnoqrs") == "1A3c dE FgHiJklmnoqrs"
    assert remove_lowercase("1A2b3c dE FgHiJklmnoqrst") == "1A3c dE FgHiJklmnoqrst"
    assert remove_lowercase("1A2b3c dE FgHiJklmnoqrstu") == "1A3c dE FgHiJklmnoqrstu"
    assert remove_lowercase("1A2b3c dE