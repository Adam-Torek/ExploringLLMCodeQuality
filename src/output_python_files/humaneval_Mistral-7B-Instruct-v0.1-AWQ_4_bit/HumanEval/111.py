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
    # split the string into a list of characters
    char_list = test.split()
    # create an empty dictionary
    hist = {}
    # loop through the list of characters
    for char in char_list:
        # check if the character is in the dictionary
        if char in hist:
            # if it is, increment the count
            hist[char] += 1
        else:
            # if it is not, add the character to the dictionary with a count of 1
            hist[char] = 1
    # return the dictionary
    return hist

# test the function
print(histogram('a b c'))