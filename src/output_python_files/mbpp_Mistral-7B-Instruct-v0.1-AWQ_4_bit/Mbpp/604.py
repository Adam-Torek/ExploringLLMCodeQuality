"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""
def reverse_words(string):
    """
    This function takes a string as an input and returns the string with words reversed.
    """
    # split the string by spaces
    words = string.split()
    # reverse the list of words
    words = words[::-1]
    # join the reversed list of words with spaces
    reversed_string = ' '.join(words)
    return reversed_string

# test the function
assert reverse_words("python program")==("program python")