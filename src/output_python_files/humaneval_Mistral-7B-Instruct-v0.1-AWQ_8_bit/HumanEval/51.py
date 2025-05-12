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
    vowels = 'aeiouAEIOU'
    text = text.translate(str.maketrans('', '', vowels))
    return text


def remove_vowels_in_words(text):
    """
    remove_vowels_in_words is a function that takes string and returns string with words without vowels.
    >>> remove_vowels_in_words('')
    ''
    >>> remove_vowels_in_words("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_in_words('abcdef')
    'bcdf'
    >>> remove_vowels_in_words('aaaaa')
    ''
    >>> remove_vowels_in_words('aaBAA')
    'B'
    >>> remove_vowels_in_words('zbcd')
    'zbcd'
    """
    words = text.split()
    for i in range(len(words)):
        words[i] = remove_vowels(words[i])
    return ' '.join(words)


def remove_vowels_in_sentence(text):
    """
    remove_vowels_in_sentence is a function that takes string and returns string with sentence without vowels.
    >>> remove_vowels_in_sentence('')
    ''
    >>> remove_vowels_in_sentence("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_in_sentence('abcdef')
    'bcdf'
    >>> remove_vowels_in_sentence('aaaaa')
    ''
    >>> remove_vowels_in_sentence('aaBAA')
    'B'
    >>> remove_vowels_in_sentence('zbcd')
    'zbcd'
    """
    sentence = text.split('. ')
    for i in range(len(sentence)):
        sentence[i] = remove_vowels_in_words(sentence[i])
    return ' '.join(sentence)


def remove_vowels_in_paragraph(text):
    """
    remove_vowels_in_paragraph is a function that takes string and returns string with paragraph without vowels.
    >>> remove_vowels_in_paragraph('')
    ''
    >>> remove_vowels_in_paragraph("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_in_paragraph('abcdef')
    'bcdf'
    >>> remove_vowels_in_paragraph('aaaaa')
    ''
    >>> remove_vowels_in_paragraph('aaBAA')
    'B'
    >>> remove_vowels_in_paragraph('zbcd')
    'zbcd'
    """
    paragraph = text.split('\n\n')
    for i in range(len(paragraph)):
        paragraph[i] = remove_vowels_in_sentence(paragraph[i])
    return '\n\n'.join(paragraph)


def remove_vowels_in_text(text):
    """
    remove_vowels_in_text is a function that takes string and returns string without vowels.
    >>> remove_vowels_in_text('')
    ''
    >>> remove_vowels_in_text("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_in_