def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    return ''.join([i for i in text if i not in 'aeiou'])


def remove_vowels_2(text):
    """
    remove_vowels_2 is a function that takes string and returns string without vowels.
    >>> remove_vowels_2('')
    ''
    >>> remove_vowels_2("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_2('abcdef')
    'bcdf'
    >>> remove_vowels_2('aaaaa')
    ''
    >>> remove_vowels_2('aaBAA')
    'B'
    >>> remove_vowels_2('zbcd')
    'zbcd'
    """
    return ''.join([i for i in text if i not in 'aeiou'])


def remove_vowels_3(text):
    """
    remove_vowels_3 is a function that takes string and returns string without vowels.
    >>> remove_vowels_3('')
    ''
    >>> remove_vowels_3("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_3('abcdef')
    'bcdf'
    >>> remove_vowels_3('aaaaa')
    ''
    >>> remove_vowels_3('aaBAA')
    'B'
    >>> remove_vowels_3('zbcd')
    'zbcd'
    """
    return ''.join(filter(lambda x: x not in 'aeiou', text))


def remove_vowels_4(text):
    """
    remove_vowels_4 is a function that takes string and returns string without vowels.
    >>> remove_vowels_4('')
    ''
    >>> remove_vowels_4("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_4('abcdef')
    'bcdf'
    >>> remove_vowels_4('aaaaa')
    ''
    >>> remove_vowels_4('aaBAA')
    'B'
    >>> remove_vowels_4('zbcd')
    'zbcd'
    """
    return ''.join(filter(lambda x: x not in 'aeiou', text))


def remove_vowels_5(text):
    """
    remove_vowels_5 is a function that takes string and returns string without vowels.
    >>> remove_vowels_5('')
    ''
    >>> remove_vowels_5("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_5('abcdef')
    'bcdf'
    >>> remove_vowels_5('aaaaa')
    ''
    >>> remove_vowels_5('aaBAA')
    'B'
    >>> remove_vowels_5('zbcd')
    'zbcd'
    """
    return ''.join(filter(lambda x: x not in 'aeiou', text))


def remove_vowels_6(text):
    """
    remove_vowels_6 is a function that takes string and returns string without vowels.
    >>> remove_vowels_6('')
    ''
    >>> remove_vowels_6("abcdef\nghijklm")
    'bcdf\nghjklm