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
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for i in range(len(txt)):
            if ord(txt[i]) % 2 == 1:
                count += 1
        return count

# Test cases
print(split_words("Hello world!")) # ["Hello", "world!"]
print(split_words("Hello,world!")) # ["Hello", "world!"]
print(split_words("abcdef")) # 3
print(split_words("a")) # 1
print(split_words("")) # 0
print(split_words("A")) # 0
print(split_words("Abcdef")) # 1
print(split_words("Abcdefg")) # 2
print(split_words("Abcdefgh")) # 3
print(split_words("Abcdefghij")) # 4
print(split_words("Abcdefghijk")) # 5
print(split_words("Abcdefghijkl")) # 6
print(split_words("Abcdefghijklm")) # 7
print(split_words("Abcdefghijklmn")) # 8
print(split_words("Abcdefghijklmnop")) # 9
print(split_words("Abcdefghijklmnopq")) # 10
print(split_words("Abcdefghijklmnopqr")) # 11
print(split_words("Abcdefghijklmnopqrs")) # 12
print(split_words("Abcdefghijklmnopqrst")) # 13
print(split_words("Abcdefghijklmnopqrstu")) # 14
print(split_words("Abcdefghijklmnopqrstuv")) # 15
print(split_words("Abcdefghijklmnopqrstuvw")) # 16
print(split_words("Abcdefghijklmnopqrstuvwx")) # 17
print(split_words("Abcdefghijklmnopqrstuvwxy")) # 18
print(split_words("Abcdefghijklmnopqrstuvwxyz")) # 19
print(split_words("Abcdefghijklmnopqrstuvwxyzabc")) # 20
print(split_words("Abcdefghijklmnopqrstuvwxyzabcd")) # 21
print(split_words("Abcdefghijklmnopqrstuvwxyzabcde")) # 22
print(split_words("Abcdefghijklmnopqrstuvwxyzabcdef")) # 23
print(split_words("Abcdefghijklmnopqrstuvwxyzabcdefg")) # 24
print(split_words("Abcdefghijklmnopqrstuvwxyzabcdefgh