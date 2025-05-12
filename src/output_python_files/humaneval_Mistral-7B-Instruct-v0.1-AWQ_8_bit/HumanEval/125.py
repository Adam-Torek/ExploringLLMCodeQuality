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
    Examples
    split_on_commas("Hello world!") ➞ ["Hello", "world!"]
    split_on_commas("Hello,world!") ➞ ["Hello", "world!"]
    '''
    words = []
    for word in txt.split(','):
        words.append(word)
    return words

def split_on_odd_order_letters(txt):
    '''
    Given a string of words, return a list of words split on odd order letters in the alphabet
    Examples
    split_on_odd_order_letters("Hello world!") ➞ ["Hello", "world!"]
    split_on_odd_order_letters("abcdef") == 3
    '''
    words = []
    for word in txt.split():
        if len(word) % 2 == 1:
            words.append(word)
    return words

def split_on_odd_order_letters_and_commas(txt):
    '''
    Given a string of words, return a list of words split on odd order letters in the alphabet and commas ','
    Examples
    split_on_odd_order_letters_and_commas("Hello world!") ➞ ["Hello", "world!"]
    split_on_odd_order_letters_and_commas("abcdef") == 3
    '''
    words = []
    for word in txt.split(','):
        if len(word) % 2 == 1:
            words.append(word)
    return words

def split_on_odd_order_letters_and_commas_and_whitespace(txt):
    '''
    Given a string of words, return a list of words split on odd order letters in the alphabet, commas ',' and whitespace
    Examples
    split_on_odd_order_letters_and_commas_and_whitespace("Hello world!") ➞ ["Hello", "world!"]
    split_on_odd_order_letters_and_commas_and_whitespace("abcdef") == 3
    '''
    words = []
    for word in txt.split():
        if len(word) % 2 == 1:
            words.append(word)
    return words