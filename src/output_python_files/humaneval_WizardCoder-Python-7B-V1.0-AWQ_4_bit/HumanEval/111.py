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
    if not test:
        return {}
    test = test.split()
    hist = {}
    for letter in test:
        if letter in hist:
            hist[letter] += 1
        else:
            hist[letter] = 1
    max_count = max(hist.values())
    result = {}
    for key, value in hist.items():
        if value == max_count:
            result[key] = value
    return result



def test_histogram():
    assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    assert histogram('a b b a') == {'a': 2, 'b': 2}
    assert histogram('a b c a b') == {'a': 2, 'b': 2}
    assert histogram('b b b a') == {'b': 4}
    assert histogram('') == {}
    assert histogram('a a a a a a b b c c') == {'a': 4, 'b': 1, 'c': 1}
    assert histogram('a b c d e f g h i j k l m n o p q r s t u v w x y z') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
    assert histogram('a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z') == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2, 'k': 2, 'l': 2, 'm': 2, 'n': 2, 'o': 2, 'p': 2, 'q': 2, 'r': 2, 's': 2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2}
    assert histogram('a b c d e f g h i j k l m n o