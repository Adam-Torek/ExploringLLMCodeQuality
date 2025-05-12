def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # split the string into a list of words
    words = s.split()
    # create an empty list to store the ordered words
    ordered_words = []
    # iterate over the list of words
    for word in words:
        # create a new string with the characters of the word arranged in ascending order
        new_word = ''.join(sorted(word))
        # append the new word to the ordered_words list
        ordered_words.append(new_word)
    # join the ordered_words list with spaces to create the final string
    return ' '.join(ordered_words)