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
print(split_words("a")) # 0
print(split_words("")) # 0
print(split_words("a,b,c,d,e,f,g")) # ["a", "b", "c", "d", "e", "f", "g"]
print(split_words("A,B,C,D,E,F,G")) # ["A", "B", "C", "D", "E", "F", "G"]
print(split_words("a,b,c,d,e,f,g,h")) # 3
print(split_words("A,B,C,D,E,F,G,H")) # 3
print(split_words("Hello,world,how,are,you")) # ["Hello", "world", "how", "are", "you"]
print(split_words("hello,world,how,are,you")) # ["hello", "world", "how", "are", "you"]
print(split_words("Hello,world,how,are,you")) # ["Hello", "world", "how", "are", "you"]
print(split_words("hello,world,how,are,you")) # ["hello", "world", "how", "are", "you"]
print(split_words("Hello,world,how,are,you")) # ["Hello", "world", "how", "are", "you"]
print(split_words("hello,world,how,are,you")) # ["hello", "world", "how", "are", "you"]
print(split_words("Hello,world,how,are,you")) # ["Hello", "world", "how", "are", "you"]
print(split_words("hello,world,how,are,you")) # ["hello", "world", "how", "are", "you"]
print(split_words("Hello,world,how,are,you")) # ["Hello", "world", "how", "are", "you"]
print(split_words("hello,world,how,are,you")) # ["hello", "world", "how", "are", "you"]
print(split_words("Hello,world,how,are,you")) # ["Hello", "world", "how", "are", "you"]
print(split_words("hello,world,how,are,you")) # ["hello", "world", "how", "are", "you"]
print(split_words("Hello,world,how,are,you")) # ["Hello", "world", "how", "