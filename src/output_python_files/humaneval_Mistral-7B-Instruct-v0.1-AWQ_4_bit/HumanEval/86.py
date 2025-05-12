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

    # create a new list of words where each word is sorted
    sorted_words = [sorted(word) for word in words]

    # join the sorted words back into a string
    return ' '.join(sorted_words)

# test the function
print(anti_shuffle('Hello World!!!'))