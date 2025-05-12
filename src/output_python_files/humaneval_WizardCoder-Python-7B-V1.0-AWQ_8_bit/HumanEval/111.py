def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    hist = {}
    for letter in test.split():
        if letter in hist:
            hist[letter] += 1
        else:
            hist[letter] = 1
    return hist



# Test cases
print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))  # {'a': 2, 'b': 2}
print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
print(histogram('b b b a'))  # {'b': 3}
print(histogram(''))  # {}
print(histogram('a a a a a a b b c c d d d d d'))  # {'a': 4, 'd': 4}
print(histogram('a b c d e f g h i j k l m n o p q r s t u v w x y z'))  # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}


# Test cases for edge cases
print(histogram('a b c d e f g h i j k l m n o p q r s t u v w x y z'))  # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
print(histogram(' '))  # {}
print(histogram(''))  # {}
print(histogram('a'))  # {'a': 1}
print(histogram('aaa'))  # {'a': 3}
print(histogram('aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp qqq rrr sss ttt uuu vvv www xxx yyy zzz'))  # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z