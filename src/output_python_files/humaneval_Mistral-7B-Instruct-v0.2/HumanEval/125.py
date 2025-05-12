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
    words = txt.split()
    if not words:
        if txt:
            words = [txt[i] for i in range(len(txt)) if ord(txt[i]) % 2 == 1]
            words = [chr(i) for i in words]
            words = [w.lower() for w in words]
            words = [w for w in words if len(w) > 0]
    return words

# Test Cases
print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
print(split_words(""))
print(split_words("12345"))
print(split_words("123,45"))
print(split_words("123,456"))
print(split_words("123,456,789"))
print(split_words("123,456,789,012"))
print(split_words("123,456,789,012,345"))
print(split_words("123,456,789,012,345,678"))
print(split_words("123,456,789,012,345,678,901"))
print(split_words("123,456,789,012,345,678,901,234"))
print(split_words("123,456,789,012,345,678,901,234,567"))
print(split_words("123,456,789,012,345,678,901,234,567,890"))
print(split_words("123,456,789,012,345,678,901,234,567,890,123"))
print(split_words("123,456,789,012,345,678,901,234,567,890,123,456"))
print(split_words("123,456,789,012,345,678,901,234,567,890,123,456,789"))
print(split_words("123,456,789,012,345,678,901,234,567,890,123,456,789,012"))
print(split_words("123,456,789,012,345,678,901,2