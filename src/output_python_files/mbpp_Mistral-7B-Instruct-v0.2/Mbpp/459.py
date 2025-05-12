"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""
def remove_uppercase(string):
    """
    :param string: string to remove uppercase substrings from
    :return: string with all uppercase substrings removed
    """
    return ''.join(filter(lambda x: x.islower(), string))

if __name__ == "__main__":
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('') == ''
    assert remove_uppercase('abc') == 'abc'
    assert remove_uppercase('ABC') == ''
    assert remove_uppercase('123') == '123'
    assert remove_uppercase('123ABC') == '123'
    assert remove_uppercase('123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC') == '123'
    assert remove_uppercase('123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC123ABC123ABC123') == '123'
    assert remove_uppercase('123ABC123ABC123ABC123ABC123ABC12