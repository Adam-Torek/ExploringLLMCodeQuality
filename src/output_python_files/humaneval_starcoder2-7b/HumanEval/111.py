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
    if test == '':
        return {}
    else:
        test = test.split()
        test = [x for x in test]
        test = [x for x in test if x.isalpha()]
        test = [x.lower() for x in test]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]
        test = [x for x in test if x.islower()]
        test = [x for x in test if x.isalpha()]