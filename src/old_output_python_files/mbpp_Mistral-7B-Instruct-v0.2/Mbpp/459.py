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

if __name__ == '__main__':
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('') == ''
    assert remove_uppercase('abc') == 'abc'
    assert remove_uppercase('123') == '123'
    assert remove_uppercase('Hello World') == 'hello world'
    assert remove_uppercase('') is None
    assert remove_uppercase(None) is None
    assert remove_uppercase('12345') == '12345'
    assert remove_uppercase('12345a') == '12345'
    assert remove_uppercase('12345A') == '12345'
    assert remove_uppercase('12345AB') == '12345'
    assert remove_uppercase('12345ABC') == '12345'
    assert remove_uppercase('12345ABCDEF') == '12345'
    assert remove_uppercase('12345ABCDEFG') == '12345'
    assert remove_uppercase('12345ABCDEFGHI') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJ') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJK') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKL') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLM') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMN') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNO') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOP') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQ') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQR') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQRS') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQRST') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQRSTU') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQRSTUV') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQRSTUVW') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQRSTUVWX') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQRSTUVWXY') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQRSTUVWXYZ') == '12345'
    assert remove_uppercase('12345ABCDEFGHIJKLMNOPQRSTUVWXYZA') == '12