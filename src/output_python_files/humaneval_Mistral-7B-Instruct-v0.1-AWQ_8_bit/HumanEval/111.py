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
    # initialize an empty dictionary
    result = {}
    # iterate over the string
    for letter in test:
        # check if the letter is in the dictionary
        if letter in result:
            # if it is, increment the count
            result[letter] += 1
        else:
            # if it is not, add the letter to the dictionary with a count of 1
            result[letter] = 1
    # return the dictionary
    return result

# test the function
print(histogram('a b c'))