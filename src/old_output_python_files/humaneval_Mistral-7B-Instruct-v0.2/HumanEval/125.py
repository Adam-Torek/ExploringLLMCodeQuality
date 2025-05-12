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
    if len(words) == 0:
        if any(char.isdigit() for char in txt):
            return [int(char) for char in txt]
        elif any(char.isalpha() for char in txt):
            odd_letters = []
            for char in txt:
                if char.isalpha() and ord(char) % 2 != 0:
                    odd_letters.append(char)
            return list(odd_letters)
        else:
            return [ord(char) for char in txt]
    return words

# Test Cases
print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
print(split_words("12345"))
print(split_words("zxczx"))
print(split_words("1a2b3c"))
print(split_words(""))
print(split_words("1234567890"))
print(split_words("z"))
print(split_words("zxczxczx"))
print(split_words("1234567890z"))
print(split_words("1234567890zxczx"))
print(split_words("1234567890zxczxczx"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zxczxczx1234567890"))
print(split_words("1234567890zx