def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    words = []
    for word in txt.split():
        words.append(word)
    return words

def split_on_commas(txt):
    '''
    Given a string of words, return a list of words split on commas ','
    '''
    words = []
    for word in txt.split(','):
        words.append(word)
    return words

def split_on_odd_order_letters(txt):
    '''
    Given a string of words, return a list of words split on odd order letters in the alphabet
    '''
    words = []
    for word in txt.split():
        if len(word) > 1:
            if ord(word[0]) % 2 == 0 and ord(word[-1]) % 2 == 1:
                words.append(word)
    return words

def split_on_odd_order_letters_and_commas(txt):
    '''
    Given a string of words, return a list of words split on odd order letters in the alphabet and commas ','
    '''
    words = []
    for word in txt.split():
        if len(word) > 1:
            if ord(word[0]) % 2 == 0 and ord(word[-1]) % 2 == 1:
                words.append(word)
    return words

def split_on_odd_order_letters_and_commas_and_whitespace(txt):
    '''
    Given a string of words, return a list of words split on odd order letters in the alphabet, commas ',' and whitespace
    '''
    words = []
    for word in split_words(txt):
        if len(word) > 1:
            if ord(word[0]) % 2 == 0 and ord(word[-1]) % 2 == 1:
                words.append(word)
    return words

def split_on_odd_order_letters_and_commas_and_whitespace_and_numbers(txt):
    '''
    Given a string of words, return a list of words split on odd order letters in the alphabet, commas ',' whitespace and numbers
    '''
    words = []
    for word in split_words(txt):
        if len(word) > 1:
            if ord(word[0]) % 2 == 0 and ord(word[-1]) % 2 == 1:
                words.append(word)
    return words

def split_on_odd_order_letters_and_commas_and_whitespace_and_numbers_and_punctuation(txt):
    '''
    Given a string of words, return a list of words split on odd order letters in the alphabet, commas ',' whitespace, numbers and punctuation
    '''
    words = []
    for word in split_words(txt):
        if len(word) > 1:
            if ord(word[0]) % 2 == 0 and ord(word[-1